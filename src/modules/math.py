import os
import utils
from _module import Module
from tools import gdal_utils

class Math(Module):

	def __init__(self, config):
		Module.__init__(self, config)

	def process(self, message):
		
		math = message.get('math')
		layer = message.get('layer')
		primaryMath = math['primary']

		layerName = layer['name']

		if layerName in primaryMath:
			noData = layer['nodata']
			layerMath = primaryMath[layerName]
			
			dataType = layerMath['datatype']
			expression = layerMath['expression']
			
			inputFilepath = layer['file'];
			inputFilename = os.path.basename(inputFilepath)

			outputFilename = inputFilename
			outputFilepath = os.path.join(self.module_path, outputFilename)

			expression = expression.replace('{' + layerName + '}', '{0}')

			utils.removeFileIfExist(outputFilepath)
			utils.log(self.name, 'Expression calculation', outputFilename, expression)
			gdal_utils.calc([inputFilepath], outputFilepath, expression, dataType, noData)

			tmpFiles = message.get('tmpFiles')
			tmpFiles.append(layer['file'])
			message.set('tmpFiles', tmpFiles)

			layer['file'] = outputFilepath
			message.set('layer', layer)

		utils.log(self.name, 'Forward message (', layerName, ')')
		self.publish(message)