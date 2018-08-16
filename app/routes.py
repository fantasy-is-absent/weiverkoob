import os
from app import app, db
from flask import session, render_template, request, flash


from forms.enterForms import LoginForm, SinginForm
from models import Users

#db.create_all()

@app.route("/")
def index():
	return render_template("index.html", user = {"name":"Ivanka"})

@app.route("/login")
def login():
	form = LoginForm(request.form)
	if request.method == "POST":
		name=request.form["name"]
		password=request.form["password"]
		if form.validate():
			# Save the comment here.
			flash('Thanks for registration ' + name)
		else:
			flash('Error: All the form fields are required. ')
	return render_template("login.html", form=form)

@app.route("/singin", methods=["POST", "GET"])
def singin():
	form = SinginForm(request.form)
	if request.method == "POST":
		name=request.form["name"]
		password=request.form["password"]
		email=request.form["email"]
		if form.validate():
			user = Users(name, email)
			print(user)
			db.session.add(user)
			db.session.commit()
			# Save the comment here.
			flash('Thanks for registration ' + name)
		else:
			flash('Error: All the form fields are required. ')
	return render_template("singin.html", form=form)
