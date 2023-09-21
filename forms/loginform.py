from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Логин (E-mail)', validators=[DataRequired('Это обязательное поле'),
                                                         Email('Некорректный формат E-mail')])
    password = PasswordField('Пароль', validators=[DataRequired('Пароль обязателен')])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
