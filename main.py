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
        int_part = int(result)
        fraction_part = result - int_part
        if fraction_part == 0.0:
            print(int(result))
        else:
            print(round(result, 2))  # первый способ
            print(f'{result:.2f}')  # второй способ
        break
