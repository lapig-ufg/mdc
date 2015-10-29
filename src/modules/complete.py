import utils
import os
from _module import Module

class Complete(Module):

	def __init__(self, config):
		Module.__init__(self, config)

	def process(self, message):
		layer = message.get('layer')
		tmpFiles = message.get('tmpFiles')

		originPath = layer['file']
		
		destinationFilename = os.path.basename(layer['file'])
		destinationPath = os.path.join(self.module_path, destinationFilename)

		utils.log(self.name, 'Removing temp files')
		for tmpFile in tmpFiles:
			utils.removeFileIfExist(tmpFile)

		utils.moveFile(originPath, destinationPath)
		utils.log(self.name, destinationFilename, ' is ready to use !!!')