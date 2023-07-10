# ООП
class Fruit:
    pass


class Greeter:
    def hello(self):
        print('Hello')

    def hello_to_name(self, name):
        print('Hello,', name)


greet1 = Greeter()
greet1.hello()  # Greeter.hello()

greet2 = Greeter()
greet2.hello()

greet2.hello_to_name('Tom')

apple = Fruit()
apple.name = 'Яблоко'
apple.weight = 150

appricot = Fruit()
appricot.name = 'Абрикос'
appricot.weight = 50
appricot.weight += 10

print(appricot.weight)
