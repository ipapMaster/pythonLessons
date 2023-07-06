# Регулярные выражения (Regular Expressions)
# Поиск по паттерну (pattern)
import re

pattern = r'\d{3}'  # есть ли в строке 3 цифры от 0 до 9, идущие подряд.
testString = 'При пожаре звонить - 112.'

# метод search ищет первое совпадение
result = re.search(pattern, testString)

# расшифруем метасимвол
# \ - в паттерне указывает на начало последовательности
# \d - целое число

try:
    print(f'Нашлось: {result[0]}.')
except TypeError:
    print('Ничего не найдено.')

