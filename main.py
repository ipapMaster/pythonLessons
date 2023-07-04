import json  # Java Script Object Notation

with open('pet.json', 'r') as f:
    pet = json.load(f)

for item in pet:
    if type(pet[item]) == list:
        print('Еда:', *pet[item])
    else:
        print(item, pet[item])