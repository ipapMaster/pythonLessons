import os
from tkinter import Tk, Button, PhotoImage, Label, Canvas, Entry
from tkinter import CENTER, LEFT, NW, N, X
from tkinter import filedialog
from PIL import ImageTk, Image, ImageFilter, ImageEnhance


class App:
    def __init__(self):
        # настройки параметров окна
        self.root = Tk()
        self.root.geometry('800x600')
        self.root.title('Поиск на карте')
        self.root.resizable(False, False)
        self.root.iconphoto(True, PhotoImage(file='pencil.png'))
        self.label = Label(text='Поиск на карте',
                           background='yellow', foreground='red',
                           font=('Verdana', 16))
        self.label.pack(fill=X)
        self.header = Label(text='Адрес:', font=('Verdana', 12))
        self.entry = Entry(width=50, font=('Verdana', 14))
        self.button = Button(text='Найти', command=self.search)
        self.canvas = Canvas(width=600, height=450)
        self.header.place(x=15, y=35)
        self.entry.place(x=85, y=35)
        self.button.place(x=700, y=35)
        self.canvas.place(x=100, y=75)
        # добавляем изображение-пустышку
        image = Image.new('RGB', (600, 450), (255, 255, 255))
        self.orig = image
        self.photo = ImageTk.PhotoImage(self.orig)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.cwd = os.getcwd()  # текущий каталог
        self.root.mainloop()

    def search(self):
        pass
