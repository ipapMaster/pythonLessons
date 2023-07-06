# Исключения (Exception) Run-Time

n = input('Введите целое число: ')

try:
    m = int(n)
    res = m + 'пример невозможной конкатенации'
except ValueError:
    print(f'Вас просили ввести целое число, а Вы ввели "{n}".')
except Exception as exp:
    print('Имя исключения:', exp.__class__.__name__)
    print('Что не так:', exp)
else:
    print('Результат:', m / 2)
