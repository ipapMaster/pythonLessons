# Исключения (Exception) Run-Time

a = [1, 2, 3, 4, 5]

try:
    print(a[-7])
except IndexError:
    print(a[-1])
