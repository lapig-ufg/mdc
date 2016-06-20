import os
import loader
import config
from sys import argv
from multiprocessing import Process
from communication import Message

def main():
	
	os.environ["PATH"] += os.pathsep + os.pathsep.join(config.getIntegrationsPath())

	for module in loader.getModules():
		for i in xrange(0, module.number_of_workers):
			p = Process(target=module.run)
			p.start()

if __name__ == "__main__":
	main()
