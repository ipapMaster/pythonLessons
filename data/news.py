import datetime
import sqlalchemy
import misc
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    # Привяжем нашу новость к пользователю из таблицы users
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship("User")

    def get_title(self):
        return self.title

    def get_days(self):
        """
        :return: Возвращает число дней с требуемой формой слова
        """
        today = datetime.datetime.now()  # текущие дата и время
        res = misc.declination(misc.day_diff(today, self.created_date),
                               ('день', 'дня', 'дней'))
        return res
