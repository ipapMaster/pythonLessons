from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired('Это обязательное поле')])
    password = PasswordField('Пароль', validators=[DataRequired('Пароль обязателен')])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
