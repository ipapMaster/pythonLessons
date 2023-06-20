steps_yest = 15850  # шаги за вчера
steps_today = 3950  # шаги за сегодня
str_out = 'Вы прошли '
steps_sum = steps_yest + steps_today

if steps_sum >= 10000:
    print('Поздравляю!!!', end=' ')
    gyges = steps_sum // 10000
    str_out += str(steps_sum)
    str_out += ' шагов. Вам стало доступно ' + str(gyges) + 'Гб. '
    str_out += '\nДо следующего "гига" Вам осталось пройти '
    str_out += str(10000 * gyges - (steps_sum - 10000))
    str_out += ' шаг(ов).'
else:
    str_out += 'пока что ' + str(steps_sum) + ' шагов):'
    str_out += '\nДо получения 1 Гб Вам следует пройти ещё '
    str_out += str(10000 - steps_sum) + ' шаг(ов).'

print(str_out)
