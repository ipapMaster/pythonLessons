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


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String,
                             nullable=True)
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
