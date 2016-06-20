import os
import shutil
import json
import datetime
import time
import traceback
import parsemodis2
import convertmodis2
from sys import exit
from os import path
from pymodis import downmodis
from subprocess import Popen, PIPE
import utils

class ModisAcess:

	def __init__(self, productName, layers, tiles, start, end, targetPath, mrtPath, extentCmd):

		self.tiles = tiles
		self.layers = layers
		self.mrtPath = mrtPath
		self.extentCmd = extentCmd;
		self.end = end.encode("ascii")
		self.start = start.encode("ascii")
		self.targetPath = targetPath.encode("ascii")
		self.productName = productName.encode("ascii")

	def __createTifName(self, archive):
		return archive.replace("hdf", "tif")

	def __createSpectralBases(self):
		baseLayer = []
		for i in range(len(self.layers)):
				baseLayer.append('0')

		baseStr = []
		for i in range(len(self.layers)):
				aux = list(baseLayer)
				aux[i] = '1'
				txt = "( "

				for letter in aux:
						txt += letter + ' '

				txt += ')'
				baseStr.append(txt)
		
		return baseStr
	
	def reproject(self):

		for filename in os.listdir(self.targetPath):
			if filename.endswith(".hdf"):
				for spectralBase in self.__createSpectralBases():

					hdfFile = path.join(self.targetPath, filename)
					tifFile = path.join(self.targetPath, self.__createTifName(filename))

					extent = self.getModisTileExtent(hdfFile)

					modisParse = parsemodis2.parseModis(hdfFile)
					confname = modisParse.confResample(spectral=spectralBase,
						output=tifFile, bound=extent)

					modisCover = convertmodis2.convertModis(
						hdfname=hdfFile, confile=confname,
						mrtpath=self.mrtPath)

					modisCover.run()

	def download(self):

		modisObj = downmodis.downModis(
			url="http://e4ftl01.cr.usgs.gov",
			user="anonymous", password=None, path="MOLT",
			timeout=3600, destinationFolder=self.targetPath, jpg=False,
			debug=True, tiles=self.tiles,
			today=self.end, enddate=self.start,
			product=self.productName)

		continueLoop = True

		while(continueLoop):
			try:
				print('download')
				modisObj.connect()
				modisObj.downloadsAllDay(clean=True, allDays=False)
				continueLoop = False
			except:
				traceback.print_exc()
				time.sleep(10)
				print('try again')
				pass

	def getModisTileExtent(self, filepath):
		command = [self.extentCmd, self.mrtPath, filepath]

		print command
		process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		extent, err = process.communicate()

		if err == '':
			print("######################", extent)
			coordArray = extent.rstrip('\n').split(' ')

			return {
				'min_lat': coordArray[2],
				'min_lon': coordArray[1],
				'max_lat': coordArray[0],
				'max_lon': coordArray[3]
			}
		else:
			print err
			return None
