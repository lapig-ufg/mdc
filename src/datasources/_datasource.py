import time
import loader
import subprocess
import json
import datetime
import inspect
from communication import Message

class Datasource:
	def __init__(self, config):
		for key in config:
			setattr(self, key, config[key])

		self.gridName = self.__class__.__name__.lower()
		self.tiles = self.__getTiles()

	def generateMessages(self):
		
		messages = [];

		for date in self.__getDates():
			message = Message()
			
			for attrName in dir(self):
				value = getattr(self, attrName)
				if not attrName.startswith('_') and not inspect.ismethod(value):
					message.set(attrName, value)

			message.set('start', date['start']);
			message.set('end', date['end']);
			message.set('tmpFiles', [])
			message.set('startDoy', self.__getDayOfYear(date['start']).zfill(3) );
			message.set('startYear', self.__getYear(date['start']) );

			messages.append(message)

		return messages

	def __getYear(self, strDate):
		return str(self.__convertDate(strDate).timetuple().tm_year)

	def __getDayOfYear(self, strDate):
		return str(self.__convertDate(strDate).timetuple().tm_yday)

	def __getTiles(self):
		sql = "SELECT A.TILES FROM {grid} A, {region} B WHERE ST_Intersects(A.geometry, B.geometry)".format( grid=self.gridName, region=self.region.capitalize() )
		command = "ogr2ogr -f GeoJSON -sql \"{sql}\" -dialect SQLITE /vsistdout/ {shpDir}".format( sql=sql, shpDir=self.path_shp)

		p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		(output, err) = p.communicate()

		geoJson = json.loads(unicode(output, "utf-8"))
		tiles = []

		for feature in geoJson['features']:
			tiles.append(feature['properties']['TILES'])

		return tiles
		
	def __getDates(self):
		
		startDate = self.__convertDate(self.start)
		endDate = self.__convertDate(self.end)

		productStartDate = self.__convertDate(self.productStart)
		productEndDate = self.__convertDate(self.productEnd)

		if startDate < productStartDate:
			startDate = productStartDate
		if endDate > productEndDate:
			endDate = productEndDate

		dateList = []

		start = startDate
		end = start
		
		temporalResolution = self.temporalResolution
		if self.temporalResolution > 1:
			temporalResolution -= 1

		while end < endDate:

			end = start + datetime.timedelta(days=temporalResolution)

			if start.year != end.year:
				end = start + datetime.timedelta(days=(31 - start.day))

			if end > endDate:
					end = endDate

			dateList.append(
					{
							"start" : start.strftime("%Y-%m-%d"),
							"end" : end.strftime("%Y-%m-%d")
					}
			)

			start = end
			start = start + datetime.timedelta(days=1)

		return dateList

	def __convertDate(self, strDate):
		try:
				if strDate is None:
					return datetime.datetime.now()
				else:
					return datetime.datetime.strptime(strDate, "%Y-%m-%d")
		except:
				exit("[DOWNLOAD MODULE ] |-> Error: '%s' have a " % strDate \
								+ "wrong date format, use YYYY-MM-DD")