# Регулярные выражения (Regular Expressions)
# Поиск по паттерну (pattern)
# Квантификаторы (quantifiers)
# Способ указать о каком количестве идёт речь
# {m} - ровно m раз
# {m,} - m и более раз;
# {,n} - не более, чем n раз
# {m,n} - от m до n раз
# ? - аналог {0,1}
# * - от 0 до бесконечности {0,}
# + - аналог {1,}
import re

# Выбор только bold
pattern = '<p[^>]*>(.*?)</p>'
testString = '<b>Начало</b><p align="center">Вот основной текст</p>, <i>и далее</i>'

# поскольку результатов может быть много, то используем findall
result = re.findall(pattern, testString)

print(result[0])
