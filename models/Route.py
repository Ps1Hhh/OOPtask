from db.Document import Document
from .Hotel import Hotel


class Route(Document):
    _propsToSave = ['_id', '_name', '_duration', '_hotelID', '_climate']
    def __init__(self, name='', duration=0.0, climate='', hotel=None, id='', collection=None, raw={}):
        self.setName(name)
        if hotel:
            self.setHotel(hotel)
        self.setClimate(climate)
        self.setDuration(duration)
        super().__init__(id, collection, raw)
    def getDuration(self): return self._duration
    def getHotelID(self): return self._hotelID
    def getClimate(self): return self._climate
    def getHotel(self):
        hotel = self._provider.findItem('Hotel', self._hotelID)
        if isinstance(hotel, Hotel):
            return hotel
        return None
    def setName(self, name): self._name = name
    def setDuration(self, duration): self._duration = duration
    def setClimate(self, climate): self._climate = climate
    def setHotel(self, hotel): self._hotelID = hotel.getId()