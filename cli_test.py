import sys

length = len(sys.argv)

if length > 1:
    print(f'Первый аргумент {sys.argv[1]}')
    print(f'Последний аргумент {sys.argv[-1]}')
else:
    print('Скрипт запущен без аргументов')
