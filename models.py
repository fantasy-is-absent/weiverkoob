from app import db

class Users(db.Model):

	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)

	def __repr__(self):
		return f"<User {self.name}>"

	def __init__(self, name=None, email=None):
		self.name = name
		self.email = email