# ООП

class Car:
    def __init__(self):
        self.engine_on = False

    def start_engine(self):
        self.engine_on = True

    def drive(self, where):
        if self.engine_on:
            print('Едем', where)
        else:
            print('Мотор не заведён.')


car = Car()
car.start_engine()
car.drive('на работу!')
