# Регулярные выражения (Regular Expressions)
# Поиск по паттерну (pattern)
# Квантификаторы (quantifiers)
# Способ указать о каком количестве идёт речь
# {m} - ровно m раз
# {m,} - m и более раз;
# {,n} - не более, чем n раз
# {m,n} - от m до n раз
import re

pattern = 'o{3,5}'  # От 2 до 5 (пишем без пробела)
testString = 'Google, Gooogle, Goooogle'

# поскольку результатов может быть много, то используем findall
result = re.findall(pattern, testString)


print(result)
