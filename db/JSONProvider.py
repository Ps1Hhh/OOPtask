from .Provider import Provider
from .Collection import Collection
import json


# Провайдер для сохранения и загрузки в разные, или один файл JSON
class JSONProvider(Provider):
    def __init__(self, readFile: str, writeFile: str = ''):
        self._readFile = readFile
        self._writeFile = writeFile
        if not writeFile:
            self._writeFile = readFile
        super().__init__()
    def load(self):
        # Поддержка кириллицы
        f = open(self._readFile, 'r', encoding='utf-8')
        raw = json.load(f)
        f.close()
        collections = self._collections
        for collName in raw:
            collections[collName] = Collection(self, self.getModel(collName), raw[collName])
        self._collections = collections
    def save(self):
        resJson = dict((collName, coll.getDictsList()) for collName, coll in self._collections.items())
        # Поддержка кириллицы
        f = open(self._writeFile, 'w', encoding='utf-8')
        json.dump(resJson, f, sort_keys=True, indent=4, ensure_ascii=False)
        f.close()
