from datetime import datetime

get_time = datetime.time(datetime.now())
cur_time = get_time.strftime("%H:%M:%S")
h = int(get_time.strftime("%H"))
print('На часах', cur_time)

if h >= 6 and h < 12:
    print('Доброе утро!')
elif h >= 12 and h < 18:
    print('Добрый день!')
elif h >= 18 and h < 23:
    print('Добрый вечер!')
else:
    print('Доброй ночи!')
