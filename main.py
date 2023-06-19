python_group = []

python_group += ['Терентьев']
python_group += ['Петров', 'Сидоров']
python_group += ['Творогов']

print('В группе', len(python_group), 'чел.\nВот они', end=': ')
print(*python_group, sep=', ', end='.\n')
