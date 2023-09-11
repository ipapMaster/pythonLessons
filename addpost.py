from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class NewPost(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired('Заголовок обязателен')])
    content = StringField('Контент', validators=[DataRequired('Введите контент')])
    submit = SubmitField('Добавить')
