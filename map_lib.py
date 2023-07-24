from datetime import datetime
from io import BytesIO
import requests
from tkinter import NW, X, END
from tkinter import Tk, Button, PhotoImage, Label, Canvas, Entry
from PIL import ImageTk, Image, UnidentifiedImageError


class Map_Search:
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
        self.label_clock = Label(font=('Verdana', 20))
        self.header = Label(text='Адрес:', font=('Verdana', 12))
        self.entry = Entry(width=50, font=('Verdana', 14))
        self.entry.bind('<Return>', self.find)
        self.button = Button(text='Найти', command=self.search)
        self.canvas = Canvas(width=600, height=450)
        self.lon, self.lat = self.pt_lon, self.pt_lat = 37.617698, 55.755864
        # размещаем элементы
        self.header.place(x=15, y=35)
        self.entry.place(x=85, y=35)
        self.button.place(x=700, y=35)
        self.canvas.place(x=100, y=75)
        self.label_clock.place(x=320, y=540)
        self.delta = '0.001'  # для изменения spn
        # добавляем изображение-пустышку
        image = Image.new('RGB', (600, 450), (255, 255, 255))
        self.orig = image
        self.photo = ImageTk.PhotoImage(self.orig)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.show_time()  # вызов метода отображения часов

    def find(self, event=None):
        self.search()

    def search(self):
        self.what_to_find = self.entry.get().strip()
        if len(self.what_to_find) < 3:
            self.entry.delete(0, END)
            self.entry.insert(END, 'СПб, Можайская, 2')
            self.what_to_find = self.entry.get()
        geocoder_params = {
            'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
            'geocode': self.what_to_find,
            'format': 'json'
        }
        url = 'http://geocode-maps.yandex.ru/1.x/'
        try:
            response = requests.get(url, params=geocoder_params).json()
            toponym = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
            self.lon, self.lat = self.pt_lon, self.pt_lat = toponym['Point']['pos'].split()
            self.show_map()
        except IndexError:
            self.show_error_image('error_pict.png')

    def show_map(self):
        map_params = {
            'll': f'{self.lon},{self.lat}',
            'spn': f'{self.delta},{self.delta}',
            'l': 'map',
            'pt': f'{self.pt_lon},{self.pt_lat},pm2dgl'
        }
        map_url = 'http://static-maps.yandex.ru/1.x/'
        try:
            response = requests.get(map_url, params=map_params)
            self.orig = Image.open(BytesIO(response.content))
            self.photo = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        except UnidentifiedImageError:
            self.show_error_image('error_pict.png')

    def show_error_image(self, img):
        temp_img = Image.open(img)
        self.photo = ImageTk.PhotoImage(temp_img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

    def forever(self):
        self.root.mainloop()

    def show_time(self):
        time_to_show = datetime.now().strftime('%H:%M:%S')
        self.label_clock['text'] = time_to_show
        self.root.after(1000, self.show_time)


class MapOperate(Map_Search):
    def __init__(self):
        super().__init__()
        # кнопки управления будут здесь
        self.plus = Button(text='+', font=('Verdana', 14),
                           command=self.positive_zoom)
        self.minus = Button(text=chr(8212), font=('Verdana', 14),
                            command=self.negative_zoom)
        self.left = Button(text='<', font=('Verdana', 14),
                           command=self.move_left)
        self.right = Button(text='>', font=('Verdana', 14),
                            command=self.move_right)
        self.plus.place(x=475, y=540)
        self.minus.place(x=250, y=540)
        self.left.place(x=40, y=250)
        self.right.place(x=725, y=250)
        self.canvas.bind('<MouseWheel>', self.wheel_zoom)

    def wheel_zoom(self, event):
        if event.delta > 0:
            self.positive_zoom()
        else:
            self.negative_zoom()

    def positive_zoom(self):
        temp = float(self.delta) / 2
        if temp < 0.00025:
            temp = 0.00025
        self.delta = str(temp)
        self.search()

    def negative_zoom(self):
        temp = float(self.delta) * 2
        if temp > 32.768:
            temp = 32.768
        self.delta = str(temp)
        self.search()

    def move_right(self):
        temp = float(self.lon) - float(self.delta) * 0.1
        self.lon = str(temp)
        self.show_map()

    def move_left(self):
        temp = float(self.lon) + float(self.delta) * 0.1
        self.lon = str(temp)
        self.show_map()
