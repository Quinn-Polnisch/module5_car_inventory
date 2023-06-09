from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()
    
class UserSignUpForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name')
    submit_button = SubmitField()

class AddCar(FlaskForm):
    make = StringField('Make', validators = [DataRequired()])
    model = StringField('Model', validators = [DataRequired()])
    year = StringField('Year', validators = [DataRequired()])
    submit_button = SubmitField()
