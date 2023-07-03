import os

fname = 'info.txt'
text = ''

files = os.listdir()

f = open(fname, 'wt')
for file in files:
    print(file, file=f)
f.close()



