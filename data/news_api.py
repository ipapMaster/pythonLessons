import flask
from flask import jsonify, request
from flask_login import login_required

from . import db_session
from .news import News

# Метод GET - Получение списка всех объектов (всех новостей). http://127.0.0.1:8000/api/news
# Метод GET - Информация о конкретном объекте (новости). http://127.0.0.1:8000/api/news/1
# Метод POST - Создание нового объекта (добавление новости). http://127.0.0.1:8000/api/news/
# Метод PUT - Изменить объект (новость на основе её ID). http://127.0.0.1:8000/api/news/1
# Метод DELETE - Удалить объект (новость на основе её ID). http://127.0.0.1:8000/api/news/1

blueprint = flask.Blueprint('news_api', __name__, template_folder='templates')


@blueprint.route('/api/news', methods=['GET'])
@login_required
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return jsonify(
        {
            'news': [item.to_dict(only=('title', 'content', 'user.name')) for item in news]
        }
    )


@blueprint.route('/api/news/<int:news_id>', methods=['GET'])
def get_one_news(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).get(news_id)
    if not news:
        return jsonify({'error': 'News not found'})
    return jsonify(
        {
            'news': news.to_dict(only=('title', 'user_id', 'is_private'))
        }
    )


@blueprint.route('/api/news', methods=['POST'])
def create_news():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['title', 'content', 'user_id', 'is_private']):
        return jsonify({'error': 'Not full request'})
    db_sess = db_session.create_session()
    news = News(
        title=request.json['title'],
        content=request.json['content'],
        user_id=request.json['user_id'],
        is_private=request.json['is_private'],
    )
    db_sess.add(news)
    db_sess.commit()
    return jsonify({'success': 'Ok'})


@blueprint.route('/api/news/<int:news_id>', methods=['PUT'])
def update_news(news_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['title', 'content', 'user_id', 'is_private']):
        return jsonify({'error': 'Not full request'})
    db_sess = db_session.create_session()
    news = db_sess.query(News).get(news_id)
    if news:
        news.title = request.json['title']
        news.content = request.json['content']
        news.user_id = request.json['user_id']
        news.is_private = request.json['is_private']
        db_sess.commit()
    else:
        return jsonify({'error': 'Not changed'})
    return jsonify({'success': 'Changed'})


@blueprint.route('/api/news/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).get(news_id)
    if not news:
        return jsonify({'error': 'Nothing to delete (not found)'})
    db_sess.delete(news)
    db_sess.commit()
    return jsonify({'success': 'Deleted'})
