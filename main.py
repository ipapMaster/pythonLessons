# ООП - Наследование
# Класс B - частный случай класса A
# Класс A - называют: базовый (родительский), super-class
# Класс B - называют: производный (дочерний), derived
# Класс B "умеет" то же, что и класс A. Плюс "умеет"
# что-то сверх того, что может A
# Класс B "расширяет" класс A - class B(A)
from lib import Rectangle, Square, Shape, GreetToName


def describe_shape(shape):
    print(f'Мы имеем дело с классом {shape.__class__.__name__}({shape.w}, {shape.h})')
    print(f'Периметр {shape.__class__.__name__} будет {shape.perimeter()}')
    print(f'Площадь {shape.__class__.__name__} будет {shape.area()}')


if __name__ == '__main__':
    shape = Shape()
    rect1 = Rectangle(80, 20)
    rect2 = Rectangle(20, 80)
    sq1 = Square(5)
    # print(sq1.perimeter())
    # print(sq1.area())
    # print(sq1.diagonal())
    describe_shape(rect2)
    describe_shape(sq1)
    describe_shape(shape)
    gr = GreetToName()
    gr.greet()

