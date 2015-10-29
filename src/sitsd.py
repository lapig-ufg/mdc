import loader
from sys import argv
from common import mapDict
from multiprocessing import Process
from communication import Message

def main():
	
	for module in loader.getModules():
		for i in xrange(0, module.number_of_workers):
			p = Process(target=module.run)
			p.start()

if __name__ == "__main__":
	main()
