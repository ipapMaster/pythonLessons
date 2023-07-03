import pymorphy2

m = pymorphy2.MorphAnalyzer().parse('рубль')[0]

num = 271

print(f'Мы потратили {num} {m.make_agree_with_number(num).word}.')
