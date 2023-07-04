import os
import pickle as p

# dict = {
#     'стол': 'table',
#     'стул': 'chair'
# }

with open('dictinary.dat', 'rb') as f:
    dict = p.load(f)

print(dict)

