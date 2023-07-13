# ООП - Спецметоды
from lib import Time

if __name__ == '__main__':
    t1 = Time(5, 50)
    t2 = Time(3, 20)

    t3 = t1 + t2

    print(t3.time_info())
