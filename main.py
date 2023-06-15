import math

r = float(input('Введите радиус окружности: '))

L = 2 * math.pi * r  # длина окружности
S = math.pi * r ** 2  # площадь круга

print('Длина окружности:', round(L, 2))
print('Площадь круга:', round(S, 2))
