import os
from flask import session, render_template, request, flash, redirect, g, url_for, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy import or_

from app import app, db, lm, bcrypt
from forms.enterForms import LoginForm, SinginForm
from models import Users, Books, Review

db.create_all()

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),
				'favicon.ico', mimetype='image/vnd.microsoft.icon')

@lm.user_loader
def load_user(user_id):
	return Users.query.get(user_id)

@app.route("/", methods = ["GET", "POST"])
@login_required
def index():
	if request.method == "GET":
		return render_template("index.html")
	search = request.form["search"]
	books_search = Books.query.filter(or_(Books.isbn.like(f"%{search}%"), 
									Books.title.like(f"%{search}%"), 
									Books.author.like(f"%{search}%"))).limit(12).all()
	if not books_search:
		flash("Error: Nothing found!")
	return render_template("index.html", books_search = books_search)


@app.route("/<string:isnbBook>", methods = ["GET", "POST"])
@login_required
def viewBook(isnbBook):
	book = Books.query.filter_by(isbn = isnbBook).first()
	#if request.method == "POST":
		#review = Review(current_user.id, book.id, request.form["review"])
		#db.session.add(review)
		#db.session.commit()
	reviews = db.session.query(Review, Users)\
						.filter(Review.book_id == book.id)\
						.filter(Review.user_id == Users.id)\
						.all()
	return render_template("viewBook.html", 
							book = book,
							reviews = reviews)

@app.route("/login", methods = ["GET", "POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("index"))
	form = LoginForm(request.form)
	if request.method == "GET":
		return render_template("login.html", form = form)
	if form.validate_on_submit():
		try:
			user = Users.query.filter_by(name = f"{form.name.data}").first()
			if bcrypt.check_password_hash(user.password, form.password.data):
				user.autentical = True
				login_user(user, remember = True)
				return redirect(url_for("index"))
			else:
				flash("Error: Wrong password!")
		except:
			flash("Error: Wrong name!")
	return render_template("login.html", form = form)


@app.route("/singin", methods = ["POST", "GET"])
def singin():
	if current_user.is_authenticated:
		return redirect(url_for("index"))
	form = SinginForm(request.form)
	if request.method == "POST":
		name = request.form["name"]
		password = request.form["password"]
		email = request.form["email"]
		if form.validate():
			user = Users(name, email, bcrypt.generate_password_hash(password).decode("utf-8"))
			db.session.add(user)
			db.session.commit()
			login_user(user, remember = True)
			flash('Thanks for registration ' + name)
			return redirect(url_for("index"))
		else:
			flash('Error: All the form fields are required. ')
	return render_template("singin.html", form = form)

@app.route("/logout", methods = ["GET"])
@login_required
def logout():
	user = current_user
	user.autentical = False
	logout_user()
	return redirect(url_for("login"))