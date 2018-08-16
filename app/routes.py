import os
from app import app
from flask import session, render_template, request, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from forms.loginForms import LoginForm

DATABASE_URL = "postgres://kmkhjzcckmmadd:0ccdd910e2a2984001d63285cb5c2e60d1bcd5fdf0f6aa9147836066404f4aaf@ec2-54-217-235-16.eu-west-1.compute.amazonaws.com:5432/d63tuv25mgl2nv"
# Check for environment variable
#if not os.getenv(DATABASE_URL):
#   raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
	return render_template("index.html", user = {"name":"Ivanka"})

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/singin", methods=["POST", "GET"])
def singin():
	form = LoginForm(request.form)
	if request.method == "POST":
		name=request.form["name"]
		password=request.form["password"]
		email=request.form["email"]
		print (name, " ", email, " ", password)
		if form.validate():
			# Save the comment here.
			flash('Thanks for registration ' + name)
		else:
			flash('Error: All the form fields are required. ')
	return render_template("singin.html", form=form, providers = app.config['OPENID_PROVIDERS'])										
