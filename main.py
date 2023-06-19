python_group = []

python_group += ['Терентьев']
python_group += ['Петров', 'Сидоров']
python_group += ['Творогов']

print('В группе', len(python_group), 'чел.\nВот они:')

counter = 0

while counter < len(python_group):
    print('\t', str(counter + 1) + '.', python_group[counter])
    counter += 1
