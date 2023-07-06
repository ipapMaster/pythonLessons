# Утверждение (assert -> AssertionError)

text = input('Введите текст: ')

try:
    assert len(text) > 3  # утвержение, что длина текста свыше 3 символов
except AssertionError:
    print('Длина введённого текста меньше 3-х символов.')
else:
    print('Всё в порядке. Длина текста в норме.')
