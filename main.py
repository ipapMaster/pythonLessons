import os
import pickle as p

fname = 'dictinary.dat'


def print_dict():
    print('Словарь содержит: ')
    for k, v in dict.items():
        print(k, '-', v)


if not os.path.isfile(fname):
    dict = {'стол': 'table', 'стул': 'chair'}
    print('Файл словаря найден не был и создана минимальная версия.')
    print_dict()
else:
    with open(fname, 'rb') as f:
        dict = p.load(f)

while True:
    word = input('\nВведите слово для перевода на русском (или # для завершения): ')
    word = word.strip().lower()
    if word == '#' or word == '№':
        break
    if len(word) < 2 or word == ' ':
        print('Слишком короткое слово. Попробуйте снова')
        continue
    if word in dict:
        print(f'Слово {word} переводится как {dict[word]}')
    else:
        print(f'Перевод слова {word} в словаре отсутствует, но я могу его добавить.')
        new_word = input(f'Как перевести слово {word}: ')
        dict[word] = new_word.strip().lower()
        print(f'Спасибо. Перевод слова {word} добавлен в словарь как {new_word}.')

print('Неплохо поработали. До свидания!')
with open(fname, 'wb') as f:
    p.dump(dict, f)
