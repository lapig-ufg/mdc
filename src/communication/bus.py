import redis

class Bus:

	def __init__(self, config):
		self.connection = redis.StrictRedis(host=config['host'], port=config['port'], db=config['db'])
		self.channel = None

	def subscribe(self, channel):
		self.channel = channel

	def publishMessage(self, channel, message):
		self.publish(channel, message.serialize())

	def publish(self, channel, data):
		self.connection.rpush(channel, data)

	def getMessage(self):
		return self.connection.lpop(self.channel)