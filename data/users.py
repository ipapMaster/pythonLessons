# Модель таблиц БД - пользователи (users)
# id - уникальный идентификатор пользователя
# name - имя пользователя
# about - краткая информация о пользователе
# email - он же логин (уникальная строка)
# hashed_password - пароль в зашифрованном виде
# creation_date - дата регистрации пользователя

import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String,
                             nullable=True)
    level = sqlalchemy.Column(sqlalchemy.Integer, default=1)
    about = sqlalchemy.Column(sqlalchemy.String,
                              nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True,
                              unique=True,
                              nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String,
                                        nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    # чтобы получать все новости конкретного пользователя
    news = orm.relationship("News", back_populates="user")

    # для нужд отладки и проверки SQL-запросов
    def __repr__(self):
        return f'База {__class__.__name__} -> {self.name} : {self.email}'

    # уровень прав пользователя
    # 1 (по умолчанию) - просто пользователь (редактирование своих и
    # чтение чужих публичных записей)
    # 2 (в идеале, мы пока не делаем) - модератор, ограниченные права
    # на редактирование определённых записей и возможность просмотра всех
    # сообщений (приватных и публичных)
    # 3 - админ - полные права
    def is_admin(self):
        # эта краткая запись означает
        # вернуть True, если level > 1
        return self.level > 1

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
