from tkinter import Tk, Button, PhotoImage, Label, Canvas
from tkinter import CENTER, LEFT, NW, N, X
from tkinter import filedialog
import os
from PIL import ImageTk, Image


class App:
    def __init__(self):
        # настройки параметров окна
        self.root = Tk()
        self.root.geometry('800x600')
        self.root.title('Работа с картинками')
        self.root.resizable(False, False)
        self.root.iconphoto(True, PhotoImage(file='pencil.png'))
        self.label = Label(text='Работа с изображениями',
                           background='yellow', foreground='red',
                           font=('Verdana', 16))
        self.label.pack(fill=X)
        self.canvas = Canvas(height=400, width=400)
        # добавляем изображение-пустышку
        image = Image.new('RGB', (400, 400), (255, 255, 255))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack(anchor=CENTER, pady=5)
        self.button = Button(text='Загрузить', command=self.change_image)
        self.button.pack(side=LEFT, anchor=N, fill=X,
                         expand=True)
        self.cwd = os.getcwd()  # текущий каталог
        self.root.mainloop()

    def change_image(self):
        try:
            fullpath = filedialog.askopenfilename(
                title='Выбор картинки', initialdir=self.cwd,
                filetypes=(
                    ('GIF-ки', '*.gif'),
                    ('PNG-шки', '*.png'),
                    ('JPG-шки', '*.jpg')
                )
            )
            image = Image.open(fullpath)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        except AttributeError:
            self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

