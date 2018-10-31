from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , PasswordField ,BooleanField
from wtforms.validators import DataRequired ,Length ,Email , EqualTo

class RegistraionForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired(), Length(min= 4 , max=100, message='atleast 4 char required')])
    email =StringField('Email' , validators=[DataRequired() , Email()])
    password=PasswordField('Password', validators=[DataRequired() ])
    conform_password= PasswordField('Conform Password', validators=[DataRequired(), EqualTo('password') ])
    submit= SubmitField('Sign up')


class LoginForm(FlaskForm):
    email =StringField('email' , validators=[DataRequired() , Email()])
    password=PasswordField('pwd', validators=[DataRequired() ])
    rememebr = BooleanField('Remember me')
    submit= SubmitField('Sign up')