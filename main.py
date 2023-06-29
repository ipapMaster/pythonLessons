from random import choice

dashes = ['\u2680', '\u2681', '\u2682',
          '\u2683', '\u2684', '\u2685']

for _ in range(10):
    print(choice(dashes), choice(dashes))
