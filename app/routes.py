import os
from flask import session, render_template, request, flash, redirect, g, url_for
from flask_login import login_user, logout_user, current_user, login_required

from app import app, db, lm
from forms.enterForms import LoginForm, SinginForm
from models import Users

db.create_all()

@lm.user_loader
def load_user(user_id):
	return Users.query.get(user_id)


@app.route("/")
def index():
	if current_user:
		return render_template("index.html")
	return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm(request.form)
	if request.method == "GET":
		return render_template("login.html", form=form)
	if form.validate_on_submit():
		user = Users.query.filter_by(name=f"{form.name.data}", 
									password=f"{form.password.data}").first()
		if user:
			user.autentical = True
			login_user(user, remember=True)
			return redirect(url_for("index"))
		else:
			flash('Error: Wrong name or password!')
	return render_template("login.html", form=form)


@app.route("/singin", methods=["POST", "GET"])
def singin():
	form = SinginForm(request.form)
	if request.method == "POST":
		name=request.form["name"]
		password=request.form["password"]
		email=request.form["email"]
		if form.validate():
			user = Users(name, email, password)
			print(user)
			db.session.add(user)
			db.session.commit()
			user.autentical = True
			login_user(user, remember=True)
			flash('Thanks for registration ' + name)
			return redirect(url_for("index"))
		else:
			flash('Error: All the form fields are required. ')
	return render_template("singin.html", form=form)

@app.route("/logout", methods=["GET"])
@login_required
def logout():
	user = current_user
	user.autentical = False
	logout_user()
	return redirect(url_for("login"))