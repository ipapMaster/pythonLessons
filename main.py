import datetime
import os
import sqlite3
from data import db_session
from data.news import News  # Подключили модель News
from data.users import User  # Подключили модель Users
from flask import Flask, url_for, redirect, request  # flask.request - с чем пользователь к нам пришёл
from flask import render_template, flash
import requests  # отдельный модуль для обращения к интернет-ресурсу (стороннему)
import json
from dotenv import load_dotenv
from addpost import NewPost
from loginform import LoginForm
from mail_sender import send_mail

app = Flask(__name__)  # создали экземпляр приложения
# секретный ключ для защиты от cross-site request forgery,
# CSRF - подделки межсайтовых запросов
app.config['SECRET_KEY'] = 'short secret key'


def connect_db():
    """
    Соединяемся с БД
    :return connection object:
    """
    conn = sqlite3.connect('base.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = connect_db()
    conn.execute(
        """CREATE TABLE IF NOT EXISTS posts 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT NOT NULL, 
        content TEXT NOT NULL)""")
    conn.close()


def close_db(conn):
    """
    :param conn - от какой базы надо отключиться:
    """
    conn.close()


@app.route('/')
def index():
    # with open('news.json', 'rt', encoding='utf=8') as file:
    #     news_list = json.loads(file.read())
    conn = connect_db()  # подключились к базе
    news = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()  # отключились от курсора базы
    return render_template('index.html',
                           title='Главная страница',
                           username='Слушатель',
                           news=news)


@app.route('/del/<int:post_id>')
def delete_post(post_id):
    conn = connect_db()
    query = f"DELETE FROM posts WHERE id={post_id}"
    # print(query)
    conn.execute(query)
    conn.commit()
    conn.close()
    flash(f'Новость №{post_id} была удалена!')
    flash('Вам теперь не узнать, что там было')
    return redirect(url_for('index'))  # '/'


# CRUD - Create, Read, Update, Delete
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    form = NewPost()
    if form.validate_on_submit():
        res = form.data
        title = res['title']
        content = res['content']
        conn = connect_db()
        query = f"UPDATE posts SET title='{title}', content='{content}' WHERE id={post_id}"
        # print(query)
        conn.execute(query)
        conn.commit()
        conn.close()
        return redirect(url_for('index'))  # '/'
    conn = connect_db()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    mess = f'Редактирование новости "{post[1]}"'
    return render_template("addpost.html",
                           title=mess,
                           news_action=mess,
                           form=form, post=post)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        res = form.data
        return render_template('success.html', title='Авторизация', form=res)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    form = NewPost()
    if form.validate_on_submit():
        res = form.data
        title = res['title']
        content = res['content']
        conn = connect_db()
        conn.execute("INSERT INTO posts (title, content) VALUES(?, ?)",
                     (title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))  # '/'
    return render_template('addpost.html', title='Добавление новости', form=form)


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
    # app.run(port=8000, host='127.0.0.1')
    # Добавим новость
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == 1).first()
    print(user)
    news = News(title="News#3", content="Content#3", is_private=False)
    print(news.get_title())
    # ДЗ
    # записи конкретного пользователя (user)
    # с взаимодействием с его записями
    user.news.append(news)  # почти как со списком
    # db_sess.add(news)
    db_sess.commit()

"""
    user.name = 'User3'
    user.about = 'Some info about user 3'
    user.email = 'email3@email.ru'
    db_sess.add(user)
    db_sess.commit()
    Вот наше первое приложение.<br>
    А вот <a href='/registration'>регистрация</a> пользователя.<br>
    А вот <a href='/test_template'>тест</a> шаблонизации.<br>
    А вот <a href='/image_sample'>ссылка</a> на картинку.<br>
    А вот <a href='/sample_page'>ссылка</a> на HTML-документ.<br>
    А вот <a href='/empty'>ссылка</a> которую мы не увидим (редирект на главную).<br>
    А вот <a href='/bootstrap_sample'>ссылка</a> на Bootstrap.<br>
    А вот <a href='/weather'>ссылка</a> на погоду.<br>
    А теперь <a href='/file_upload'>загрузим</a> файл.<br>
"""
