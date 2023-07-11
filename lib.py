class Car:
    def __init__(self, name=''):
        self.__name = ''
        if name != '':
            self.__name = name
        self.engine_on = False

    def start_engine(self):
        self.engine_on = True

    def drive(self, where):
        if self.engine_on:
            if self.__name:
                print('Едем', where, f'на {self.__name}')
            else:
                print('Едем', where)
        else:
            print('Мотор не заведён.')

    # getter (геттер)
    def get_name(self):
        return self.__name

    # setter (сеттер)
    def set_name(self, newname):
        if self.__name == '':
            self.__name = newname


# Для атрибутов принято использовать обозначения
# self.name - public
# self._name - protected (защищённый и доступен только в
# производных классах)
# self.__name - private (доступ только для членов класса)
