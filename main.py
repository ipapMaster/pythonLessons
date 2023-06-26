c = 3


def multiply(num):
    global c  # получаем доступ к глобальной переменной
    c *= num
    print(c)


multiply(5)
print(c)
