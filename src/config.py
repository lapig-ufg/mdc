import os
from ConfigParser import SafeConfigParser

sitsPath, filename = os.path.split(os.path.abspath(__file__))

def getSections(fileName, sectionName):
	cp = __loadConfigParser(fileName)
	return cp.sections()

def getItems(fileName, sectionName):

	cp = __loadConfigParser(fileName)

	config = {}
	for key, values in cp.items(sectionName):
		config[key] = values.format(sits_path=sitsPath)

	return config

def __loadConfigParser(fileName):
	cp = SafeConfigParser()
	filePath = os.path.join(sitsPath, 'conf', fileName + ".conf")
	cp.read(filePath)
	return cp