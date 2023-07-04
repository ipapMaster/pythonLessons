import os

fname = 'info.txt'
text = ''

if os.path.isfile(fname):
    f = open(fname, 'rt', encoding='utf-8')
    text = f.read()  # читаем строку целиком
    f.close()

if text:
    res = text.splitlines()  # строковый метод, разбивающий строку на элементы списка по \n

print(res)
