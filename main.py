import os

fname = 'info.txt'
text = ''

f = open(fname, 'rt', encoding='utf-8')

temp = f.readline()
while temp != '':
    if temp[0] != '.':
        text += temp
    temp = f.readline()

f.close()

print(text)



