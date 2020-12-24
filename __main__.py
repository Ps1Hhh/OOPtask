from db.Provider import Provider
from db.JSONProvider import JSONProvider
from db.SQLiteProvider import SQLiteProvider
from models.User import User
from models.Hotel import Hotel
from models.Route import Route
from models.Voucher import Voucher

def main1():
    print('main1')
    provider = Provider()
    u1 = User('Иванович', 'Иван', 'Иванов', 'г. Москва, ул. Ленина, д 123, кв 10', '9169761398', '1')
    u2 = User('Поручникова', 'Юлия', 'Владимировна', 'г. Санкт-Петербург, ул. Маркса, д 24, кв 30', '9057525924', '2')
    u3 = User('Жирнов', 'Евгений', 'Борисович', 'г. Томск, ул. Октябрьская, д 7, кв 17', '9169284356', '3')
    provider.appendItem('User', u1)
    provider.appendItem('User', u2)
    provider.appendItem('User', u3)
    h1 = Hotel('Сокол', 6300, 'Россия, Крым', '4')
    h2 = Hotel('Саванна', 7000, 'США, Джорджия', '5')
    h3 = Hotel('Джунгли', 5600, 'Индия, Нью-Дели', '6')
    provider.appendItem('Hotel', h1)
    provider.appendItem('Hotel', h2)
    provider.appendItem('Hotel', h3)
    r1 = Route('Жаркий Крым', 2, 'Умеренно-континентальный', h1, '7')
    r2 = Route('Дикая Саванна', 4, 'Субэкваториальный', h2, '8')
    r3 = Route('Индийские джунгли', 1, 'Субтропический', h3, '9')
    r4 = Route('Русское Чёрное море', 4, 'Умеренно-континентальный', h1, '10')
    provider.appendItem('Route', r1)
    provider.appendItem('Route', r2)
    provider.appendItem('Route', r3)
    provider.appendItem('Route', r4)
    w1 = Voucher(r4, u1, '20.06.2019', 3, '11')
    w2 = Voucher(r2, u3, '03.10.2019', 1, '12')
    w3 = Voucher(r3, u3, '10.04.2019', 2, '13')
    provider.appendItem('Voucher', w1)
    provider.appendItem('Voucher', w2)
    provider.appendItem('Voucher', w3)
    # Вывод эл-тов из всех коллекций
    print(provider)
    # Проверка рассчёта суммы для путёвки
    print(w1.getCost() == 17955.0)
    print(w2.getCost() == 7000)
    print(w3.getCost() == 10640.0)
    w1 = provider.findItem('Voucher', w1.getId())
    w2 = provider.findItem('Voucher', w2.getId())
    w3 = provider.findItem('Voucher', w3.getId())
    # Вывод эл-тов из всех коллекций
    print(provider)
    # Проверка рассчёта суммы для путёвки
    print(w1.getCost() == 17955.0)
    print(w2.getCost() == 7000)
    print(w3.getCost() == 10640.0)
    provider.removeItem('Voucher', w3.getId())
    provider.removeItem('Route', r3.getId())
    provider.removeItem('User', u3.getId())
    # Вывод эл-тов из всех коллекций
    print(provider)

def main2():
    print('main2')
    jsonP = JSONProvider('', 'test.json')
    u1 = User('Иванович', 'Иван', 'Иванов', 'г. Москва, ул. Ленина, д 123, кв 10', '9169761398', '1')
    u2 = User('Поручникова', 'Юлия', 'Владимировна', 'г. Санкт-Петербург, ул. Маркса, д 24, кв 30', '9057525924', '2')
    u3 = User('Жирнов', 'Евгений', 'Борисович', 'г. Томск, ул. Октябрьская, д 7, кв 17', '9169284356', '3')
    jsonP.appendItem('User', u1)
    jsonP.appendItem('User', u2)
    jsonP.appendItem('User', u3)
    h1 = Hotel('Сокол', 6300, 'Россия, Крым', '4')
    h2 = Hotel('Саванна', 7000, 'США, Джорджия', '5')
    h3 = Hotel('Джунгли', 5600, 'Индия, Нью-Дели', '6')
    jsonP.appendItem('Hotel', h1)
    jsonP.appendItem('Hotel', h2)
    jsonP.appendItem('Hotel', h3)
    r1 = Route('Жаркий Крым', 2, 'Умеренно-континентальный', h1, '7')
    r2 = Route('Дикая Саванна', 4, 'Субэкваториальный', h2, '8')
    r3 = Route('Индийские джунгли', 1, 'Субтропический', h3, '9')
    r4 = Route('Русское Чёрное море', 4, 'Умеренно-континентальный', h1, '10')
    jsonP.appendItem('Route', r1)
    jsonP.appendItem('Route', r2)
    jsonP.appendItem('Route', r3)
    jsonP.appendItem('Route', r4)
    w1 = Voucher(r4, u1, '20.06.2019', 3, '11')
    w2 = Voucher(r2, u3, '03.10.2019', 1, '12')
    w3 = Voucher(r3, u3, '10.04.2019', 2, '13')
    jsonP.appendItem('Voucher', w1)
    jsonP.appendItem('Voucher', w2)
    jsonP.appendItem('Voucher', w3)
    #Вывод эл-тов из всех коллекций
    print(jsonP)
    # Проверка рассчёта суммы для путёвки
    print(w1.getCost() == 17955.0)
    print(w2.getCost() == 7000)
    print(w3.getCost() == 10640.0)
    # Сохранение в json-файл
    jsonP.save()
    # Пересоздание JSON провайдера
    del jsonP
    jsonP = JSONProvider('test.json', 'test.json')
    # Загрузка эл-тов коллекций из файла
    jsonP.load()
    w1 = jsonP.findItem('Voucher', w1.getId())
    w2 = jsonP.findItem('Voucher', w2.getId())
    w3 = jsonP.findItem('Voucher', w3.getId())
    # Вывод эл-тов из всех коллекций
    print(jsonP)
    # Проверка рассчёта суммы для путёвки
    print(w1.getCost() == 17955.0)
    print(w2.getCost() == 7000)
    print(w3.getCost() == 10640.0)
    jsonP.removeItem('Voucher', w3.getId())
    jsonP.removeItem('Route', r3.getId())
    jsonP.removeItem('User', u3.getId())
    # Вывод эл-тов из всех коллекций
    print(jsonP)
    # Сохранение в json-файл
    jsonP.save()


def main3():
    print('main3')
    sqlP = SQLiteProvider('db.sqlite3')
    u1 = User('Иванович', 'Иван', 'Иванов', 'г. Москва, ул. Ленина, д 123, кв 10', '9169761398', '1')
    u2 = User('Поручникова', 'Юлия', 'Владимировна', 'г. Санкт-Петербург, ул. Маркса, д 24, кв 30', '9057525924', '2')
    u3 = User('Жирнов', 'Евгений', 'Борисович', 'г. Томск, ул. Октябрьская, д 7, кв 17', '9169284356', '3')
    sqlP.appendItem('User', u1)
    sqlP.appendItem('User', u2)
    sqlP.appendItem('User', u3)
    h1 = Hotel('Сокол', 6300, 'Россия, Крым', '4')
    h2 = Hotel('Саванна', 7000, 'США, Джорджия', '5')
    h3 = Hotel('Джунгли', 5600, 'Индия, Нью-Дели', '6')
    sqlP.appendItem('Hotel', h1)
    sqlP.appendItem('Hotel', h2)
    sqlP.appendItem('Hotel', h3)
    r1 = Route('Жаркий Крым', 2, 'Умеренно-континентальный', h1, '7')
    r2 = Route('Дикая Саванна', 4, 'Субэкваториальный', h2, '8')
    r3 = Route('Индийские джунгли', 1, 'Субтропический', h3, '9')
    r4 = Route('Русское Чёрное море', 4, 'Умеренно-континентальный', h1, '10')
    sqlP.appendItem('Route', r1)
    sqlP.appendItem('Route', r2)
    sqlP.appendItem('Route', r3)
    sqlP.appendItem('Route', r4)
    w1 = Voucher(r4, u1, '20.06.2019', 3, '11')
    w2 = Voucher(r2, u3, '03.10.2019', 1, '12')
    w3 = Voucher(r3, u3, '10.04.2019', 2, '13')
    sqlP.appendItem('Voucher', w1)
    sqlP.appendItem('Voucher', w2)
    sqlP.appendItem('Voucher', w3)
    # Вывод эл-тов из всех коллекций
    print(sqlP)
    # Проверка рассчёта суммы для путёвки
    print(w1.getCost() == 17955.0)
    print(w2.getCost() == 7000)
    print(w3.getCost() == 10640.0)
    # Применение всех изменений в БД (commit)
    sqlP.save()
    # Пересоздание провайдера SQL
    del sqlP
    sqlP = SQLiteProvider('db.sqlite3')
    # Загрузка всех таблиц из БД в коллекции
    sqlP.load()
    w1 = sqlP.findItem('Voucher', w1.getId())
    w2 = sqlP.findItem('Voucher', w2.getId())
    w3 = sqlP.findItem('Voucher', w3.getId())
    # Вывод эл-тов из всех коллекций
    print(sqlP)
    # Проверка рассчёта суммы для путёвки
    print(w1.getCost() == 17955.0)
    print(w2.getCost() == 7000)
    print(w3.getCost() == 10640.0)
    sqlP.removeItem('Voucher', w3.getId())
    sqlP.removeItem('Route', r3.getId())
    sqlP.removeItem('User', u3.getId())
    # Вывод эл-тов из всех коллекций
    print(sqlP)
    # Применение всех изменений в БД (commit)
    sqlP.save()

main1()
main2()
main3()