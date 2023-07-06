# Регулярные выражения (Regular Expressions)
# Поиск по паттерну (pattern)
import re

pattern = r'\d{3}'  # Три цифры идущие подряд
testString = 'При пожаре звонить 112.'

# метод search ищет первое совпадение
result = re.search(pattern, testString)

# расшифруем метасимволы
# \ - в паттерне указывает на начало последовательности
# \d - цифра от 0 до 9

try:
    print(f'Нашлось: {result[0]}.')
except TypeError:
    print(f'Ничего не найдено.')

