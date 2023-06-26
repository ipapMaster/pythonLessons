# Функции built-in
""" help(int) - помощь по функции
print(), input(), str(), float(), int(), round(),
range(), reversed(), len(), list(), dict()
"""


def say_hello(name='bro'):
    print('Hello,', name)


def summ(a, b):
    c = a + b  # локальные переменные
    # a = int(input('Введите первое слагаемое: '))
    # b = int(input('Введите второе слагаемое: '))
    # print('Сумма', a, '+', b, '=', c)
    if a < 0 or b < 0:
        return -1000
    # else после return - излишний оператор
    return c


x, y = 1, 3  # глобальные переменные
res = summ(x - 8, y - 10)
if res == -1000:
    print('Согласно задаче, в функцию нельзя передавать отрицательные значения.')
else:
    print('Сумма', x + 1, '+', y + 1, '=', res)

print(x, y)
# say_hello()
# say_hello('Bill')
