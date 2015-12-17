import os
import shutil
import json
import datetime
import time
import traceback
from sys import exit
from os import path
from pymodis import downmodis
from pymodis import parsemodis
from pymodis import convertmodis
import utils

class ModisAcess:

	def __init__(self, productName, layers, tiles, start, end, targetPath, mrtPath):

		self.tiles = tiles
		self.layers = layers
		self.mrtPath = mrtPath
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

					modisParse = parsemodis.parseModis(hdfFile)
					confname = modisParse.confResample(spectral=spectralBase,
						output=tifFile)

					modisCover = convertmodis.convertModis(
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