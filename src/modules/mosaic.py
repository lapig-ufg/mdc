import os
import utils
from _module import Module
from tools import gdal_utils

class Mosaic(Module):

	def __init__(self, config):
		Module.__init__(self, config)

	def process(self, message):
		
		end = message.get('end')
		start = message.get('start')
		startDoy = message.get('startDoy')
		startYear = message.get('startYear')
		layer = message.get('layer')
		region = message.get('region')
		productName = message.get('productName').replace('.','_')

		outputFilename = "_".join([productName, layer['name'], startDoy, startYear, region]) + '.tif'
		outputFilepath = os.path.join(self.module_path, outputFilename)

		utils.removeFileIfExist(outputFilepath)

		utils.log(self.name, 'Generating', outputFilename, 'merging', str(len(layer['files'])), 'files')
		gdal_utils.mosaic(layer['files'], outputFilepath, layer['nodata'])

		tmpFiles = message.get('tmpFiles')
		tmpFiles += layer['files']
		message.set('tmpFiles', tmpFiles)

		del layer['files']
		layer['file'] = outputFilepath
		message.set('layer', layer)

		utils.log(self.name, 'Forward message (', outputFilename, ')')
		self.publish(message)