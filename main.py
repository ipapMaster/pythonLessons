# ООП
from lib import Car

if __name__ == '__main__':
    car = Car('Volvo')
    car.start_engine()
    car.set_name('Жигули')
    car.drive('на работу')
    # напрямую обращаться к атрибутам
    # не рекомендуется
