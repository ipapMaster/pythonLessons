string = 'город Рим'  # город Миргород

temp = string.lower().split() ['город', 'рим']
str1 = temp[1][::-1].capitalize()  # Мир

res = f'{temp[0]} {str1}{temp[0]}'

print(res)
