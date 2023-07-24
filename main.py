# PEP 249 (Python Database API Specification)
# СУБД - Система Управления Базами Данных
import sqlite3

# Подключаемся к базе данных (БД)
connection = sqlite3.connect('films.sqlite')

# создаём курсор
cursor = connection.cursor()

# создаём запрос
# UPDATE <table> SET <имя поля> = NEW VALUE WHERE <условие>
query = f"""
UPDATE genres SET title = 'Жизнь'
WHERE id = 29
"""

# выполнение запроса на добавление
cursor.execute(query)

# подтверждение запроса на запись (изменение БД)
connection.commit()

# Отключаемся от БД
connection.close()
