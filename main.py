import datetime
import os

import misc
import news_resources
from data import db_session, news_api
from data.news import News  # Подключили модель News
from data.users import User  # Подключили модель Users
from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, url_for, redirect, request, jsonify  # flask.request - с чем пользователь к нам пришёл
from flask import render_template, make_response, session, flash
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
import requests  # отдельный модуль для обращения к интернет-ресурсу (стороннему)
from sqlalchemy import or_
from forms.news import NewsForm
from forms.user import RegisterForm
from forms.loginform import LoginForm
from mail_sender import send_mail

app = Flask(__name__)  # создали экземпляр приложения
# регистрируем API-сервис
api = Api(app)
# секретный ключ для защиты от cross-site request forgery,
# CSRF - подделки межсайтовых запросов
app.config['SECRET_KEY'] = 'short secret key'
# срок жизни сессии
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

# создаём объект менеджера авторизации пользователя
# и приписываем его к нашему приложению
login_manager = LoginManager()
login_manager.init_app(app)

# добавляем собственные функции в шаблонизатор Jinja
# для фильтрации, передавая day_diff как объект
app.jinja_env.filters['retrieve_days'] = misc.day_diff
# а также для требуемого для визуализации формата даты
app.jinja_env.filters['date_format'] = misc.format_datetime


# функция получения данных пользователя
@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)  # return db_sess.query(User).get(user_id)


@app.errorhandler(401)
def http_401_handler(error):
    flash('Для начала войдите с логином и паролем')
    return redirect('/login')


@app.errorhandler(404)
def http_404_handler(error):
    return make_response(jsonify({'error': 'Request was not correct'}), 404)

@app.errorhandler(415)
def http_415_handler(error):
    return make_response(jsonify({'error': 'Request had bad format'}), 415)


@app.route('/')
def index():
    found = request.args.get('substring')
    if found:
        params = {'title': f'Результаты поиска {found}',
                  'username': f'Слушатель. Искали {found}. Авторизуйтесь.'}
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(
            or_(
                News.title.like(f'%{found}%'),
                News.content.like(f'%{found}%'),
                News.title.like(f'%{found.title()}%'),
                News.content.like(f'%{found.title()}%'),
                News.title.like(f'%{found.title()}%'),
                News.content.like(f'%{found.title()}%')
                & (News.is_private == 0)
            )
        )
        params['news'] = news
        return render_template('index.html', **params)
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            ((News.is_private == 1) &
             (News.user == current_user)) |
            (News.is_private == 0)
        )
    else:
        news = db_sess.query(News).filter(News.is_private == 0)
    return render_template('index.html',
                           title='Главная страница',
                           username='Слушатель. Авторизуйтесь, пожалуйста',
                           news=news)


@app.route('/<int:post_id>')
def get_news_by_id(post_id):
    url = f'http://127.0.0.1:8000/api/news/{post_id}'
    response = requests.get(url).json()
    return response


@app.route('/test_cookie')
def cookie_test():
    """
    Чтобы удалить данные из cookies
    res.set_cookie("visits_count", '1', max_age=0)
    """
    visit_count = int(request.cookies.get('visits_count', 0))
    if visit_count:
        res = make_response(f'Вы были на этой странице {visit_count + 1} раз')
        res.set_cookie('visits_count', str(visit_count + 1),
                       max_age=60 * 60 * 24)
    else:
        res = make_response('Вы тут впервые')
        res.set_cookie('visits_count', '1',
                       max_age=60 * 60 * 24)
    return res


@app.route('/test_session')
def session_test():
    """
    Для удаления сессии используем следующий код
    session.pop('visits_count', None)
    """
    visit_count = session.get('visits_count', 0)
    session['visits_count'] = visit_count + 1
    return make_response(f'Вы пришли на эту страницу {visit_count + 1} раз')


@app.route('/del/<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == post_id,
                                      News.user == current_user).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        flash(f'{current_user.name}, у Вас нет прав на удаление этой новости')
        return redirect('/')
    return redirect('/')


# CRUD - Create, Read, Update, Delete
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    form = NewsForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == post_id,
                                          News.user == current_user).first()
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
            form.submit.label.text = 'Обновить'
        else:
            flash(f'{current_user.name}, у Вас нет прав на редактирование этой новости')
            return redirect('/')
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == post_id,
                                          News.user == current_user).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            flash('Новость успешно обновлена')
            return redirect('/')
        else:
            flash(f'{current_user.name}, у Вас нет прав на редактирование этой новости')
            return redirect('/')
    return render_template('news.html', title='Редактирование новости', form=form)


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
        flash('Процедура регистрации прошла успешно!')
        return redirect('/login')
    return render_template('register.html',
                           title='Регистрация',
                           form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли')
    return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    else:
        form = LoginForm()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            user = db_sess.query(User).filter(User.email == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash('Вы успешно вошли')
                return redirect('/')
            flash('Неверные пара: логин - пароль')
            render_template('login.html', title='Авторизация',
                            message='Неверный логин или пароль',
                            form=form)
        return render_template('login.html', title='Авторизация', form=form)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_post():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        flash('Новость добавлена')
        return redirect('/')
    return render_template('news.html', title='Добавление новости', form=form)


@app.route('/mail_form', methods=['GET'])
def main_form():
    return render_template('ваш.html')


# <form method="post" class="form-group">
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
@login_required
def users():
    t = 'Кто за кем в очереди???'
    if current_user.is_admin():
        return render_template('query.html', title=t)
    flash(f'У Вас недостаточно прав, {current_user.name} для просмотра этой страницы')
    return redirect('/')


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


if __name__ == '__main__':
    # создание или подключение к БД
    db_session.global_init('db/blogs.db')
    # регистрация api
    # app.register_blueprint(news_api.blueprint)
    # регистрация ресурсов
    # для чтения всех новостей
    api.add_resource(news_resources.NewsListResource, '/api/v2/news')
    # для чтения новости по номеру
    api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
    # запуск приложения
    app.run(port=8000, host='127.0.0.1')
