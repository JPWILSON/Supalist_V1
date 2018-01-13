import os 
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy import Table, Text, DateTime, Time, Interval
from sqlalchemy import BLOB, Numeric, Boolean, Float
from sqlalchemy.dialects import postgresql


#useful reference:
#	http://docs.sqlalchemy.org/en/rel_1_1/orm/tutorial.html
Base = declarative_base()
'''
class User(Base):
	__tablename__ = 'usery'

	id = Column(Integer, primary_key = True)
	user_name = Column(String(25), nullable=False, unique = True)
	firstname = Column(String(25), nullable=True)
	lastname = Column(String(25), nullable=True)
	email = Column(String(45), nullable=False)
	picture = Column(String(250)) 
	self_description = Column(String(450), nullable=True)

	@property
	def serialize(self):
		#Returns object data in easily serializable format
		return {
			'id' : self.id,
			'user_name' : self.user_name,
			'firstname' : self.firstname,
			'lastname' : self.lastname,
			'email' : self.email,
			'picture' : self.picture,
			'description' : self.description,
		}
'''
class User(Base):
	__tablename__ = 'usery'

	id = Column(Integer, primary_key = True)
	user_name = Column(Text, nullable=False, unique = True)
	firstname = Column(Text, nullable=True)
	lastname = Column(Text, nullable=True)
	email = Column(Text, nullable=False)
	picture = Column(Text) 
	self_description = Column(Text, nullable=True)

	@property
	def serialize(self):
		#Returns object data in easily serializable format
		return {
			'id' : self.id,
			'user_name' : self.user_name,
			'firstname' : self.firstname,
			'lastname' : self.lastname,
			'email' : self.email,
			'picture' : self.picture,
			'description' : self.description,
		}

#ASSOCIATION TABLES (MANY TO MANY RELS - EG FOR ALL THE KEYWORDS)

#1 FOR LIST KEYWORDS (USE THIS TO SEARCH THE LISTS)
list_keywords = Table('list_keywords', Base.metadata,
	Column('list_id', ForeignKey('lists.id'), primary_key=True),
	Column('keyword_id', ForeignKey('l_keywords.id'), primary_key=True))

# From :  http://bitwiser.in/2015/09/09/add-google-login-in-flask.html
"""
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=False)
    tokens = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
"""
# Experimenting, not actually part of the code



#Dont forget, there is an association table with 
class List(Base):
	__tablename__ = 'lists'

	id = Column(Integer, primary_key=True)
	name = Column(Text, nullable=False)
	description = Column(Text, nullable=True)
	votes = Column(Integer, nullable = True)
	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)

	# many to many List<->Keyword
	l_keywords = relationship('ListKeyword',secondary=list_keywords,
		back_populates='lists')

	@property
	def serialize(self):
		#Returns object data in easily serializable format
		return {
			'id' : self.id,
			'name' : self.name,
			'description' : self.description,
			'votes' : self.votes,
		}

class ListKeyword(Base):
	__tablename__ = 'l_keywords'

	id = Column(Integer, primary_key = True)
	keyword = Column(Text, nullable = False)
	
	# many to many List<->Keyword
	lists = relationship('List', secondary=list_keywords, back_populates='l_keywords')

class HeadingItem(Base):
	__tablename__ = 'heading'

	id = Column(Integer, primary_key=True)
	name = Column(Text, nullable = False)
	description = Column(Text, nullable=True)
	entry_data_type = Column(Integer, nullable = False)
	votes = Column(Integer, nullable = True)
	list_id = Column(Integer, ForeignKey('lists.id'))
	lists = relationship(List)

	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)
	

class Row(Base):
	__tablename__ = 'row'

	id = Column(Integer, primary_key=True)
	votes = Column(Integer, nullable = True)
	list_id = Column(Integer, ForeignKey('lists.id'))
	lists = relationship(List)

	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)
	
# INDIVIDUAL ENTRIES INTO LISTS

# formats can be found at: https://www.w3schools.com/sql/sql_datatypes.asp
#This is for names, titles, nouns, locations, urls, adjectives, etc 
class TextEntry(Base):
	__tablename__ = 'short_text'

	id = Column(Integer, primary_key=True) 
	entry = Column(Text, nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)


class IntegerEntry(Base):
	__tablename__ = 'integer'

	id = Column(Integer, primary_key=True) 
	entry = Column(Integer, nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)

# This is for descriptions, long addresses, etc 
"""
class LongTextEntry(Base):
	__tablename__ = 'long_text'

	id = Column(Integer, primary_key=True) 
	entry = Column(Text, nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)"""

# This is for birthdays, or any date that needs to be entered 

class DateEntry(Base):
	__tablename__ = 'date'

	id = Column(Integer, primary_key=True) 
	entry = Column(Date(), nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)


# Precise dates, that include the time
class DateTimeEntry(Base):
	__tablename__ = 'date_time'

	id = Column(Integer, primary_key=True) 
	entry = Column(DateTime(timezone=False), nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)

# Boolean
class TrueFalse(Base):
	__tablename__ = 'bools'

	id = Column(Integer, primary_key=True) 
	entry = Column(Boolean, nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)

# The time
class TimeEntry(Base):
	__tablename__ = 'time'

	id = Column(Integer, primary_key=True) 
	entry = Column(Time(), nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)



# Duration - eg winning time for a race
class Duration(Base):
	__tablename__ = 'duration'

	id = Column(Integer, primary_key=True) 
	entry = Column(Interval(), nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)

# 2 decimal places, currency 
class TwoDecimal(Base):
	__tablename__ = 'currency'

	id = Column(Integer, primary_key=True) 
	entry = Column(Numeric(precision=15, scale=2), nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)


# For any precision number 
class LargeDecimal(Base):
	__tablename__ = 'precision_num'

	id = Column(Integer, primary_key=True) 
	entry = Column(Float(25), nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

	user_id = Column(Integer, ForeignKey('usery.id'))
	user = relationship(User)

# Blobs for bits, like images? 
"""class Blobs(Base):
	__tablename__ = 'images'

	id = Column(Integer, primary_key=True) 
	entry = Column(BLOB, nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)"""


# dialect+driver://username:password@host:port/database
# engine = create_engine('postgresql+psycopg2://jean:wils@localhost/supalist')
#engine = create_engine('postgresql+psycopg2://myapp:dbpass@localhost:15432/myapp')

engine = create_engine('postgresql+psycopg2://catalog:db-password@localhost/supalist1')
Base.metadata.create_all(engine)


"""
class (Base):
	__tablename__ = 'heading'

	id = Column(Integer, primary_key=True)

class (Base):
	__tablename__ = 'heading'

	id = Column(Integer, primary_key=True)

	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)
	= Column(Integer, nullable = True)





	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)
	= Column(String(250), nullable=True)


"""