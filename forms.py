# coding:utf-8
from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import validators
from wtforms.fields.html5 import EmailField

class RegistrationForm(FlaskForm):

    email = EmailField('email',
                       validators = [validators.InputRequired(), validators.Email()])
    password = PasswordField('password',
                             validators = [validators.InputRequired(), validators.Length(min=8, message='Please choose a password of at least 8 characters')])
    password2 = PasswordField('password2',
                              validators = [validators.InputRequired(), validators.EqualTo('password', message='Passwords must match')])
    submit = SubmitField('submit',[validators.InputRequired()])

class LoginForm(FlaskForm):
    loginemail = EmailField('email',
                       validators = [validators.InputRequired(), validators.Email()])
    loginpassword = PasswordField('password',
                             validators = [validators.InputRequired(message='Password field is required')])
    submit = SubmitField('submit',[validators.InputRequired()])