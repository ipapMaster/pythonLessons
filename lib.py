from tkinter import *
import requests
from urllib.request import urlopen
from io import BytesIO
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.win = Tk()  # создаём объект окна
        self.win.title('Информация о погоде')
        self.win.geometry('700x400')
        self.win.resizable(False, False)
        # Иконка на Ваш выбор - скачать в корень проекта файл icon.png
        # self.win.iconphoto(True, PhotoImage(file='icon.png'))
        self.title = Label(text='Погода', background='yellow',
                           foreground='red', font=('Verdana', 18))  # Формат цвета '#45ff78'
        self.title.pack(fill=X)
        self.canvas = Canvas(bg='white', width=100, height=100)
        self.canvas.pack(anchor=CENTER, pady=10)
        mess = StringVar()
        mess.set('Курск')
        self.town = Entry(width=40, font=('Verdana', 15), textvariable=mess)
        self.town.pack(side=LEFT, fill=X, anchor=N, padx=50)
        self.btn = Button(text='Получить', command=self.get_weather)
        self.btn.pack(side=LEFT, fill=X, anchor=N)
        self.temper = Label(font=('Verdana', 18))
        self.temper.place(x=50, y=210)
        self.flike = Label(font=('Verdana', 18))
        self.flike.place(x=50, y=250)
        self.hmd = Label(font=('Verdana', 18))
        self.hmd.place(x=50, y=290)
        self.icon = None
        # Ожидание действий пользователя
        self.win.mainloop()

    def get_weather(self):
        if self.town.get() == '':
            town = 'Санкт Петербург'
        else:
            town = self.town.get()
        # полученный ключ
        key = 'c747bf84924be997ff13ac5034fa3f86'
        # API - Server
        url = 'http://api.openweathermap.org/data/2.5/weather'
        # Дополнительные параметры
        params = {'APPID': key, 'q': town, 'units': 'metric'}
        # Отправляем запрос:
        response = requests.get(url, params=params)
        result = response.json()  # читаем отсюда
        code = result['cod']  # прочли код ответа
        if code != 200:
            self.temper['text'] = 'Нет информации'
            self.flike['text'] = ''
            self.hmd['text'] = ''
        else:
            temper = result['main']['temp']  # температура
            feels_like = result['main']['feels_like']  # ощущается как
            humidity = result['main']['humidity']  # влажность
            icon_temp = result['weather'][0]['icon']  # иконка
            self.url = f'https://openweathermap.org/img/wn/{icon_temp}@2x.png'
            icon = urlopen(self.url).read()
            self.image = ImageTk.PhotoImage(Image.open(BytesIO(icon)))
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)
            self.temper['text'] = f'Температура (город: {town}): {temper: .1f} \xB0C'
            self.flike['text'] = f'Ощущается как: {feels_like: .1f} \xB0C'
            self.hmd['text'] = f'Влажность: {humidity: .1f} %'
