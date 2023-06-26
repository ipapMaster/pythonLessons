a = [i for i in range(1, 11)]

# def twice(a):
#     return a ** 2
# lambda <аргументы>: <выражение>
b = map(lambda x: x ** 2, a)

print(list(b))
