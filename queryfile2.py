from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, list_keywords, List, ListKeyword, HeadingItem
from database_setup import Row, TextEntry, DateEntry, DateTimeEntry, IntegerEntry 
from database_setup import TrueFalse, TimeEntry, Duration, TwoDecimal, LargeDecimal

engine = create_engine('postgresql+psycopg2://catalog:db-password@localhost/supalist1')
Base.metadata.bind = engine 
DBSession = sessionmaker(bind = engine)
session = DBSession()

session.rollback()

print "now, its rolled back?"
'''

kw = session.query(List).filter(List.l_keywords.any(keyword="richest")).all()
for k in kw: 
	print k.name   
	'''
