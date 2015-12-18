import time
import os
import loader
import utils
import traceback
from communication import Message

class Module:
	def __init__(self, config):
		for key in config:
			setattr(self, key, config[key])

		self.__setDefaultValues()
		self.__initBus()
		
		utils.createDir(self.module_path)

	def __setDefaultValues(self):
		className = self.__class__.__name__.lower()
		
		defaultValues = {
				'subcribe_channel': className.capitalize()
			,	'name': className.capitalize()
			,	'number_of_workers': 1
			,	'sleep_time': 5
			, 'module_path': os.path.join(self.path_workdir, className)
			, 'debug_flag' : 0
		}

		for key in defaultValues:
			if not hasattr(self, key):
				setattr(self, key, defaultValues[key])

		self.number_of_workers = int(self.number_of_workers)
		self.sleep_time = float(self.sleep_time)
		self.publish_channel = self.publish_channel.capitalize()
		self.debug_flag = int(self.debug_flag)

	def __initBus(self):
		self.bus = loader.getBus()
		self.bus.subscribe(self.subcribe_channel)

	def run(self):
		utils.log(self.name, 'started')
		while True:
			message = self.getMessage()
			utils.log(self.name, 'Message received')
			try:
				result = self.process(message)
			except:
				traceback.print_exc()
				pass

	def publish(self, message):
		if self.publish_channel is not None:
			seriealizedMsg = message.serialize()
			if self.debug_flag == 2:
				utils.log(self.name, 'publish message: ', seriealizedMsg)
			self.bus.publish(self.publish_channel, seriealizedMsg)
		else:
			print("Publish Channel is None")

	def getMessage(self):
		message = None
		while True:
			message = self.bus.getMessage()

			if message is not None:
				break	
			time.sleep(self.sleep_time)
			
		if self.debug_flag == 2:
			utils.log(self.name, 'receive message: ', message)

		return Message(message)
