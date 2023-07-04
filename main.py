import os
import pickle as p

dict = {
    'стол': 'table',
    'стул': 'chair'
}

with open('dictinary.dat', 'wb') as f:
    p.dump(dict, f)



