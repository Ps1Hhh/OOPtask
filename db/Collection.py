

# Коллекция, реализует удобную загрузку-сохранение для списка документов.
class Collection():
    def __init__(self, provider, itemClass, itemsRaw=[]):
        self._provider = provider
        self._itemClass = itemClass
        self._name = itemClass.__name__
        items = list(self._itemClass(collection=self, raw=item) for item in itemsRaw)
        self._items = dict(map((lambda item: (item.getId(), item)), items))
    def getItemClass(self): return self._itemClass
    def getName(self): return self._name
    def getProvider(self): return self._provider
    # List methods
    def map(self, fn): return map(fn, self._items.values())
    def find(self, fn): return next(x for x in self._items.values() if fn(x))
    def filter(self, fn): return [x for x in self._items.values() if fn(x)]
    def getIdList(self): return list(self._items.keys())
    def findById(self, id): return self._items.get(id, None)
    def removeById(self, id): return self._items.pop(id, None)
    def append(self, item):
        item.setCollection(self)
        self._items[item.getId()] = item
        return item
    def clear(self): self._items.clear()
    # Additional methods
    def __eq__(self, other): return self._name == other._name
    def getDictsList(self): return list(dict(i) for i in self._items.values())
    def __str__(self):
        s = self.getName()+':\n'
        for i in self._items.values():
            s += '{'+str(i)+'},\n'
        s = s[:-1]
        if len(self._items):
            s = s[:-1]
        return s
