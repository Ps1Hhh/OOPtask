from models import models
from .Collection import Collection

# Провайдер - базовый класс для новых провайдеров.
# Реализует работу, загрузку и сохранение коллекций и док-ов в них.
class Provider():
    def __init__(self):
        self._models = models
        self._collections = {}
        for model in models: self._collections[model.__name__] = Collection(self, model)
    def getModels(self): return self._models
    def getModel(self, modelName): return next(m for m in self.getModels() if m.__name__ == modelName)
    def getCollection(self, name): return self._collections.get(name)
    def findItem(self, collectionName, itemId):
        coll = self._collections.get(collectionName)
        if (coll):
            return coll.findById(itemId)
        return None
    def appendItem(self, collectionName, item):
        coll = self._collections.get(collectionName)
        if (coll):
            return coll.append(item)
        return None
    def removeItem(self, collectionName, itemId):
        coll = self._collections.get(collectionName)
        if (coll):
            return coll.removeById(itemId)
        return None
    def __str__(self):
        s = ''
        for coll in self._collections.values():
            s += str(coll)+'\n'
        return s
    def load(self): pass
    def save(self): pass
