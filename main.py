from flask import Flask, url_for, redirect, request  # flask.request - с чем пользователь к нам пришёл
import requests  # отдельный модуль для обращения к интернет-ресурсу (стороннему)

app = Flask(__name__)


@app.route('/')
def index():
    return """Вот наше первое приложение.<br>
    А вот <a href='/countdown'>ссылка</a> на обратный отсчёт.<br>
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
    PATCH - частиное изменение данных
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
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <title>HTML-страница c Bootstrap</title>
</head>
<body>
<h1>HTML-документ c Bootstrap</h1>
<div class="alert alert-primary" role="alert">Балуемся с Bootstrap</div>
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
