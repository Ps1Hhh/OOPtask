from db.Document import Document
from .User import User
from .Route import Route


class Voucher(Document):
    _propsToSave = ['_id', '_routeID', '_userID', '_departureDate', '_count']
    def __init__(self, route=None, user=None, departureDate='', count=0.0, id='', collection=None, raw={}):
        if route:
            self.setRoute(route)
        if user:
            self.setUser(user)
        self.setDepartureDate(departureDate)
        self.setCount(count)
        super().__init__(id, collection, raw)
    def getRouteID(self): return self._routeID
    def getUserID(self): return self._userID
    def getDepartureDate(self): return self._departureDate
    def getCount(self): return self._count
    def getUser(self):
        user = self._provider.findItem('User', self._userID)
        if isinstance(user, User):
            return user
        return None
    def getRoute(self):
        route = self._provider.findItem('Route', self._routeID)
        if isinstance(route, Route):
            return route
        return None
    def getDiscount(self): return 5 if self._count > 1 else 0
    def getCost(self):
        route = self.getRoute()
        if not route:
            raise TypeError('Bad RouteID')
        hotel = route.getHotel()
        if not hotel:
            raise TypeError('Bad HotelID')
        fullCost = hotel.getCost() * self.getCount()
        discount = self.getDiscount()
        return fullCost * (100 - discount) / 100 if discount else fullCost
    def setRoute(self, route): self._routeID = route.getId()
    def setUser(self, user): self._userID = user.getId()
    def setDepartureDate(self, departureDate): self._departureDate = departureDate
    def setCount(self, count): self._count = count
