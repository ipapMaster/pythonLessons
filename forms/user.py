from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email


# Для валидации E-mail средствами скрипта
# необходимо доустановить модуль
# pip install email_validator


class RegisterForm(FlaskForm):
    email = EmailField('Почта',
                       validators=[DataRequired('E-mail обязателен'), Email(message='Не корректный формат почты')])
    password = PasswordField('Пароль', validators=[DataRequired('Вы не ввели пароль'),
                                                   Length(min=6, message='Пароль слишком короткий')])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired('Введите подтверждение пароля')])
    name = StringField('Имя пользователя',
                       validators=[DataRequired('Укажите своё имя'),
                                   Length(min=3,
                                          max=25,
                                          message='Имя пользователя должно быть от 3 до 25 символов')])
    about = TextAreaField('Немного о себе')
    submit = SubmitField('Зарегистрироваться')
