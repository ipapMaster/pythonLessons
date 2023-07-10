# Декораторы
def say_hello():
    print('Hello')

# обернём функцию (wrapper - обёртка)
def wrapper():
    def say_hello():
        print('Hello')

    say_hello()


def decorator_function(func):
    def wrapper():
        print(f'Оборачиваемая функция: {func}')
        print('Выполняем обёрнутую функцию')
        func()
        print('Выходим из обёртки')

    return wrapper


# Выражение @decorator_function
# вызывает decorator_function, определённую выше
# с say_hello в качестве аргумента и присваивает
# имени say_hello возвращаемую функцию
@decorator_function  # синтаксический сахар
def say_hello():
    print('Hello')


say_hello()
