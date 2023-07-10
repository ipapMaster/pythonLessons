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

# "Вытащить" URL из текста (как http, так и https)
pattern = r'http(?:s)?://[\S]+'
testString = '<p>Информация здесь: https://google.com и ...</p>'

# поскольку результатов может быть много, то используем findall
result = re.findall(pattern, testString)

print(result[0])
