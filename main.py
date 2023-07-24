# PEP 249 (Python Database API Specification)
# СУБД - Система Управления Базами Данных
import sqlite3

# Подключаемся к базе данных (БД)
connection = sqlite3.connect('films.sqlite')

# создаём курсор
cursor = connection.cursor()

# создаём запрос
# query =

# выполнение запроса
result = cursor.execute("""SELECT title FROM films
WHERE year > ? """, (2010, )).fetchmany(5)

for item in result:
    print(item[0])

# Отключаемся от БД
connection.close()
