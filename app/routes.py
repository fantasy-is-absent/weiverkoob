import os
from app import app
from flask import session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#DATABASE_URL = "postgres://kmkhjzcckmmadd:0ccdd910e2a2984001d63285cb5c2e60d1bcd5fdf0f6aa9147836066404f4aaf@ec2-54-217-235-16.eu-west-1.compute.amazonaws.com:5432/d63tuv25mgl2nv"
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"										
