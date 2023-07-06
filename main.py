# "Бросание" исключения (raise exception)

min_val = 1
max_val = 10

string = input(f'Введите целое число от {min_val} до {max_val}: ')
try:
    cur_val = int(string)
    if not min_val <= cur_val <= max_val:
        raise ValueError(f'введённое число вне заданного диапазона:'
                         f' от {min_val} до {max_val}.')
except ValueError as exp:
    print('Произошло следующее:', exp.__class__.__name__)
    print('Будьте внимательнее:', exp)
else:
    print('Успешный ввод.')
