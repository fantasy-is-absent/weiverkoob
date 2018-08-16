from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField
from wtforms.validators import Required, Length

class LoginForm(FlaskForm):
	name = TextField('Name:', validators=[Required()])
	email = TextField('Email:', validators=[Required(), Length(min=6, max=35)])
	password = TextField('Password:', validators=[Required(), Length(min=3, max=35)])
	remember_me = BooleanField('remember_me', default = False)