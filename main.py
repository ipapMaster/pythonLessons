# Регулярные выражения (Regular Expressions)
# Поиск по паттерну (pattern)
import re

pattern = r'начало!\Z'  # Заканчивается на "начало!"
testString = 'Главное - начало!'

# метод search ищет первое совпадение
result = re.search(pattern, testString)

# расшифруем метасимволы
# \ - в паттерне указывает на начало последовательности
# \Z - заканчивается на...

try:
    print(f'Нашлось: {result[0]}.')
except TypeError:
    print(f'Ничего не найдено.')

