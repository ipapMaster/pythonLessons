# Исключения (Exception) Run-Time

fname = 'temp.txt'

try:
    with open(fname, encoding='utf-8') as f:
        t = f.read()
        print(t)
except FileNotFoundError:
    with open(fname, 'w', encoding='utf-8') as f:
        f.write('Файл отсутствовал и был создан.')
