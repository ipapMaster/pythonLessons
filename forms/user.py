from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired('E-mail обязателен'),
                                            Email(message='Не корректный формат почты')])
    password = PasswordField('Пароль', validators=[DataRequired('Вы не ввели пароль'),
                                                   Length(min=6, message='Пароль слишком короткий')])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired('Введите подтверждение пароля')])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField('Немного о себе')
    submit = SubmitField('Зарегистрироваться')
