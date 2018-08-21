from sqlalchemy import  create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Books(Base):
	
	__tablename__="books"
	
	id = Column(Integer, primary_key = True)
	isbn = Column(String, index = True, unique = True)
	title = Column(String, index = True)
	author = Column(String, index = True)
	year = Column(Integer, index = True)
	
	def __init__(self, isbn, title, author, year):
		self.isbn = isbn
		self.title = title
		self.author = author
		self.year = year


SQLALCHEMY_DATABASE_URI = "postgres://oajlecdrqctkdc:1cfac06095f7c488e34a179da416cbcdc9bc448d839313c9754785caa2b14634@ec2-107-21-236-219.compute-1.amazonaws.com:5432/d73fpsr4h3g909"
session = sessionmaker(bind=create_engine(SQLALCHEMY_DATABASE_URI))()
file = "books.csv"

for line in open(file):
	isbn,*title, author, year = line.split(",")
	book = Books(isbn, ",".join(title), author, int(year[:-1]))
	session.add(book)
	session.commit()