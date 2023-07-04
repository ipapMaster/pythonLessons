import json  # Java Script Object Notation

pet = {
    'name': 'Mursik',
    'age': 5,
    'meal': ['Purina', 'Wiskas']
}

with open('pet.json', 'w') as f:
    json.dump(pet, f)
