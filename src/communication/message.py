import json

class Message:

	def __init__(self, rawData = None):
		if rawData:
			self.dictData = json.loads(rawData)
		else:
			self.dictData = {}

	def get(self, key):
		return self.dictData[key]

	def set(self, key, value):
		self.dictData[key] = value

	def serialize(self):
		return json.dumps(self.dictData)