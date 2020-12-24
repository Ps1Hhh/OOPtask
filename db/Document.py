import uuid

# Документ - базовый класс для эл-тов коллекций.
# Реализует быструю систему id, сохранения-загрузки и вывода.
class Document:
    _propsToSave = ['_id']  # Свойства, которые подлежат сохранению и загрузке
    def __init__(self, id='', collection=None, raw={}):
        if collection:
            self.setCollection(collection)
        if '_id' in raw:
            self._id = str(raw['_id'])
        elif id:
            self._id = str(id)
        else:
            self._id = Document.__generateId()
        # Загрузка значений свойств документа из словаря
        for key in self.__class__._propsToSave:
            if key in raw:
                setattr(self, key, raw[key])
    def getId(self): return self._id
    def getCollection(self): return self._collection  # Ссылка на коллекцию-владелец
    def setCollection(self, collection):
        self._collection = collection  # Ссылка на коллекцию-владелец
        self._provider = collection.getProvider()  # Ссылка на провайдер
    def __eq__(self, other): return self._id == other._id
    def __hash__(self): return self._id
    def __iter__(self):
        # Получение значений сохраняемых свойств документа
        for key in self.__class__._propsToSave:
            yield (key, getattr(self, key))
    def __str__(self):
        s = ''
        for key in self.__class__._propsToSave:
            s += '{0}: {1}, '.format(key, getattr(self, key))
        return s[:-2]
    @staticmethod
    def __generateId():
        # Генерация id в строковом формате
        return uuid.uuid1().hex
