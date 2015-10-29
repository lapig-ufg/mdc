import loader
from sys import argv
from common import mapDict
from multiprocessing import Process
from communication import Message

usage = """\
Usage: %s [OPTIONS]
		-d      name of satellite observation program
		-p      product name
		-r      download specifics tiles of this region
		-s      start date of image that will be download
		-e      end date of images that will be download
		[-i]    index formula to apply
""" % argv[0]

def main():
	argDict = mapDict(argv, usage)

	if "-d" in argDict and "-p" in argDict and "-r" in argDict \
						and "-s" in argDict and "-e" in argDict:

				datasourceName = argDict["-d"].capitalize()
				productName = argDict["-p"]
				region = argDict["-r"]
				start = argDict["-s"]
				end = argDict["-e"]

				datasourceConfig = {
						"productName": productName
					,	"region": region
					,	"start": start
					,	"end": end
				}

				bus = loader.getBus()
				datasource = loader.getDatasource(datasourceName,datasourceConfig)
				for message in datasource.generateMessages():
					bus.publishMessage(datasourceName, message)
					

	else:
			exit(usage)

if __name__ == "__main__":
	main()
