phone = '+7-012-345-67-89'

print('Исходный вариант номера', phone)
# заменить все дефисы на пробел
spaced_phone = phone.replace('-', ' ')
print('С заменой дефисов на пробелы:', spaced_phone)
# первая замена с сохранением во временной переменной
temp = phone.replace('-', ' (', 1)
bracked_code = temp.replace('-', ') ', 1)
print('Код в скобках', bracked_code)
