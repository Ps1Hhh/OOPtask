from db.Document import Document


class Hotel(Document):
    _propsToSave = ['_id', '_name', '_cost', '_country']

    def __init__(self, name='', cost=0.0, country='', id='', collection=None, raw={}):
        self.setName(name)
        self.setCost(cost)
        self.setCountry(country)
        super().__init__(id, collection, raw)
    def getName(self): return self._name
    def getCost(self): return self._cost
    def getCountry(self): return self._country
    def setName(self, name): self._name = name
    def setCost(self, cost): self._cost = cost
    def setCountry(self, country): self._country = country