# PEP 249 (Python Database API Specification)
# СУБД - Система Управления Базами Данных
import sqlite3

# Подключаемся к базе данных (БД)
connection = sqlite3.connect('films.sqlite')

# создаём курсор
cursor = connection.cursor()

# Вычисляем максимальный ID
id_max = cursor.execute("SELECT MAX(id) from genres").fetchone()[0]
id_max += 1

# создаём запрос
# INSERT INTO <table>(название полей) VALUES(значения в том же порядке)
query = f"""
INSERT INTO genres VALUES(28, 'Наука'), (29, 'Техника')
"""

# выполнение запроса на добавление
cursor.execute(query)

# подтверждение запроса на запись (изменение БД)
connection.commit()

# Отключаемся от БД
connection.close()
