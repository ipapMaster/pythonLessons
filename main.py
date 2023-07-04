import os

fname = 'info.txt'
text = ''

if os.path.isfile(fname):
    with open(fname, 'rt', encoding='utf-8') as f:
        text = f.read()  # читаем строку целиком
        # другие операции с открытым файлом

# f.close() в этом случае уже не нужно

if text:
    res = text.splitlines()  # строковый метод, разбивающий строку на элементы списка по \n

print(res)
