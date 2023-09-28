from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.news import News


def abort_if_news_not_found(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).get(news_id)
    if not news:
        abort(404, message=f'News {news_id} not found')


class NewsResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        db_sess = db_session.create_session()
        news = db_sess.query(News).get(news_id)
        return jsonify(
            {
                'news': news.to_dict(
                    only=('title', 'content', 'user_id', 'is_private')
                )
            }
        )

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        db_sess = db_session.create_session()
        news = db_sess.query(News).get(news_id)
        db_sess.delete(news)
        db_sess.commit()
        return jsonify({'success': 'Ok'})


parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('content', required=True)
parser.add_argument('is_private', required=True, type=bool)
parser.add_argument('user_id', required=True, type=int)


class NewsListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        news = db_sess.query(News).all()
        return jsonify(
            {
                'news': [
                    item.to_dict(
                        only=('title', 'content', 'user.name'))
                    for item in news]
            }
        )

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        news = News(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_private=args['is_private'],
        )
        db_sess.add(news)
        db_sess.commit()
        return jsonify({'success': 'Ok'})
