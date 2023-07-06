# Исключения (Exception) Run-Time

n = input('Введите целое число: ')

try:
    m = int(n)
except Exception as exp:
    print('Исключение:', exp.__class__.__name__)
    print(f'Вас просили ввести целое число, а Вы ввели "{n}".')
else:
    print('Результат:', m / 2)
