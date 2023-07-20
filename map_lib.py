from datetime import datetime
from io import BytesIO
import requests
from tkinter import NW, X
from tkinter import Tk, Button, PhotoImage, Label, Canvas, Entry
from PIL import ImageTk, Image


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
        self.label_clock = Label(font=('Verdana', 20))
        self.header = Label(text='Адрес:', font=('Verdana', 12))
        self.entry = Entry(width=50, font=('Verdana', 14))
        self.button = Button(text='Найти', command=self.search)
        self.canvas = Canvas(width=600, height=450)
        # размещаем элементы
        self.header.place(x=15, y=35)
        self.entry.place(x=85, y=35)
        self.button.place(x=700, y=35)
        self.canvas.place(x=100, y=75)
        self.label_clock.place(x=320, y=540)
        # добавляем изображение-пустышку
        image = Image.new('RGB', (600, 450), (255, 255, 255))
        self.orig = image
        self.photo = ImageTk.PhotoImage(self.orig)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.show_time()  # вызов метода отображения часов

    def search(self):
        geocoder_params = {
            'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
            'geocode': 'СПб, Можайская, 2',
            'format': 'json'
        }
        url = 'http://geocode-maps.yandex.ru/1.x/'
        response = requests.get(url, params=geocoder_params).json()
        toponym = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        coords = toponym['Point']['pos']
        coords = coords.split()
        map_params = {
            'll': ','.join(coords),
            'spn': '0.005,0.005',
            'l': 'map',
            'pt': ','.join(coords) + ',pm2dgl'
        }
        map_url = 'http://static-maps.yandex.ru/1.x/'
        response = requests.get(map_url, params=map_params)
        self.orig = Image.open(BytesIO(response.content))
        self.photo = ImageTk.PhotoImage(self.orig)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)




    def forever(self):
        self.root.mainloop()

    def show_time(self):
        time_to_show = datetime.now().strftime('%H:%M:%S')
        self.label_clock['text'] = time_to_show
        self.root.after(1000, self.show_time)
