string = 'Видеть, вертеть, смотреть.'

# получили число вхождений подстроки "еть"
count = string.count('еть')
print(count)  # и выведем его

counter = 0  # счётчик проходов по строке
indexes = []  # тут будем хранить индексы вхождений
index = 0  # откуда ищем (с какого индекса)

while counter < count:
    if counter == 0: # для первого прохода идём с нуля
        index = string.find('еть', index)
    else:
        index = string.find('еть', index + 1)
    indexes.append(index)
    counter += 1

print(*indexes)
