from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

DATABASE_URL = "postgres://kmkhjzcckmmadd:0ccdd910e2a2984001d63285cb5c2e60d1bcd5fdf0f6aa9147836066404f4aaf@ec2-54-217-235-16.eu-west-1.compute.amazonaws.com:5432/d63tuv25mgl2nv"
db = SQLAlchemy(app)


from app import routes