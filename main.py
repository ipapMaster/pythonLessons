counter = 0

while True:
    counter += 1
    if counter > 10:
        break
    if counter == 5:  # чтобы не печатать цифру 5
        continue
    print(counter)
    # куча всего

print('Цикл прекращён!')
