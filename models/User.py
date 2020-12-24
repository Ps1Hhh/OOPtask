from db.Document import Document


class User(Document):
    _propsToSave = ['_id', '_secname', '_firstname', '_patronym', '_adress', '_phone']
    def __init__(self, secname='', firstname='', patronym='', adress='', phone='', id='', collection=None, raw={}):
        self.setSecname(secname)
        self.setFirstname(firstname)
        self.setPatronym(patronym)
        self.setAdress(adress)
        self.setPhone(phone)
        super().__init__(id, collection, raw)
    def getSecname(self): return self._secname
    def getFirstname(self): return self._firstname
    def getPatronym(self): return self._patronym
    def getAdress(self): return self._adress
    def getPhone(self): return self._phone
    def setSecname(self, secname): self._secname = secname
    def setFirstname(self, firstname): self._firstname = firstname
    def setPatronym(self, patronym): self._patronym = patronym
    def setAdress(self, adress): self._adress = adress
    def setPhone(self, phone): self._phone = phone
