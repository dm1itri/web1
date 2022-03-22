from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id = StringField('id Астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль Астронавта', validators=[DataRequired()])
    id_cap = StringField('id Капитана', validators=[DataRequired()])
    password_cap = PasswordField('Пароль Капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')