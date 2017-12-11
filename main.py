from flask import Flask, render_template, request, url_for, redirect, flash, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, list_keywords, List, ListKeyword, HeadingItem
from database_setup import Row, ShortTextEntry, LongTextEntry, DateEntry, DateTimeEntry 
from database_setup import Bools, TimeEntry, Duration, TwoDecimal, LargeDecimal

engine = create_engine('postgresql+psycopg2://catalog:db-password@localhost/supalist1')
Base.metadata.bind = engine 
DBSession = sessionmaker(bind = engine)
session = DBSession()


app = Flask(__name__)

user1 = session.query(User).first()
#This is for when I need to access the different data types: 
li_of_dtypes = [ShortTextEntry,LongTextEntry,DateEntry,DateTimeEntry,Bools,TimeEntry,Duration,TwoDecimal,LargeDecimal]
data_types ={}
for i in range(0,9):
	data_types[i] = li_of_dtypes[i]
#This is for when I need to access the TEXT (strings) of the different data types: 
li_of_dtypes_str = ["Short Text","Long Text","Date","Date & Time","True/False","Time","Duration","Two Decimal","Large Decimal"]
data_types_str ={}
for i in range(0,9):
	data_types_str[i] = li_of_dtypes_str[i]

@app.route('/')
@app.route('/home/')
def Home():
	#return "headings of all/ top lists, or of the main menu options"
	all_lists = session.query(List).all()
	lists_and_headings = {}
	for li in all_lists:
		lists_and_headings[li] = session.query(HeadingItem).filter_by(list_id = li.id).all()
	return render_template('homepage.html', all_lists = all_lists, lists_and_headings = lists_and_headings)

@app.route('/new/', methods = ['GET', 'POST'])
def NewList():
	if request.method == 'POST':
		newli = List(name = request.form['namer'], description = request.form['desc'], votes = 0, user=user1)
		kw1 = request.form['kw1']
		if kw1 != None:
			newli.l_keywords.append(ListKeyword(keyword = kw1))
		
		kw2 = request.form['kw2']
		if kw2 != None:
			newli.l_keywords.append(ListKeyword(keyword = kw2))

		kw3 = request.form['kw3']
		if kw3 != None:
			newli.l_keywords.append(ListKeyword(keyword = kw3))
		session.add(newli)
		session.commit()
		return redirect(url_for('Home'))
	else:
		return render_template('new_list.html')

@app.route('/<int:list_id>/edit/', methods = ['GET', 'POST'])
def EditList(list_id):
	li_2_edit = session.query(List).filter_by(id = list_id).one()
	keyword_list = []
	for i in li_2_edit.l_keywords:
		keyword_list.append(i)
	if request.method == 'POST':
		li_2_edit.name = request.form['namer']
		li_2_edit.description = request.form['desc']
		kw1, kw2 = request.form['kw1'], request.form['kw2']
		if kw1 != None and kw1 not in li_2_edit.l_keywords:
			li_2_edit.l_keywords.append(ListKeyword(keyword = kw1))
		if kw2 != None and kw2 not in li_2_edit.l_keywords:
			li_2_edit.l_keywords.append(ListKeyword(keyword = kw2))
		session.add(li_2_edit)
		session.commit()
		return redirect(url_for('QueryList', list_id = li_2_edit.id))
	else:
		return render_template('edit_list.html', list_id = list_id, lname=li_2_edit, keyword_list=keyword_list)


@app.route('/<int:list_id>/delete/', methods = ['GET', 'POST'])
def DeleteList(list_id):
	li_2_del = session.query(List).filter_by(id = list_id).one()
	headings2del = session.query(HeadingItem).filter_by(list_id = list_id).all()
	rows_2_del = session.query(Row).filter_by(list_id = list_id).order_by(Row.id.asc()).all()
	print type(rows_2_del), len(rows_2_del), "row id: ", rows_2_del[0].id
	if request.method == 'POST':
		#Delete all keywords associated to this list:
		li_2_del.l_keywords = []
		#First, delete the list
		
		#Second, delete the heading items


		#Third, Delete every single entry: 
		for row in rows_2_del:
			e_2_del1 = session.query(ShortTextEntry).filter_by(row_id = row.id).all()
			if len(e_2_del1) > 0:
				for w in e_2_del1:
					session.delete(w)
					session.commit()

			e_2_del2 = session.query(LongTextEntry).filter_by(row_id = row.id).all()
			#print "This is the e2_del2: ", len(e_2_del2), type(e_2_del2), type(e_2_del2[0]),e_2_del2[0], e_2_del2[0].entry
			if len(e_2_del2) > 0:
				for w in e_2_del2:
					session.delete(w)
					session.commit()

			e_2_del3 = session.query(DateEntry).filter_by(row_id = row.id).all()
			if len(e_2_del3) > 0:
				for w in e_2_del3:
					session.delete(w)
					session.commit()

			e_2_del4 = session.query(Bools).filter_by(row_id = row.id).all()
			if len(e_2_del4) > 0:
				for w in e_2_del4:
					session.delete(w)
					session.commit()

			e_2_del5 = session.query(TimeEntry).filter_by(row_id = row.id).all()
			if len(e_2_del5) > 0:
				for w in e_2_del5:
					session.delete(w)
					session.commit()

			e_2_del6 = session.query(Duration).filter_by(row_id = row.id).all()
			if len(e_2_del6) > 0:
				for w in e_2_del6:
					session.delete(w)
					session.commit()

			e_2_del7 = session.query(TwoDecimal).filter_by(row_id = row.id).all()
			if len(e_2_del7) > 0:
				for w in e_2_del7:
					session.delete(w)
					session.commit()

			e_2_del8 = session.query(LargeDecimal).filter_by(row_id = row.id).all()
			if len(e_2_del8) > 0:
				for w in e_2_del8:
					session.delete(w)
					session.commit()

			e_2_del9 = session.query(DateTimeEntry).filter_by(row_id = row.id).all()
			if len(e_2_del9) > 0:
				for w in e_2_del9:
					session.delete(w)
					session.commit()

			#Lastly, delete every row
		for heading in headings2del:
			session.delete(heading)
			session.commit()

		for row in rows_2_del:
			session.delete(row)
			session.commit()

		session.delete(li_2_del)
		session.commit()


		return redirect(url_for('Home'))
	else:
		return render_template('delete_list.html', li_2_del = li_2_del, list_id = list_id, 
			headings2del = headings2del, no_rows_2_del=len(rows_2_del))


	return "Are you sure you want to delete this list? (only certain privileges will allow you to delete a list? - or never?) list{}".format(list_id)

@app.route('/<int:list_id>/')
def QueryList(list_id):
	list_to_view = session.query(List).filter_by(id = list_id).first()
	#heading_items = session.query(HeadingItem).filter_by(list_id = list_to_view.id).order_by(asc(HeadingItem.id))
	heading_items = session.query(HeadingItem).filter_by(list_id = list_to_view.id).order_by(HeadingItem.id.asc())
	rows = session.query(Row).filter_by(list_id = list_to_view.id).order_by(Row.id.asc())
	row_entries = {}

	# Need to collect data entries for each of the different types of entries that are available
	for row in rows:
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


	return render_template('view.html', list = list_to_view, h_items = heading_items, rows = rows, 
		row_entries = row_entries, lid = list_id, data_types_str = data_types_str)
	#return "A single list that you can view or inspect/query (this should be the most important\
	#feature, and \n it is from here that you would add to the list (edit). list{}".format(list_id)

@app.route('/<int:list_id>/new_col/', methods = ['GET', 'POST'])
def AddColumn(list_id):
	list_to_add_to = session.query(List).filter_by(id=list_id).one()
	if request.method == 'POST':
		newhi = HeadingItem(name=request.form['namer'], description=request.form['desc'], entry_data_type = request.form['data_type'], votes=0, lists= list_to_add_to)
		session.add(newhi)
		session.commit()
		return redirect(url_for('QueryList', list_id = list_id))
	else:
		return render_template('add_column.html', list_id = list_id, lname = list_to_add_to.name)
		"""
	kw1 = request.form['kw1']
	if kw1 != None:
		newli.l_keywords.append(ListKeyword(keyword = kw1))
	
	kw2 = request.form['kw2']
	if kw2 != None:
		newli.l_keywords.append(ListKeyword(keyword = kw2))

	kw3 = request.form['kw3']
	if kw3 != None:
		newli.l_keywords.append(ListKeyword(keyword = kw3))"""
	#return "Add a new column (and therefore increase the usefulness of your list{}".format(list_id)

@app.route('/<int:list_id>/edit_col/', methods = ['GET', 'POST'])
def EditColumn(list_id):
	col_id = request.form.get('id_of_col')
	return render_template('edit_column.html', list_id = list_id, col_id = col_id)
	"""return "Edit a column (and therefore increase the usefulness of your list. \n \
	Ordinarily this should be to modify or add to the descriptions on this column, or to make another column more useful. \
	That is, \n when there are two columns doing the job that one column previosly used to do. (Eg. Address becomes:\
	GPS co-ords in one column, and Residential addresss in another column list{}, col{})".format(list_id, col_id)"""

@app.route('/<int:list_id>/<int:col_id>/delete_col/')
def DeleteColumn(list_id, col_id):
	return "Delete this column for list number: {}, column id: {}".format(list_id, col_id)

@app.route('/<int:list_id>/new_row/', methods = ['GET', 'POST'])
def AddRow(list_id):
	list_to_add_to = session.query(List).filter_by(id=list_id).one()
	heading_items = session.query(HeadingItem).filter_by(list_id = list_id).order_by(HeadingItem.id.asc()).all()
	if request.method == 'POST':

		new_row = Row(votes = 0, lists = list_to_add_to)
		session.add(new_row)
		session.commit()
		print "new row added"

		for i in range(1, len(heading_items)+1):
			print i, data_types[heading_items[i-1].entry_data_type], "then this", request.form["name_{}".format(i)]
			form_val = request.form["name_{}".format(i)]
			stri = data_types[heading_items[i-1].entry_data_type]
			print type(stri), "is a type..."
			e1 = stri(entry=form_val, votes=0, heading = heading_items[i-1] , lists =new_row)
			session.add(e1)
			session.commit()
		return redirect(url_for('QueryList', list_id = list_id))
	else:
		return render_template('add_row.html', list_id = list_id, h_items = heading_items, list = list_to_add_to)
	#return "Add a new row to your list. That is, a new entry (and therefore increase the usefulness of your list with id: {}). ".format(list_id)

@app.route('/<int:list_id>/<int:row_id>/edit_row/')
def EditRow(list_id, row_id):
	heading_items = [ {'name':'First Name','description':'A person\'s first name','adjective1':'First Name','id' :'1','list_id' :'1'}, 
		{'name':'Middle Name','description':'A person\'s middle name','adjective1':'Middle Name','id' :'2','list_id' :'1'},
		{'name':'Last Name','description':'A person\'s last name','adjective1':'Last Name','id' :'3','list_id' :'1'},
		{'name':'Net Worth', 'description':'Value of all personal assets','adjective1':'Richest','id' :'4','list_id' :'1'},
		{'name':'Common Name', 'description':'What this building is known as ','adjective1':'name','id' :'5','list_id' :'2'},
		{'name':'Make & Model', 'description':'What is this car known as ','adjective1':'name','id' :'6','list_id' :'3'} ]
	#sorted_heading_items = sorted(heading_items, key = itemgetter('id'))
	list32 = {'name': 'UNICORN LISTINGS', 'id': '1', 'description': 'A list describing companies valued over $1bn', 'unique_instance':'True', 'votes':'0'}
	return render_template('edit_row.html', list_id = list_id, h_items = heading_items[:4], list = list32)
	#return "Edit a row from list id: list{}, with a row id of: row{})".format(list_id, row_id)

@app.route('/<int:list_id>/<int:row_id>/delete_row/')
def DeleteRow(list_id, row_id):
	return "Delete this row for list number: {}, row id: {}".format(list_id, row_id)




#____LIST COMMENTS______

@app.route('/<int:list_id>/new_comment/')
def NewListComment(list_id):
	return render_template('new_comment.html', list_id = list_id)
	#return "Page for making a new comment for the list: {}.".format(list_id)

@app.route('/<int:list_id>/comments/')
def ListComments(list_id):
	return "A list of all the comments for the list: {}.\n \
	There should be: VIEW|COMMENT|EDIT|DELETE buttons for each of the entries".format(list_id)

#@app.route('/<int:list_id>/<int:comment_id>/')
@app.route('/<int:list_id>/<int:comment_id>/view_list_comment/')
def ViewListComment(list_id,comment_id):
	return "View a single comment with buttons on here for when you want to edit and or delete this comment from list id:{}, comment id:{}".format(list_id, comment_id)

@app.route('/<int:list_id>/<int:comment_id>/edit_list_comment')
def EditListComment(list_id,comment_id):
	return "Page for editing a comment for the list: list{}, comment:{}".format(list_id, comment_id)

@app.route('/<int:list_id>/<int:comment_id>/delete_list_comment')
def DeleteListComment(list_id,comment_id):
	return "Page for deleting a comment for the list: list{}, comment:{}".format(list_id, comment_id)


#____HEADING COMMENTS______

@app.route('/<int:col_id>/new_comment/')
def NewColumnComment(col_id):
	return "Page for making a new comment for the col: {}.".format(col_id)

@app.route('/<int:col_id>/comments/')
def ColumnComments(col_id):
	return "A list of all the comments for the col: {}.\n \
	There should be: VIEW|COMMENT|EDIT|DELETE buttons for each of the entries".format(col_id)

#@app.route('/<int:col_id>/<int:comment_id>/')
@app.route('/<int:col_id>/<int:comment_id>/view_col_comment/')
def ViewColumnComment(col_id,comment_id):
	return "View a single comment with buttons on here for when you want to edit and or delete this comment from col id:{}, comment id:{}".format(col_id, comment_id)

@app.route('/<int:col_id>/<int:comment_id>/edit_col_comment')
def EditColumnComment(col_id,comment_id):
	return "Page for editing a comment for the col: col{}, comment:{}".format(col_id, comment_id)

@app.route('/<int:col_id>/<int:comment_id>/delete_col_comment')
def DeleteColumnComment(col_id,comment_id):
	return "Page for deleting a comment for the col: col{}, comment:{}".format(col_id, comment_id)



#____ROW COMMENTS______

@app.route('/<int:row_id>/new_comment/')
def NewRowComment(row_id):
	return "Page for making a new comment for the row: {}.".format(row_id)

@app.route('/<int:row_id>/comments/')
def RowComments(row_id):
	return "A list of all the comments for the row with VIEW|COMMENT|EDIT|DELETE buttons for each of the comments for this row with id: {}.".format(row_id)

#@app.route('/<int:row_id>/<int:comment_id>/')
@app.route('/<int:row_id>/<int:comment_id>/view_row_comment/')
def ViewRowComment(row_id,comment_id):
	return "View a single comment with buttons on here for when you want to edit and or delete this comment from row id:{}, comment id:{}".format(row_id, comment_id)

@app.route('/<int:row_id>/<int:comment_id>/edit_row_comment')
def EditRowComment(row_id,comment_id):
	return "Page for editing a comment for the row: row{}, comment:{}".format(row_id, comment_id)

@app.route('/<int:row_id>/<int:comment_id>/delete_row_comment')
def DeleteRowComment(row_id,comment_id):
	return "Page for deleting a comment for the row: row{}, comment:{}".format(row_id, comment_id)


#____ITEM COMMENTS______

@app.route('/<int:row_id>/<int:col_id>/new_comment/')
def NewItemComment(row_id, col_id):
	return "Page for making a new comment for the item: Row{}, Col{}.".format(row_id, col_id)

@app.route('/<int:row_id>/<int:col_id>/comments/')
def ItemComments(row_id, col_id):
	return "A list of all the comments for the item with VIEW|COMMENT|EDIT|DELETE buttons for each of the comments for this item: row{}, col{}".format(row_id, col_id)

#@app.route('/<int:row_id>/<int:col_id>/<int:comment_id>/')
@app.route('/<int:row_id>/<int:col_id>/<int:comment_id>/view_row_comment/')
def ViewItemComment(row_id,col_id, comment_id):
	return "View a single comment with buttons on here for when you want to edit and or delete this comment from row id:{}, col_id: {} comment id:{}".format(row_id, col_id, comment_id)

@app.route('/<int:row_id>/<int:col_id>/<int:comment_id>/edit_row_comment')
def EditItemComment(row_id,col_id,comment_id):
	return "Page for editing a comment for the row: row{}, col_id{}, comment id:{}".format(row_id, col_id, comment_id)

@app.route('/<int:row_id>/<int:col_id>/<int:comment_id>/delete_row_comment')
def DeleteItemComment(row_id, col_id, comment_id):
	return "Page for deleting a comment for the row: row{}, col_id{}, comment id:{}".format(row_id, col_id, comment_id)


#____COMMENT COMMENTS______ - I don't think this is necessary? 

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)