from random import randint, shuffle

p_length = 12

symbols = 'qwertyuiopasdfghjklzxcvbnm'
symbols_caps = symbols.upper()
numbers = '1234567890'
special = '@#^'
total = symbols + symbols_caps + numbers + special
total_list = list(total)
shuffle(total_list)

length = len(total_list)

start = randint(0, length - p_length)

pwd = total_list[start:start + p_length]

print(*pwd, sep='')
