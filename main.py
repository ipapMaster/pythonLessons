# Дан код без обработки исключений

while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    if a.isdigit() and b.isdigit():  # Строки a и b – числа?
        if int(b) == 0:  # если второе число равно нулю
            print('На ноль делить нельзя!')
        else:
            print(int(a) / int(b))
            break
    else:
        print('Необходимо вводить только числа.')
