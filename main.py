# Словари - dictionary
# d = dict() - пустой словарь

d = {
    'Иванов': 'Монтажник',
    'Петров': 'Менеджер',
    'Сидоров': 'Бухгалтер',
}

print(d['Петров'])  # обращение по ключу

# добавим нового работника
d['Фёдоров'] = 'Сварщик'

print(d)  # распечатали весь словарь (как есть)
