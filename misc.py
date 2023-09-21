# miscellaneous - прочие (полезности)
from datetime import date, datetime


def declination(number, titles, show=True):
    """
    Функция склонения существительных в
    зависимости от целого числа
    :param number: собственно число
    :param titles: кортеж форм существительного
    :param show: показывать ли само число
    :return: значение(?) + форму существительного
    """
    out = ''  # что будем выводить
    temp = number % 100
    if temp > 19:
        temp %= 10

    if show:
        out += str(number) + ' '

    match temp:
        case 1:
            out += titles[0]
        case 2 | 3 | 4:
            out += titles[1]
        case _:
            out += titles[2]

    return out


def day_diff(date1, date2):
    """
    Функция, возвращающая число дней
    путем вычитания двух дат
    :param date1: первая дата в формате YY-mm-dd h:m:s.f
    :param date2: вторая дата в формате YY-mm-dd h:m:s.f
    :return: целое число разницы в днях
    """
    if isinstance(date1, str):
        d0 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S.%f')
    else:
        d0 = date1
    if isinstance(date2, str):
        d1 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S.%f')
    else:
        d1 = date2
    return abs((d0 - d1).days)
