while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    try:
        result = int(a) / int(b)  # попытка деления
    except ValueError as exp:  # некорректный ввод
        print('Одно из чисел введено некорректно!')
        print(exp)
    except ZeroDivisionError:  # деление на ноль
        print('На ноль делить нельзя!')
    else:
        print(result)
        break
