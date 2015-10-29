import json
from _datasource import Datasource

class Modis(Datasource):

    def __init__(self, config):
      Datasource.__init__(self, config)

      jsonProducts = json.load(open(self.path_products))
      self.product = jsonProducts[self.productName]
      
      self.temporalResolution = self.product['temporalResolution']
      self.productStart = self.product['start']
      self.productEnd = self.product['end']