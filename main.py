# f-строка

name = 'Виктор'  # в слове 6 символов
age = 9  # однозначное число
height = 141.457  # 5 знакомест и 2 знака после запятой (точки)
# форматированная f-строка с плейсхолдерами
f_string = f'{name},\nвозраст: {age:2d} лет,\nрост: {height:.2f} см.'

print(f_string)
