from flask import Flask, url_for, redirect, request  # flask.request - с чем пользователь к нам пришёл
from flask import render_template
import requests  # отдельный модуль для обращения к интернет-ресурсу (стороннему)

app = Flask(__name__)


@app.route('/odd_even')
def odd_even():
    params = {
        'number': 2,
        'title': 'Четное или нечётное'
    }
    return render_template('odd_even.html', **params)


@app.route('/test_template')
def template_test():
    params = {}
    params['username'] = 'Слушатель'
    params['title'] = 'Приветствие'
    return render_template('index.html', **params)


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


@app.route('/')
def index():
    return """Вот наше первое приложение.<br>
    А вот <a href='/registration'>регистрация</a> пользователя.<br>
    А вот <a href='/test_template'>тест</a> шаблонизации.<br>
    А вот <a href='/image_sample'>ссылка</a> на картинку.<br>
    А вот <a href='/sample_page'>ссылка</a> на HTML-документ.<br>
    А вот <a href='/empty'>ссылка</a> которую мы не увидим (редирект на главную).<br>
    А вот <a href='/bootstrap_sample'>ссылка</a> на Bootstrap.<br>
    А вот <a href='/weather'>ссылка</a> на погоду.<br>
    А теперь <a href='/file_upload'>загрузим</a> файл.<br>
    """


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


@app.route('/<town>')
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


@app.route('/countdown')
def countdown():
    lst = [str(i) for i in range(10, 0, -1)]
    lst.append('Старт!')
    return '<br>'.join(lst) + '<br><a href=\'/\'>назад</a>'


@app.route('/empty')
def empty():
    return redirect('/')


@app.route('/image_sample')
def img_sample():
    return f"""<img src="{url_for('static', filename='images/sea.png')}">
    <br><a href=\'/\'>назад</a>"""


@app.route('/sample_page')
def return_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    <title>Первая HTML-страница</title>
</head>
<body>
<h1>Первый HTML-документ</h1>
<a href="/">назад</a>
</body>
</html>"""


@app.route('/bootstrap_sample')
def bootstrap():
    with open('templates/index.html', 'rt', encoding='utf-8') as html:
        code = html.read()
    return code


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
