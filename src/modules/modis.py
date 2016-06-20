import os
import utils
import time
from tools import ModisAcess
from _module import Module

class Modis(Module):

	def __init__(self, config):
		Module.__init__(self, config)

	def process(self, message):

		self.message = message

		end = message.get('end')
		start = message.get('start')
		tiles = message.get('tiles')
		startDoy = message.get('startDoy')
		startYear = message.get('startYear')
		pathMrt = message.get('path_mrt')
		product = message.get('product');
		productName = message.get('productName')

		layers = product['bands'];

		tiles = ",".join(tiles).lower()
		noTiles = ('noTiles' in product and product['noTiles'])
		if noTiles:
			tiles = None

		tmpDir = "_".join(['tmp', productName, startYear + startDoy])
		tmpPath = os.path.join(self.module_path, tmpDir)
		utils.createDir(tmpPath)
		time.sleep(1)
		
		self.__downloadAndReproject(productName=productName, tiles=tiles, 
			start=start, end=end, layers=layers, 
			tmpPath=tmpPath, pathMrt=pathMrt);

		layerFiles = self.__moveLayerFiles(tmpPath, self.module_path)
		#utils.removeDir(tmpPath)

		for layer in self.__getLayers(layers, layerFiles):
			message.set('layer', layer)
			self.publish(message)
			utils.log(self.name, 'Forward message (', productName , layer['name'], ')')

	def __downloadAndReproject(self, productName, tiles, start, end, layers, tmpPath, pathMrt):

		modisAcess = ModisAcess(productName=productName, tiles=tiles, 
			start=start, end=end, layers=layers, 
			targetPath=tmpPath, mrtPath=pathMrt, extentCmd=self.extent_cmd)
		
		utils.log(self.name, 'Downloading', productName, start, end, tiles)
		modisAcess.download()

		utils.log(self.name, 'Reprojecting', productName, start, end, tiles)
		modisAcess.reproject()

	def __getLayers(self, layers, layerFiles):

		layersMap = {}

		for layerFile in layerFiles:
			layername = self.__getLayername(layerFile)
			
			if layername not in layersMap:
				noData = layers[layername]
				if noData is not None:
					noData = utils.number(noData);

				layersMap[layername] = { 
					"name": layername, 
					"nodata": noData,
					"files": []
				}

			layersMap[layername]['files'].append(layerFile)

		layersList = []
		for key in layersMap:
			layersList.append(layersMap[key])

		return layersList

	def __moveLayerFiles(self, originPath, destinationPath):

		result = []

		for filename in os.listdir(originPath):
			if filename.endswith(".tif"):
				originFilepath = os.path.join(originPath, filename)
				destinationFilepath = os.path.join(destinationPath, filename)

				utils.moveFile(originFilepath, destinationFilepath)
				result.append(destinationFilepath)

		return result

	def __getLayername(self, layerFile):
		return layerFile.split('.')[-2]