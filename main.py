from datetime import datetime

get_time = datetime.time(datetime.now())
cur_time = get_time.strftime("%H:%M:%S")
h = int(get_time.strftime("%H"))
print('На часах', cur_time)

if 6 <= h < 12:
    print('Доброе утро!')
elif 12 <= h < 18:
    print('Добрый день!')
elif 18 <= h < 23:
    print('Добрый вечер!')
else:
    print('Доброй ночи!')
