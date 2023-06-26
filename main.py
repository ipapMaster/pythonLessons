def summ(*args):
    res = 0
    for i in args:
        res += i
    return res, len(args)


print(summ(1, 2, 3, 4, 5, 6))
