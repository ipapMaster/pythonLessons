import os

fname = 'info.txt'
text = ''

if os.path.isfile(fname):
    f = open(fname, 'rt', encoding='utf-8')  # открыт на чтение (текстовый файл)
    text = f.read(6)  # курсор файла остановится на 6-й позиции
    f.read(5)
    text += f.read(9)
    f.close()
else:
    print('Файл не существует!')

print(f'Из файла прочитано {len(text)} байт.')
if text:
    print(f'Вот этот текст: {text}')
