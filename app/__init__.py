from flask import Flask
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

DATABASE_URL = "postgres://kmkhjzcckmmadd:0ccdd910e2a2984001d63285cb5c2e60d1bcd5fdf0f6aa9147836066404f4aaf@ec2-54-217-235-16.eu-west-1.compute.amazonaws.com:5432/d63tuv25mgl2nv"
#engine = create_engine(DATABASE_URL)
#db = scoped_session(sessionmaker(bind=engine))
#Session(app)
db = SQLAlchemy(app)

from app import routes