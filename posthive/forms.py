#!/usr/bin/env python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, equal_to

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
            validators=[DataRequired(), equal_to('Password')])
    submit = SubmitField('Sign Up')
    
class LoginForm(FlaskForm):
    email = StringField('Email', 
            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')