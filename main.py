# Декораторы

def time_elapsed(func):  # Декоратор
    import time

    def wrapper():
        start = time.time()  # засекли время
        func()
        end = time.time()  # выключили секундомер
        print(f'Потрачено времени: {end - start} сек.')
    return wrapper

@time_elapsed
def long_list_creation():
    # создаём список из 1'000'000 значений
    a = [i for i in range(10000000)]


long_list_creation()
