from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class AnswerForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    education = StringField('Образование', validators=[DataRequired()])
    profession = StringField('Профессия', validators=[DataRequired()])
    sex = StringField('Пол', validators=[DataRequired()])
    motivation = StringField('Мотивация', validators=[DataRequired()])
    ready = BooleanField('Готовность остаться на марсе', validators=[DataRequired()])
    submit = SubmitField('Отправить')