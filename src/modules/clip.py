import os
import utils
from _module import Module
from tools import gdal_utils

class Clip(Module):

	def __init__(self, config):
		Module.__init__(self, config)

	def process(self, message):
		
		end = message.get('end')
		start = message.get('start')
		layer = message.get('layer')
		region = message.get('region')
		pathShp = message.get('path_shp')
		productName = message.get('productName').replace('.','_')

		inputFilepath = layer['file'];
		inputFilename = os.path.basename(inputFilepath)

		outputFilename = "_".join([productName, layer['name'], start, end, region]) + '.tif'
		outputFilepath = os.path.join(self.module_path, outputFilename)

		utils.removeFileIfExist(outputFilepath)

		shapeFilepath = os.path.join(pathShp, region.lower() + '.shp')
		
		utils.log(self.name, 'Generating', outputFilename, ' by region ', region)
		gdal_utils.clip(inputFilepath, outputFilepath, shapeFilepath, layer['nodata'])

		tmpFiles = message.get('tmpFiles')
		tmpFiles.append(layer['file'])
		message.set('tmpFiles', tmpFiles)

		layer['file'] = outputFilepath
		message.set('layer', layer)

		utils.log(self.name, 'Forward message (', outputFilename, ')')
		self.publish(message)
