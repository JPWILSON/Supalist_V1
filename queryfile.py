from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, list_keywords, List, ListKeyword, HeadingItem
from database_setup import Row, TextEntry, DateEntry, DateTimeEntry, IntegerEntry 
from database_setup import TrueFalse, TimeEntry, Duration, TwoDecimal, LargeDecimal

engine = create_engine('postgresql+psycopg2://catalog:db-password@localhost/supalist1')
Base.metadata.bind = engine 
DBSession = sessionmaker(bind = engine)
session = DBSession()

print"About to start"
arr = [1,'gff', 'sdf','sd', 4,5,6,90]
for i in range(0, len(arr)):
	print i, arr[i]
print "Done", len(arr)

"""

li = session.query(List).all()


print "li is a: ", type(li), "\n"

for table in li:
	print table.name, "\n"
	print table.description, "\n"
	print table.id, "\n"


li_headings = {}

for table in li:
 li_headings[table.name] = session.query(HeadingItem).filter_by(list_id = table.id).all()


for i in li_headings:
	print i, "\n"
	for item in li_headings[i]:
		print "heading name: ",item.name, "\n"



print "DONE!"


li = session.query(List).all()
li3 = li[0]
#rows = session.query(Row).filter_by(list_id = li.id).order_by(asc(Row.id))
print "list 3 id: ", li3.id 

heading_items = session.query(HeadingItem).filter_by(list_id = li3.id).order_by(HeadingItem.id.asc()).all()
print "Is heading items a list?  ", type(heading_items)
for h in heading_items:
	print "Heading items: ", type(h), h.name, h.id, "data type: ", h.entry_data_type 



rows = session.query(Row).filter_by(list_id = li3.id).order_by(Row.id.asc()).all()
for row in rows:
	print row.id, "list id: ", row.list_id

print "DONE now!"
row_entries = {}

for row in rows:
	#row_entries[row.id] = session.query(ShortTextEntry, LongTextEntry, DateEntry, DateTimeEntry, Bools, TimeEntry, Duration, TwoDecimal, LargeDecimal).filter_by(row_id = row.id)
	row_entries[row.id] = session.query(ShortTextEntry).filter_by(row_id = row.id).order_by(ShortTextEntry.heading_id).all()
	for i in (session.query(LongTextEntry).filter_by(row_id = row.id).all()):
		row_entries[row.id].append(i)
	for i in (session.query(DateEntry).filter_by(row_id = row.id).all()):
		row_entries[row.id].append(i)
	for i in (session.query(DateTimeEntry).filter_by(row_id = row.id).all()):
			row_entries[row.id].append(i)
	for i in (session.query(Bools).filter_by(row_id = row.id).all()):
			row_entries[row.id].append(i)
	for i in (session.query(TimeEntry).filter_by(row_id = row.id).all()):
			row_entries[row.id].append(i)
	for i in (session.query(Duration).filter_by(row_id = row.id).all()):
			row_entries[row.id].append(i)
	for i in (session.query(TwoDecimal).filter_by(row_id = row.id).all()):
			row_entries[row.id].append(i)
	for i in (session.query(LargeDecimal).filter_by(row_id = row.id).all()):
			row_entries[row.id].append(i)

	(row_entries[row.id]).sort(key=lambda x: int(x.heading_id))

	#row_entries[row.id] = session.query(ShortTextEntry).join(LongTextEntry).join(DateEntry).join(DateTimeEntry).join(Bools).join(TimeEntry).join(Duration).join(TwoDecimal).join(LargeDecimal).filter_by(row_id = row.id)

for val in row_entries:
		print val, "----------", type(row_entries[val])
		count = 0 
		for e in row_entries[val]:
			#print "Entry: ", e.entry, "-----", e.row_id, e.heading_id, "\n"
			print "Row id: ", e.row_id, "  Heading id: ", e.heading_id, "  Entry: ", e.entry 
			count += 1
		print "Count: ", count, "\n"

print "Complet"

#.order_by(heading.id.asc())

li_of_dtypes = ['ShortTextEntry','LongTextEntry','DateEntry','DateTimeEntry','Bools','TimeEntry','Duration','TwoDecimal','LargeDecimal']
data_types ={}
for i in range(1,10):
	data_types[i] = li_of_dtypes[i-1]


for i in range(1,(len(data_types)+1)):
	print data_types[i]


for i in range(1, len(heading_items)+1):
	print data_types[heading_items[i-1].entry_data_type], "WOHHAHAHA"
print len(heading_items)
print "Now done!"

"""