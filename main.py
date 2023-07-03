# import os
# if os.path.isfile(file)

fname = 'info.txt'

f = open(fname, 'at', encoding='utf-8')  # открыт на запись (текстовый файл)
# для дозаписи используется a - append
if f.encoding == 'utf-8':
    print('Всё верно')
else:
    print('Будьте осторожны с читабельностью')
    print(f.encoding)
f.write('Привет')
f.close()
