from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(),length(min=8, max=80)])
    remember = BooleanField('remember me')
    
    
class SignupForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), length(min=4, max=15)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), length(max=50)])
    password = PasswordField('password', validators=[InputRequired(),length(min=8, max=80)])
    
    