# Регулярные выражения (Regular Expressions)
# Поиск по паттерну (pattern)
import re

pattern = '20'
testString = '20 плюс 10 = 30'

# метод match ищет совпадение только в начале строки
result = re.match(pattern, testString)

# span - индекс начали и конца найденной подстроки
# match - собственно найденная подстрока

print(result)
