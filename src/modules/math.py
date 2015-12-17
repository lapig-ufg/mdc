import os
import utils
from _module import Module
from tools import gdal_utils

class Math(Module):

	def __init__(self, config):
		Module.__init__(self, config)

	def process(self, message):
		
		layer = message.get('layer')
		math = message.get('math')
		primaryMath = math['primary']

		if layer in primaryMath:
			layerMath = primaryMath[layer]
			expression = layerMath['expression']
			dataType = layerMath['datatype']
			
			inputFilepath = layer['file'];
			inputFilename = os.path.basename(inputFilepath)

			outputFilename = "_".join([productName, layer['name'], startYear + startDoy, region]) + '.tif'
			outputFilepath = os.path.join(self.module_path, outputFilename)

			expression = expression.replace('{' + layer['name'] + '}', '{0}')

			utils.removeFileIfExist(outputFilepath)
			utils.log(self.name, 'Expression calculation', outputFilename, expression)
			gdal_utils.calc([inputFilepath], outputFilepath, expression, dataType)

			tmpFiles = message.get('tmpFiles')
			tmpFiles.append(layer['file'])
			message.set('tmpFiles', tmpFiles)

			layer['file'] = outputFilepath
			message.set('layer', layer)

			utils.log(self.name, 'Forward message (', outputFilename, ')')
			self.publish(message)