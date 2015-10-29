import os
import modules
import datasources
import config
from communication import Bus

instances = {}

def getBus():
	return Bus( config.getItems('sits', 'Bus') )

def getModules():

	typeName = 'modules'
	modules = []

	for moduleName in config.getSections(typeName, typeName):
		modules.append(getModule(moduleName))

	return modules

def getDatasource(datasourceName, userParams):
	typeName = 'datasources'
	datasourceConfig = config.getItems(typeName, datasourceName)
	datasourceConfig.update(userParams)

	datasourceClass = getattr(datasources, datasourceName)
	return datasourceClass(datasourceConfig)

def getModule(moduleName):
	typeName = 'modules'
	moduleConfig = config.getItems(typeName, moduleName)
	sitsConfig = config.getItems('sits', 'General')
	moduleConfig.update(sitsConfig)


	moduleClass = getattr(modules, moduleName)
	return moduleClass(moduleConfig)