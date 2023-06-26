# Функции built-in
""" help(int) - помощь по функции
print(), input(), str(), float(), int(), round(),
range(), reversed(), len(), list(), dict()
"""


def say_hello(name='bro'):
    print('Hello,', name)


def greeting(cur_hour):
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


print(greeting(19))
