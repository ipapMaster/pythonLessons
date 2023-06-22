# Словари - dictionary
d = dict()  # пустой словарь
string = 'Изучение языка Python'
# удаление всех пробелов
naked_string = ''.join(string.split())

# перебираем строку по буквам
for ch in naked_string:
    if ch in d:  # если ключ (буква) в словаре есть
        d[ch] += 1  # увеличиваем значение на 1
    else:  # если ключа (буквы) в словаре нет
        d[ch] = 1  # то создаём ключ и задаём ему значение - 1

print('Частотный анализ строки', '"' + string + '":')
for k, v in d.items():
    print(k, '-', v)
