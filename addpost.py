from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# ORM - Object Relational Model (объектно-реляционное отображение)
# MVC - Model - View - Control
# pip install sqlalchemy
class NewPost(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired('Заголовок обязателен')])
    content = TextAreaField('Контент', validators=[DataRequired('Введите контент')])
    submit = SubmitField('Добавить')
