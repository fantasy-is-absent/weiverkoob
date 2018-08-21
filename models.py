from app import db

class Users(db.Model):

	__tablename__ = "users"
	
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(35), index = True, unique = True)
	email = db.Column(db.String(35), index = True)
	password = db.Column(db.String(600), index = True)
	authenticated = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return f"<User {self.name}>"

	def __init__(self, name=None, email=None, password=None, authenticated=True):
		self.name = name
		self.email = email
		self.password = password
		self.authenticated = authenticated
	
	def is_active(self):
		return True

	def get_id(self):
		return self.id
	
	def is_authenticated(self):
		return self.authenticated

class Books(db.Model):
	
	__tablename__="books"
	
	id = db.Column(db.Integer, primary_key = True)
	isbn = db.Column(db.String, index = True, unique = True)
	title = db.Column(db.String, index = True)
	author = db.Column(db.String, index = True)
	year = db.Column(db.Integer, index = True)

	def __init__(self, isbn, title, author, year):
		self.isbn = isbn
		self.title = title
		self.author = author
		self.year = year