# Словари - dictionary
# d = dict() - пустой словарь

d = {
    'Иванов': 'Монтажник',
    'Петров': 'Менеджер',
    'Сидоров': 'Бухгалтер',
}

# добавим нового работника
d['Фёдоров'] = 'Сварщик'

# создадим список всех фамилий
surname_list = list(d.keys())
# создадим список всех должностей
position_list = list(d.values())
print(sorted(surname_list))
print(position_list)
# распечатка с помощью метода items
for k, v in d.items():
    print(k, '->', v)
