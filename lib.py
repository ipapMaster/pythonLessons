import os
from tkinter import Tk, Button, PhotoImage, Label, Canvas
from tkinter import CENTER, LEFT, NW, N, X
from tkinter import filedialog
from PIL import ImageTk, Image, ImageFilter, ImageEnhance


class App:
    def __init__(self):
        # настройки параметров окна
        self.root = Tk()
        self.root.geometry('800x600')
        self.root.title('Работа с картинками')
        self.root.resizable(False, False)
        self.root.iconphoto(True, PhotoImage(file='static/images/world.png'))
        self.label = Label(text='Работа с изображениями',
                           background='yellow', foreground='red',
                           font=('Verdana', 16))
        self.label.pack(fill=X)
        self.canvas = Canvas(height=400, width=400)
        # добавляем изображение-пустышку
        image = Image.new('RGB', (400, 400), (255, 255, 255))
        self.orig = image
        self.photo = ImageTk.PhotoImage(self.orig)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack(anchor=CENTER, pady=5)
        self.button = Button(text='Загрузить', command=self.change_image)
        self.button.pack(side=LEFT, anchor=N, fill=X, expand=True, padx=5)
        self.orig_btn = Button(text='Оригинал', command=self.orig_image)
        self.orig_btn.pack(side=LEFT, anchor=N, fill=X, expand=True, padx=5)
        self.blur = Button(text='Размыть', command=self.image_blur)
        self.blur.pack(side=LEFT, anchor=N, fill=X, expand=True, padx=5)
        self.sharp = Button(text='Резкость', command=self.image_sharp)
        self.sharp.pack(side=LEFT, anchor=N, fill=X, expand=True, padx=5)
        self.flip_h = Button(text='FlipH', command=self.image_flip_h)
        self.flip_h.pack(side=LEFT, anchor=N, fill=X, expand=True, padx=5)
        self.flip_v = Button(text='FlipV', command=self.image_flip_v)
        self.flip_v.pack(side=LEFT, anchor=N, fill=X, expand=True, padx=5)
        self.rotate = Button(text='90\xB0', command=self.image_rotate_90)
        self.rotate.pack(side=LEFT, anchor=N, fill=X, expand=True, padx=5)
        self.contour = Button(text='Контур', command=self.image_contour)
        self.contour.pack(side=LEFT, anchor=N, fill=X, expand=True, padx=5)
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
            if image.mode != 'RGB':  # получили mode изображения и проверили
                image = image.convert('RGB')
            w, h = image.size  # получили размеры изображения
            if w > 400:
                ratio = w / 400  # во сколько раз больше
                image = image.resize((400, int(h / ratio)))
            self.orig = image
            self.photo = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        except AttributeError:
            self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

    def image_blur(self):
        blur_img = self.orig.filter(ImageFilter.BLUR)
        self.photo = ImageTk.PhotoImage(blur_img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

    def orig_image(self):
        self.photo = ImageTk.PhotoImage(self.orig)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

    def image_sharp(self):
        sharper = ImageEnhance.Sharpness(self.orig)
        sharped_img = sharper.enhance(10.0)
        self.photo = ImageTk.PhotoImage(sharped_img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

    def image_flip_h(self):
        flipped_img = self.orig.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.photo = ImageTk.PhotoImage(flipped_img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

    def image_flip_v(self):
        flipped_img = self.orig.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        self.photo = ImageTk.PhotoImage(flipped_img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

    def image_rotate_90(self):
        temp = self.orig.transpose(Image.Transpose.ROTATE_90)
        self.photo = ImageTk.PhotoImage(temp)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

    def image_contour(self):
        temp = self.orig.convert('L')
        temp = temp.filter(ImageFilter.FIND_EDGES)
        self.photo = ImageTk.PhotoImage(temp)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
