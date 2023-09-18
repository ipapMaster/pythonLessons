import datetime
import os
from data import db_session
from data.news import News  # Подключили модель News
from data.users import User  # Подключили модель Users
from flask import Flask, url_for, redirect, request  # flask.request - с чем пользователь к нам пришёл
from flask import render_template, flash
import requests  # отдельный модуль для обращения к интернет-ресурсу (стороннему)
import json
from dotenv import load_dotenv
from addpost import NewPost
from forms.user import RegisterForm
from loginform import LoginForm
from mail_sender import send_mail

app = Flask(__name__)  # создали экземпляр приложения
# секретный ключ для защиты от cross-site request forgery,
# CSRF - подделки межсайтовых запросов
app.config['SECRET_KEY'] = 'short secret key'


@app.route('/')
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private == 0)
    return render_template('index.html',
                           title='Главная страница',
                           username='Слушатель',
                           news=news)


@app.route('/del/<int:post_id>')
def delete_post(post_id):
    pass


# CRUD - Create, Read, Update, Delete
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    pass

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # form.about.data =
        if form.password.data != form.password_again.data:
            return render_template('register.html',
                                   title='Регистрация',
                                   form=form,
                                   message='Пароли не совпадают')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html',
                                   title='Регистрация',
                                   form=form,
                                   message='Такой пользователь уже существует')
        user = User(name=form.name.data,
                    email=form.email.data,
                    about=form.about.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html',
                           title='Регистрация',
                           form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        res = form.data
        return render_template('success.html', title='Авторизация', form=res)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    pass


@app.route('/mail_form', methods=['GET'])
def main_form():
    return render_template('ваш.html')


# <form method="post" class="from-group">
# 	<input type="email" class="form-control" name="email">
# 	<button type="submit" class="btn btn-primary">Прислать письмо</button>
# </form>

@app.route('/mail_form', methods=['POST'])
def mail_form():
    email = request.values.get('email')
    if send_mail(email, 'Вам письмо', 'Поздравляю, всё работает'):
        return f'Письмо на адрес {email} успешно отправлено!'
    return 'Сбой при отправке'


# <form method="post" class="from-group">
# 	<input type="email" class="form-control" name="email">
# 	<button type="submit" class="btn btn-primary">Прислать письмо</button>
# </form>
@app.route('/users')
def users():
    t = 'Кто за кем в очереди???'
    return render_template('query.html', title=t)


@app.route('/combo')
def combo():
    params = {
        'title': 'Ингредиенты окрошки',
        'h1': 'Ингредиенты окрошки'
    }
    return render_template('combo_test.html', **params)


@app.route('/slideshow')
def slides():
    root = os.getcwd()  # получили путь корневого каталога
    os.chdir('./static/slides')  # перешли в папку слайдов
    cwd = os.getcwd()  # записали путь к слайдам в cwd
    # записываем все имена файлов в список (исключая имена каталогов)
    picts = [f.name for f in os.scandir(cwd) if f.is_file()]
    os.chdir(root)  # возвращаемся в корневой каталог
    return render_template('pictures.html', picts=picts)


@app.route('/odd_even/<int:num>')
def odd_even(num):
    params = {
        'number': num,
        'title': 'Четное или нечётное'
    }
    return render_template('odd_even.html', **params)


@app.route('/registration', methods=['GET', 'POST'])
def regs():
    user_dict = {
        'email': 'эл. почта:',
        'password': 'пароль:',
        'class': 'аудитория:',
        'about': 'обо мне:',
        'sex': 'пол:',
        'accept': 'согласен с правилами'
    }
    if request.method == 'POST':
        with open('result.html', 'r', encoding='utf-8') as html:
            content = html.read()
        content = content.replace('{{ style }}', f'{url_for("static", filename="css/style.css")}')
        d = dict(request.form)
        insertion = ''
        f = request.files['file']
        if f:
            f.save('static/images/' + f.filename)
            insertion += f"""<div class="row text-center">
                <div class="col text-center">
                    <img src={url_for("static", filename="images/" + f.filename)} height="400">
                </div>
            </div>"""
        for key in d:
            insertion += f"""<div class="row">
            <div class="col text-end h2">{user_dict[key]}</div>
            <div class="col text-start h2">{d[key]}</div>
            </div>
            """
        content = content.replace('{{ table }}', insertion)
        return content
    with open('regform.html', 'r', encoding='utf-8') as html:
        content = html.read()
    content = content.replace('{{ style }}', f'{url_for("static", filename="css/style.css")}')
    return content


@app.route('/file_upload', methods=['GET', 'POST'])
def sample_upload():
    if request.method == 'POST':
        f = request.files['file']
        return f.read()
    return """<form method="post" enctype="multipart/form-data">
    <label for="text-file">Выберите файл</label>
    <input type="file" id="text-file" name="file">
    <input type="submit" value="Загрузить">
    </form>
    """


@app.route('/weather/<town>')
def town_weather(town):
    """
    :param town:
    :return weather:
    :string - параметр по умолчанию (тип не указывается)
    :<int:town> - целое число
    :<float:town> - дробь
    :<path:town> - путь, содержащий слэши и т.д.
    :<uuid:town> - строка идентификатор в hex-виде 6564635-t46654-dsfsdf (16-байт)
    """
    key = 'c747bf84924be997ff13ac5034fa3f86'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': town, 'units': 'metric'}
    response = requests.get(url, params=params).json()
    return f"Температура в городе {town} - {response['main']['temp']:.1f} °C."


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    """
    Основные методы для форм:
    GET - по умолчанию http://site.ru?param1=5&param2=8
    POST - отправляет данные на сервер
    PUT - заменяет данные сервера, данным запроса
    DELETE - удаляет указанные данные
    PATCH - частичное изменение данных
    """
    if request.method == 'POST':
        if request.form.get('town'):
            town = request.form['town']
        else:
            town = 'Москва'
        key = 'c747bf84924be997ff13ac5034fa3f86'
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': key, 'q': town, 'units': 'metric'}
        response = requests.get(url, params=params).json()
        return f"""<img src="https://openweathermap.org/img/wn/{response['weather'][0]['icon']}@2x.png"><br>
        Температура в городе {town} - {response['main']['temp']:.1f} °C.
        <br><a href='/weather'>назад</a>"""
    return """<form method="POST">
    <h2>Введите город:</h2>
    <input type="text" name="town" placeholder="Москва">
    <input type="submit" value="Узнать">
    </form>
    """


# когда первый раз зашли на сайт
# перед запуском рендера шаблона (первый из них)


if __name__ == '__main__':
    # создание или подключение к БД
    db_session.global_init('db/blogs.db')
    # запуск приложения
    app.run(port=8000, host='127.0.0.1')
