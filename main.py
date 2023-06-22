string = input('Введите пять целых чисел через пробел: ')

# 1. классический способ
lst = string.split()
a = []
for x in lst:
    a.append(int(x))

print('Сумма чисел:', sum(a))

# 2. списочным выражением
a = [int(x) for x in string.split()]
print('Сумма чисел:', sum(a))
