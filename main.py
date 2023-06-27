string = 'Видеть, вертеть, смотреть.'
# find('что ищем', start, stop)
index = string.find('еть')
print(index)

index = string.find('еть', 7)
print(index)

index = string.find('еть', 15, 20)
print(index)