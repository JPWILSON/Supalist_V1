from flask import Flask, render_template, request, url_for, redirect, flash, jsonify

#Fake Lists
list1 = {'name': 'people', 'id': '1', 'description': 'A list describing people, should have about 10billion entries I gues?', 'unique_instance':'True', 'votes':'0'}
lists = [{'name': 'people', 'id': '1', 'description': 'A list describing people, should have about 10billion entries I gues?', 'votes':'0'}, 
{'name':'buildings', 'id':'2', 'description': 'A list describing buildings, from houses to skyscrapers', 'unique_instance':'False', 'votes':'0'},
{'name':'cars', 'id':'3', 'description': 'A list describing all the types of cars on the planet', 'unique_instance':'False', 'votes':'0'}]


#Fake Headings
heading_item =  {'name':'First Name','description':'A person\'s first name','adjective1':'First Name','id' :'1','list_id' :'1'}
heading_items = [ {'name':'First Name','description':'A person\'s first name','adjective1':'First Name','id' :'1','list_id' :'1'}, 
{'name':'Middle Name','description':'A person\'s middle name','adjective1':'Middle Name','id' :'2','list_id' :'1'},
{'name':'Last Name','description':'A person\'s last name','adjective1':'Last Name','id' :'3','list_id' :'1'},
{'name':'Net Worth', 'description':'Value of all personal assets','adjective1':'Richest','id' :'4','list_id' :'1'},
{'name':'Common Name', 'description':'What this building is known as ','adjective1':'name','id' :'5','list_id' :'2'},
{'name':'Make & Model', 'description':'What is this car known as ','adjective1':'name','id' :'6','list_id' :'3'} ]


#Fake Rows
row_item =  {'id':'1','l_id':'1','votes':'7'}
row_items = [ {'id':'1','l_id':'1','votes':'7'},{'id':'2','l_id':'1','votes':'17'},
{'id':'3','l_id':'1','votes':'71'},{'id':'4','l_id':'2','votes':'6'},{'id':'5','l_id':'3','votes':'97'} ]


#Fake Data_entry
data_item =  {'id':'1','data':'Jean-Paul','l_id':'1','h_id' :'1'}
data_items = [ {'id':'1','data':'Jean-Paul','row_id':'1','h_id' :'1'},{'id':'2','data':'none','row_id':'1','h_id' :'2'},
{'id':'3','data':'Wilson','row_id':'1','h_id' :'3'},{'id':'4','data':'Michelle','row_id':'2','h_id' :'1'},
{'id':'5','data':'Ingrid','row_id':'2','h_id' :'2'},{'id':'6','data':'Wilson','row_id':'2','h_id' :'3'},
{'id':'7','data':'105000','row_id':'22','h_id' :'4'},{'id':'8','data':'85000','row_id':'23','h_id' :'4'} ]




app = Flask(__name__)

@app.route('/')
def Home():
	#return "heading of all/ top lists, or of the main menu options"
	lists = [{'name': 'people', 'id': '1', 'description': 'A list describing people, should have about 10billion entries I gues?', 'votes':'0'}, 
	{'name':'buildings', 'id':'2', 'description': 'A list describing buildings, from houses to skyscrapers', 'unique_instance':'False', 'votes':'0'},
	{'name':'cars', 'id':'3', 'description': 'A list describing all the types of cars on the planet', 'unique_instance':'False', 'votes':'0'}]

	heading_items = [ {'name':'First Name','description':'A person\'s first name','adjective1':'First Name','id' :'1','list_id' :'1'}, 
	{'name':'Middle Name','description':'A person\'s middle name','adjective1':'Middle Name','id' :'2','list_id' :'1'},
	{'name':'Last Name','description':'A person\'s last name','adjective1':'Last Name','id' :'3','list_id' :'1'},
	{'name':'Net Worth', 'description':'Value of all personal assets','adjective1':'Richest','id' :'4','list_id' :'1'},
	{'name':'Common Name', 'description':'What this building is known as ','adjective1':'name','id' :'5','list_id' :'2'},
	{'name':'Make & Model', 'description':'What is this car known as ','adjective1':'name','id' :'6','list_id' :'3'} ]
	return render_template('homepage.html', lists = lists, h_items = heading_items)

@app.route('/new/')
def NewList():
	return "Page for making a new list"

@app.route('/<int:list_id>/edit/')
def EditList(list_id):
	return "Edit a list name, or any columnlike this __ {} __ ".format(list_id)

@app.route('/<int:list_id>/delete/')
def DeleteList(list_id):
	return "Are you sure you want to delete this list? (only certain privileges will allow you to delete a list? - or never?) list{}".format(list_id)

@app.route('/<int:list_id>/')
def QueryList(list_id):
	list1 = {'name': 'people', 'id': '1', 'description': 'A list describing people, should have about 10billion entries I gues?', 'unique_instance':'True', 'votes':'0'}
	heading_items = [ {'name':'First Name','description':'A person\'s first name','adjective1':'First Name','id' :'1','list_id' :'1'}, 
		{'name':'Middle Name','description':'A person\'s middle name','adjective1':'Middle Name','id' :'2','list_id' :'1'},
		{'name':'Last Name','description':'A person\'s last name','adjective1':'Last Name','id' :'3','list_id' :'1'},
		{'name':'Net Worth', 'description':'Value of all personal assets','adjective1':'Richest','id' :'4','list_id' :'1'},
		{'name':'Common Name', 'description':'What this building is known as ','adjective1':'name','id' :'5','list_id' :'2'},
		{'name':'Make & Model', 'description':'What is this car known as ','adjective1':'name','id' :'6','list_id' :'3'} ]

	row_items = [ {'id':'1','l_id':'1','votes':'7'},{'id':'2','l_id':'1','votes':'17'},
		{'id':'3','l_id':'1','votes':'71'}]

	data_items = [ {'id':'1','data':'Jean-Paul','row_id':'1','h_id' :'1'},{'id':'2','data':'none','row_id':'1','h_id' :'2'},
		{'id':'3','data':'Wilson','row_id':'1','h_id' :'3'},{'id':'4','data':'Michelle','row_id':'1','h_id' :'4'},
		{'id':'5','data':'Ingrid','row_id':'2','h_id' :'1'},{'id':'6','data':'Wilson','row_id':'2','h_id' :'2'},
		{'id':'7','data':'105000','row_id':'2','h_id' :'3'},{'id':'8','data':'85h00','row_id':'2','h_id' :'4'}, 
		{'id':'9','data':'Ingrhjd','row_id':'3','h_id' :'1'},{'id':'10','data':'Whjilson','row_id':'3','h_id' :'3'},
		{'id':'11','data':'105000','row_id':'3','h_id' :'3'},{'id':'12','data':'85j000','row_id':'3','h_id' :'4'}]

	return render_template('view.html', list = list1, h_items = heading_items[:4], row_items = row_items, d_items = data_items, lid = list_id)
	#return "A single list that you can view or inspect/query (this should be the most important\
	#feature, and \n it is from here that you would add to the list (edit). list{}".format(list_id)

@app.route('/<int:list_id>/new_col/')
def AddColumn(list_id):
	return render_template('add_column.html', list_id = list_id)
	#return "Add a new column (and therefore increase the usefulness of your list{}".format(list_id)

@app.route('/<int:list_id>/<int:col_id>/edit_col/')
def EditColumn(list_id, col_id):
	return "Edit a column (and therefore increase the usefulness of your list. \n \
	Ordinarily this should be to modify or add to the descriptions on this column, or to make another column more useful. \
	That is, \n when there are two columns doing the job that one column previosly used to do. (Eg. Address becomes:\
	GPS co-ords in one column, and Residential addresss in another column list{}, col{})".format(list_id, col_id)

@app.route('/<int:list_id>/<int:col_id>/delete_col/')
def DeleteColumn(list_id, col_id):
	return "Delete this column for list number: {}, column id: {}".format(list_id, col_id)

@app.route('/<int:list_id>/new_row/')
def AddRow(list_id):
	return "Add a new row to your list. That is, a new entry (and therefore increase the usefulness of your list with id: {}). ".format(list_id)

@app.route('/<int:list_id>/<int:row_id>/edit_row/')
def EditRow(list_id, row_id):
	return "Edit a row from list id: list{}, with a row id of: row{})".format(list_id, row_id)

@app.route('/<int:list_id>/<int:row_id>/delete_row/')
def DeleteRow(list_id, row_id):
	return "Delete this row for list number: {}, row id: {}".format(list_id, row_id)




#____LIST COMMENTS______

@app.route('/<int:list_id>/new_comment/')
def NewListComment(list_id):
	return "Page for making a new comment for the list: {}.".format(list_id)

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