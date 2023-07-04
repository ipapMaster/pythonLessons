# Исключения (Exception) Run-Time
a, b = 10, 2
z = [1, 2]

try:  # попытка операции
    print(a / b)
    z[2] = a * b
except IndexError:  # ошибка индекса
    print('Неправильный индекс', z[-1])
except ZeroDivisionError:  # деление на ноль
    print('Деление на ноль', a / a)
finally:  # выполнится в любом случае
    print('Z =', z[1])
