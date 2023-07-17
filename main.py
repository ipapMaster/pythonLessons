# ООП - Наследование
# Класс B - частный случай класса A
# Класс A - называют: базовый (родительский), super-class
# Класс B - называют: производный (дочерний), derived
# Класс B "умеет" то же, что и класс A. Плюс "умеет"
# что-то сверх того, что может A
# Класс B "расширяет" класс A - class B(A)

from tkinter import Tk, Button
from PIL import ImageTk, Image


class MyButton(Button):
    def __init__(self, pict, command):
        self.image = Image.open(pict)
        self.image = self.image.resize((100, 100))
        self.pict = ImageTk.PhotoImage(self.image)
        super().__init__(image=self.pict, command=command)


root = Tk()
root.geometry('800x600')
root.title('Красивая кнопка')

MyButton("pensil.png", command=lambda: print('click')).pack()
MyButton("pensil.jpg", command=lambda: print('click')).pack()
MyButton("sea.png", command=lambda: print('click')).pack()
root.mainloop()
