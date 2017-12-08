import os 
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy import Table, Text, DateTime, Time, Interval
from sqlalchemy import BLOB, Numeric, Boolean, Float


#useful reference:
#	http://docs.sqlalchemy.org/en/rel_1_1/orm/tutorial.html
Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key = True)
	user_name = Column(String(25), nullable=False, unique = True)
	firstname = Column(String(25), nullable=True)
	lastname = Column(String(25), nullable=True)
	email = Column(String(45), nullable=True)
	self_description = Column(String(450), nullable=True)

#ASSOCIATION TABLES (MANY TO MANY RELS - EG FOR ALL THE KEYWORDS)

#1 FOR LIST KEYWORDS (USE THIS TO SEARCH THE LISTS)
list_keywords = Table('list_keywords', Base.metadata,
	Column('list_id', ForeignKey('lists.id'), primary_key=True),
	Column('keyword_id', ForeignKey('l_keywords.id'), primary_key=True))


#Dont forget, there is an association table with 
class List(Base):
	__tablename__ = 'lists'

	id = Column(Integer, primary_key=True)
	name = Column(String(25), nullable=False)
	description = Column(String(250), nullable=True)
	votes = Column(Integer, nullable = True)
	creator = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	# many to many List<->Keyword
	l_keywords = relationship('ListKeyword',secondary=list_keywords,
		back_populates='lists')

class ListKeyword(Base):
	__tablename__ = 'l_keywords'

	id = Column(Integer, primary_key = True)
	keyword = Column(String(50), nullable = False)
	
	# many to many List<->Keyword
	lists = relationship('List', secondary=list_keywords, back_populates='l_keywords')

class HeadingItem(Base):
	__tablename__ = 'heading'

	id = Column(Integer, primary_key=True)
	name = Column(String(25), nullable = False)
	description = Column(String(250), nullable=True)
	entry_data_type = Column(Integer, nullable = False)
	votes = Column(Integer, nullable = True)
	list_id = Column(Integer, ForeignKey('lists.id'))
	lists = relationship(List)
	

class Row(Base):
	__tablename__ = 'row'

	id = Column(Integer, primary_key=True)
	votes = Column(Integer, nullable = True)
	list_id = Column(Integer, ForeignKey('lists.id'))
	lists = relationship(List)
	
# INDIVIDUAL ENTRIES INTO LISTS

# formats can be found at: https://www.w3schools.com/sql/sql_datatypes.asp
#This is for names, titles, nouns, locations, urls, adjectives, etc 
class ShortTextEntry(Base):
	__tablename__ = 'short_text'

	id = Column(Integer, primary_key=True) 
	entry = Column(String(50), nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

# This is for descriptions, long addresses, etc 
class LongTextEntry(Base):
	__tablename__ = 'long_text'

	id = Column(Integer, primary_key=True) 
	entry = Column(String(1000), nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

# This is for birthdays, or any date that needs to be entered 

class DateEntry(Base):
	__tablename__ = 'date'

	id = Column(Integer, primary_key=True) 
	entry = Column(Date, nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)


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

# Boolean
class Bools(Base):
	__tablename__ = 'bools'

	id = Column(Integer, primary_key=True) 
	entry = Column(Boolean, nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

# The time
class TimeEntry(Base):
	__tablename__ = 'time'

	id = Column(Integer, primary_key=True) 
	entry = Column(Time, nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)



# Duration - eg winning time for a race
class Duration(Base):
	__tablename__ = 'duration'

	id = Column(Integer, primary_key=True) 
	entry = Column(Interval, nullable = False)
	votes = Column(Integer, nullable = True)

	heading_id = Column(Integer, ForeignKey('heading.id'))
	heading = relationship(HeadingItem)
	row_id = Column(Integer, ForeignKey('row.id'))
	lists = relationship(Row)

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