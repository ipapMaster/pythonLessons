s = 'весна пришла'  # надо сделать "пришла весна"

lst = s.split()  # "расщепили" строку по пробелу (default)
print('До', lst)
# меняем нулевой и первый элемент списка
lst.reverse()

print('После', lst)
print(*lst)  # теперь в виде строки
