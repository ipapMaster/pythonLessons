# ООП - Спец. методы
from lib import Rectangle

if __name__ == '__main__':
    rect1 = Rectangle(80, 20)
    rect2 = Rectangle(20, 80)

    # print(id(rect1), id(rect2))
    print(rect1 == rect2)
    print(rect1 > rect2)
    print(rect1 + rect2)
    print(rect1 - rect2)
