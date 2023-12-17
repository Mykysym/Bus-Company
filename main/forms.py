from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from main.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Логін', validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField('Номер телефону', validators=[DataRequired(), Length(min=10, max=13)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Підтвердити пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зареєструватись')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Логін зайнято, оберіть інший')

    def validate_phone(self, phone):

        user = User.query.filter_by(phone=phone.data).first()
        if user:
            raise ValidationError('Такий номер вже зареєстровано, оберіть інший')

    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Такий номер вже зареєстровано, оберіть інший')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Номер телефону', validators=[DataRequired(), Length(min=10, max=13)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField("Запам'ятати")
    submit = SubmitField('Увійти')


class SearchForm(FlaskForm):
    departure = StringField('Пункт відправлення', validators=[DataRequired(), Length(min=2, max=50)])
    arrival = StringField("Пункт призначення", validators=[DataRequired(), Length(min=2, max=50)])
    date = DateField("Дата відпрвлення", validators=[DataRequired()])
    submit = SubmitField('Пошук')

