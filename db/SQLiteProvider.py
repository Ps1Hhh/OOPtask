from .Collection import Collection
from .Provider import Provider
import sqlite3

# Провайдер для сохранения и загрузки в файл SQLite3
class SQLiteProvider(Provider):
    def __init__(self, dbFile):
        super().__init__()
        self._connection = sqlite3.connect(dbFile)
        self._cursor = self._connection.cursor()
    def removeItem(self, collectionName, itemId):
        item = super().removeItem(collectionName, itemId)
        if item:
            self.__remove_row(collectionName, itemId)
        return item
    def save(self):
        for colName in self._collections:
            for item in self._collections[colName].getDictsList():
                self.__post_row(colName, dict(item))
        self._connection.commit()
    def load(self):
        for collName in self._collections:
            rawItems = self.__get_table(collName)
            self._collections[collName] = Collection(self, self.getModel(collName), rawItems)
    def __get_table(self, tablename):
        # Получение всех док-тов из таблицы БД
        sqlite_select_query = 'SELECT * FROM '+tablename
        self._cursor.execute(sqlite_select_query)
        records = self._cursor.fetchall()
        itemClass = self._collections[tablename].getItemClass()
        return [dict(zip(itemClass._propsToSave, d)) for d in records]
    def __post_row(self, tablename, itemDict):
        # Запись одного док-та в таблицу БД
        keys = ','.join(itemDict.keys())
        question_marks = ','.join(list('?'*len(itemDict)))
        values = tuple(itemDict.values())
        sql_post_query = 'INSERT OR REPLACE INTO '+tablename+' ('+keys+') VALUES ('+question_marks+')'
        self._connection.execute(sql_post_query, values)
    def __remove_row(self, tablename, id):
        # Удаление дного док-та в теблице БД
        sql_remove_query = 'DELETE FROM '+tablename+' WHERE _id = \''+id+'\''
        self._cursor.execute(sql_remove_query)
