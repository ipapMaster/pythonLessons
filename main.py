import os

fname = 'info.txt'
text = ''

f = open(fname, 'rt', encoding='utf-8')

lst = f.readlines()

f.close()

res = list(map(lambda x: x.rstrip('\n'), lst))

print(res)
