class Profile:
    def __init__(self, profession):
        self.profession = profession

    def info(self):
        return ''

    def describe(self):
        return f'Дополнительная информация: {self.profession} {self.info()}'


class Vacancy(Profile):
    def __init__(self, profession, salary):
        super().__init__(profession)
        self.salary, self.profession = salary, profession

    def info(self):
        return f'Предлагаемая зарплата: {self.salary} для профессии {self.profession}'


class Resume(Profile):
    def __init__(self, profession, experience):
        super().__init__(profession)
        self.profession = profession
        self.experience = experience

    def info(self):
        return f'Стаж работы {self.experience}'


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)
        self.a = a


class Greeter:
    def greet(self):
        print('Привет')


class GreetToName(Greeter):
    def greet(self):
        # print('Привет тебе')
        super().greet()


class Shape:
    def __init__(self):
        self.w = None
        self.h = None

    def area(self):
        return None

    def perimeter(self):
        return None


class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__()
        self.w = w
        self.h = h

    def perimeter(self):
        return (self.w + self.h) * 2

    def area(self):
        return self.w * self.h

    def diagonal(self):
        return ((self.w ** 2) + (self.h ** 2)) ** 0.5

    def __eq__(self, other):  # self.__eq__(other)
        if (self.h * self.w) == (other.h * other.w):
            return 'Они равны'
        return 'Они не равны'

    def __gt__(self, other):  # self.__qt__(other)
        if (self.h * self.w) > (other.h * other.w):
            return True
        return False

    def __add__(self, other):
        w = self.w + other.w
        h = self.h + other.h
        return Rectangle(w, h)

    def __sub__(self, other):
        w = abs(self.w - other.w)
        h = abs(self.h - other.h)
        return Rectangle(w, h)

    def __str__(self):
        return f'Rectangle({self.w}, {self.h})'


class Square(Rectangle):
    def __init__(self, a):
        # print('Конструируем квадрат из прямоугольника')
        # self.a = a
        super().__init__(a, a)  # вызван конструктор базового класса


class Time:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        m += s // 60
        s = s % 60
        return Time(m, s)

    def __str__(self):
        return f'Время {self.minutes}:{self.seconds}'

    def __repr__(self):
        return f'Time({self.minutes}:{self.seconds})'

    def time_info(self):
        return f'{self.minutes}:{self.seconds}'


class ReversedList:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, item):
        return self.lst[len(self.lst) - 1 - item]
