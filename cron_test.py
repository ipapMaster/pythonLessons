import schedule
import datetime

count = 1


def task():
    global count
    print(f'Задача выполнена {count} раз.')
    count += 1
    print(datetime.datetime.now().strftime('%H:%M:%S'))
    if count > 3:
        return schedule.CancelJob


schedule.every(3).seconds.do(task)

while True:
    schedule.run_pending()
