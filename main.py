# strip - убирает символы в начале и конце строки
# rstrip - убирает символы справа (конец строки)
# lstrip - убирает символы слева (начале строки)

string = '  pPythons       '

string = string.strip()  # "чистим" все пробелы
string = string.lstrip('p')  # убираем "p" слева (в начале)
string = string.rstrip('s')  # убираем "s" справа (в конце)

print(string)
