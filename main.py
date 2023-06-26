# Функции built-in
""" help(int) - помощь по функции
print(), input(), str(), float(), int(), round(),
range(), reversed(), len(), list(), dict()
"""


def say_hello(name='bro'):
    print('Hello,', name)


def greeting(cur_hour=0):
    if 6 <= cur_hour < 12:
        return 'Доброе утро'
    if 12 <= cur_hour < 18:
        return 'Добрый день'
    if 18 <= cur_hour < 23:
        return 'Добрый вечер'
    return 'Доброй ночи'


def summ(a, b):
    c = a + b  # локальные переменные
    # a = int(input('Введите первое слагаемое: '))
    # b = int(input('Введите второе слагаемое: '))
    # print('Сумма', a, '+', b, '=', c)
    if a < 0 or b < 0:
        return -1000
    # else после return - излишний оператор
    return c


def sqeq(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return 'Нет корней'
    if d == 0:
        return -b / 2 * a
    return (-b - d ** 0.5) / 2 * a, (-b + d ** 0.5) / 2 * a


res = sqeq(4, -4, 4)

if isinstance(res, tuple):
    x1, x2 = res
    print(round(x1, 2), round(x2, 2), sep='; ')
elif isinstance(res, float):
    print(round(res, 2))
else:
    print(res)
