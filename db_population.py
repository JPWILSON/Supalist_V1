from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, list_keywords, List, ListKeyword, HeadingItem
from database_setup import Row, ShortTextEntry, LongTextEntry, DateEntry, DateTimeEntry 
from database_setup import Bools, TimeEntry, Duration, TwoDecimal, LargeDecimal

engine = create_engine('postgresql+psycopg2://catalog:db-password@localhost/supalist1')
Base.metadata.bind = engine 
DBSession = sessionmaker(bind = engine)
session = DBSession()

user1 = User(user_name = 'jeany', email = 'jeany@jean.com', picture = 'None')
session.add(user1)
session.commit()
'''
u1 = session.query(User).all()

for u in u1:
	print u.email, "   --    __   --  ", u.user_name'''

user2 = User(user_name = 'michy', email = 'michy@jean.com', picture = 'None')
session.add(user2)
session.commit()

user3 = User(user_name = 'catty', email = 'catty@jean.com', picture = 'None')
session.add(user3)
session.commit()

print "3 users added"
#Lists
l1 = List(name = "People", description = "list of every person on the planet - should get to about 9billion entries when complete", votes = 0, user=user1 )
session.add(l1)
session.commit()

l2 = List(name = "Banks", description = "list every single bank", votes = 0, user=user1 )
session.add(l2)
session.commit()

l3 = List(name = "Dog breeds", description = "", votes = 0, user=user2 )
session.add(l3)
session.commit()

l4 = List(name = "Skyscrapers", description = "This is a subset of buildings - lets see how it plays out", votes = 0, user=user3 )
session.add(l4)
session.commit()

#Keywords    eg post.keywords.append(Keyword('wendy'))
l1.l_keywords.append(ListKeyword(keyword = 'richest'))
#session.commit()
l1.l_keywords.append(ListKeyword(keyword = 'oldest'))
#session.commit()
l1.l_keywords.append(ListKeyword(keyword = 'fastest'))
#session.commit()



l2.l_keywords.append(ListKeyword(keyword = 'oldest'))
session.commit()
l2.l_keywords.append(ListKeyword(keyword = 'richest'))
session.commit()
l2.l_keywords.append(ListKeyword(keyword = 'transparent'))
session.commit()
l2.l_keywords.append(ListKeyword(keyword = 'largest'))
session.commit()


l3.l_keywords.append(ListKeyword(keyword = 'biggest'))
session.commit()
l3.l_keywords.append(ListKeyword(keyword = 'smallest'))
session.commit()
l3.l_keywords.append(ListKeyword(keyword = 'fastest'))
session.commit()


l4.l_keywords.append(ListKeyword(keyword = 'tallest'))
session.commit()
l4.l_keywords.append(ListKeyword(keyword = 'newest'))
session.commit()


#Heading Items:
# For list 1
h1 = HeadingItem(name="Frist Name", description="The first name a person is known by", entry_data_type = 1, votes=0, lists= l1, user=user3)
session.add(h1)
session.commit()
h2 = HeadingItem(name="Last Name", description="The last or surname", entry_data_type = 1, votes=0, user=user3)
session.add(h2)
session.commit()
h3 = HeadingItem(name="Date of birth", description="", entry_data_type = 3, votes=0, lists= l1, user=user2)
session.add(h3)
session.commit()
h4 = HeadingItem(name="Net worth", description="How much money does a person have ", entry_data_type = 8, votes=0, lists= l1, user=user3)
session.add(h4)
session.commit()

# For list 2
h5 = HeadingItem(name="Name", description="of bank", entry_data_type = 1, votes=0, lists= l2, user=user3)
session.add(h5)
session.commit()
h6 = HeadingItem(name="Founding Date", description="self explanatory", entry_data_type = 3, votes=0, lists= l2, user=user3)
session.add(h6)
session.commit()
h7 = HeadingItem(name="Founding Location", description="self explanatory", entry_data_type = 1, votes=0, lists= l2, user=user2)
session.add(h7)
session.commit()
h8 = HeadingItem(name="Value", description="self explanatory", entry_data_type = 8, votes=0, lists= l2, user=user3)
session.add(h8)
session.commit()

# For list 3
h9 = HeadingItem(name="Name", description="self explanatory", entry_data_type = 1, votes=0, lists= l3, user=user3)
session.add(h9)
session.commit()
h10 = HeadingItem(name="Origin", description="self explanatory", entry_data_type = 1, votes=0, lists= l3, user=user3)
session.add(h10)
session.commit()
h11 = HeadingItem(name="Date declared", description="self explanatory", entry_data_type = 3, votes=0, lists= l3, user=user2)
session.add(h11)
session.commit()
h12 = HeadingItem(name="Avg Male Height", description="self explanatory ", entry_data_type = 8, votes=0, lists= l3, user=user3)
session.add(h12)
session.commit()

# For list 4
h13 = HeadingItem(name="Name", description="self explanatory", entry_data_type = 1, votes=0, lists= l4, user=user3)
session.add(h13)
session.commit()
h14 = HeadingItem(name="Architect", description="self explanatory", entry_data_type = 1, votes=0, lists= l4, user=user3)
session.add(h14)
session.commit()
h15 = HeadingItem(name="Cost", description="self explanatory", entry_data_type = 8, votes=0, lists= l4, user=user3)
session.add(h15)
session.commit()
h16 = HeadingItem(name="Date built", description="self explanatory ", entry_data_type = 3, votes=0, lists= l4, user=user2)
session.add(h16)
session.commit()
h17 = HeadingItem(name="Location", description="self explanatory ", entry_data_type = 1, votes=0, lists= l4, user=user3)
session.add(h17)
session.commit()

#Specific Rows for each list

# For list 1
r1 = Row(votes = 0, lists = l1, user=user3)
session.add(r1)
session.commit()
r2 = Row(votes = 0, lists = l1, user=user3)
session.add(r2)
session.commit()
r3 = Row(votes = 0, lists = l1, user=user3)
session.add(r3)
session.commit()

# For list 2
r4 = Row(votes = 0, lists = l2, user=user3)
session.add(r4)
session.commit()
r5 = Row(votes = 0, lists = l2, user=user3)
session.add(r5)
session.commit()
r6 = Row(votes = 0, lists = l2, user=user2)
session.add(r6)
session.commit()

# For list 3
r7 = Row(votes = 0, lists = l3, user=user3)
session.add(r7)
session.commit()
r8 = Row(votes = 0, lists = l3, user=user2)
session.add(r8)
session.commit()
r9 = Row(votes = 0, lists = l3, user=user3)
session.add(r9)
session.commit()

# For list 4
r10 = Row(votes = 0, lists = l4, user=user3)
session.add(r10)
session.commit()
r11 = Row(votes = 0, lists = l4, user=user3)
session.add(r11)
session.commit()
r12 = Row(votes = 0, lists = l4, user=user3)
session.add(r12)
session.commit()


#Now, the actual entries: 
#list1 row1
entry1 = ShortTextEntry(entry="Jean-Paul", votes=0, heading =h1 , lists =r1 , user=user2)
session.add(entry1)
session.commit()
entry2 = ShortTextEntry(entry="Wilson", votes=0, heading =h2 , lists =r1 , user=user3)
session.add(entry2)
session.commit()
entry3 = DateEntry(entry="1984-06-05", votes=0, heading =h3 , lists =r1, user=user3)
session.add(entry3)
session.commit()
entry4 = TwoDecimal(entry="100000.00", votes=0, heading =h4 , lists =r1, user=user3)
session.add(entry4)
session.commit()

#list1 row2
entry5 = ShortTextEntry(entry="Michelle", votes=0, heading =h1 , lists =r2 , user=user3)
session.add(entry5)
session.commit()
entry6 = ShortTextEntry(entry="Wilson", votes=0, heading =h2 , lists =r2  , user=user3)
session.add(entry6)
session.commit()
entry7 = DateEntry(entry="1984-02-19", votes=0, heading =h3 , lists =r2 , user=user2)
session.add(entry7)
session.commit()
entry8 = TwoDecimal(entry="75000.00", votes=0, heading =h4 , lists =r2 , user=user3)
session.add(entry8)
session.commit()

#list1 row3
entry9 = ShortTextEntry(entry="Henk", votes=0, heading = h1, lists =r3 , user=user3)
session.add(entry9)
session.commit()
entry10 = ShortTextEntry(entry="Wilson", votes=0, heading =h2 , lists =r3  , user=user3)
session.add(entry10)
session.commit()
entry11 = DateEntry(entry="2017-05-25", votes=0, heading =h3 , lists =r3 , user=user3)
session.add(entry11)
session.commit()
entry12 = TwoDecimal(entry="50.00", votes=0, heading =h4 , lists =r3 , user=user1)
session.add(entry12)
session.commit()


#list2 row1
e13 = ShortTextEntry(entry="Capitec", votes=0, heading =h5 , lists =r4 , user=user3)
session.add(e13)
session.commit()
e14 = DateEntry(entry="2012-05-25", votes=0, heading =h6 , lists =r4 , user=user1)
session.add(e14)
session.commit()
e15 = ShortTextEntry(entry="Cape Town, South Africa", votes=0, heading =h7 , lists =r4, user=user3)
session.add(e15)
session.commit()
e16 = TwoDecimal(entry="450000000.00", votes=0, heading =h8 , lists =r4, user=user3)
session.add(e16)
session.commit()


# list2 row2
e17 = ShortTextEntry(entry="JPMorgan", votes=0, heading =h5 , lists =r5, user=user1)
session.add(e17)
session.commit()
e18 = DateEntry(entry="1918-05-25", votes=0, heading =h6 , lists =r5, user=user1)
session.add(e18)
session.commit()
e19 = ShortTextEntry(entry="NYC, USA", votes=0, heading =h7 , lists =r5, user=user3)
session.add(e19)
session.commit()
e20 = TwoDecimal(entry="17000000000", votes=0, heading =h8 , lists =r5, user=user3)
session.add(e20)
session.commit()

# list2 row3
e21 = ShortTextEntry(entry="First National Bank", votes=0, heading =h5 , lists =r6, user=user3)
session.add(e21)
session.commit()
e22 = DateEntry(entry="1942-01-25", votes=0, heading =h6 , lists =r6, user=user3)
session.add(e22)
session.commit()
e23 = ShortTextEntry(entry="London, England", votes=0, heading =h7 , lists =r6, user=user1)
session.add(e23)
session.commit()
e24 = TwoDecimal(entry="6000000000.00", votes=0, heading =h8 , lists =r6, user=user3)
session.add(e24)
session.commit()

# list3 row1
e25 = ShortTextEntry(entry="Weimaraner", votes=0, heading =h9 , lists =r7, user=user1)
session.add(e25)
session.commit()
e26 = ShortTextEntry(entry="Germany", votes=0, heading =h10 , lists =r7, user=user3)
session.add(e26)
session.commit()
e27 = DateEntry(entry="1902-01-25", votes=0, heading =h11 , lists =r7, user=user3)
session.add(e27)
session.commit()
e28 = TwoDecimal(entry="65", votes=0, heading =h12 , lists =r7, user=user1)
session.add(e28)
session.commit()

# list3 row2
e29 = ShortTextEntry(entry="Dalmation", votes=0, heading =h9 , lists =r8, user=user1)
session.add(e29)
session.commit()
e30 = ShortTextEntry(entry="Dalmatia, Croatia", votes=0, heading =h10 , lists =r8, user=user1)
session.add(e30)
session.commit()
e31 = DateEntry(entry="1500-01-02", votes=0, heading =h11 , lists =r8, user=user1)
session.add(e31)
session.commit()
e32 = TwoDecimal(entry="55", votes=0, heading =h12 , lists =r8, user=user1)
session.add(e32)
session.commit()

# list3 row3
e33 = ShortTextEntry(entry="Siberian Husky", votes=0, heading =h9 , lists =r9, user=user3)
session.add(e33)
session.commit()
e34 = ShortTextEntry(entry="Chukchi Peninsula, Siberia", votes=0, heading =h10 , lists =r9, user=user3)
session.add(e34)
session.commit()
e35 = DateEntry(entry="1908-01-25", votes=0, heading =h11 , lists =r9, user=user1)
session.add(e35)
session.commit()
e36 = TwoDecimal(entry="58", votes=0, heading =h12 , lists =r9 , user=user3)
session.add(e36)
session.commit()

# list4 row1
e37 = ShortTextEntry(entry="Empire State Building", votes=0, heading =h13 , lists =r10 , user=user3)
session.add(e37)
session.commit()
e38 = ShortTextEntry(entry="William F. Lamb", votes=0, heading =h14 , lists =r10 , user=user3)
session.add(e38)
session.commit()
e39 = TwoDecimal(entry="41000000.00", votes=0, heading =h15 , lists =r10 , user=user3)
session.add(e39)
session.commit()
e40 = DateEntry(entry="1931-05-31", votes=0, heading =h16 , lists =r10 , user=user1)
session.add(e40)
session.commit()
e41 = ShortTextEntry(entry="NYC, USA", votes=0, heading =h17 , lists =r10 , user=user3)
session.add(e41)
session.commit()

# list4 row2
e42 = ShortTextEntry(entry="Chrysler Building", votes=0, heading =h13 , lists =r11 , user=user3)
session.add(e42)
session.commit()
e43 = ShortTextEntry(entry="William Van Alen", votes=0, heading =h14 , lists =r11 , user=user3)
session.add(e43)
session.commit()
e44 = TwoDecimal(entry="15000000.00", votes=0, heading =h15 , lists =r11 , user=user3)
session.add(e44)
session.commit()
e45 = DateEntry(entry="1930-01-01", votes=0, heading =h16 , lists =r11 , user=user1)
session.add(e45)
session.commit()
e46 = ShortTextEntry(entry="NYC, USA", votes=0, heading =h17 , lists =r11 , user=user1)
session.add(e46)
session.commit()

# list4 row3
e47 = ShortTextEntry(entry="Burj Khalifa", votes=0, heading =h13 , lists =r12 , user=user1)
session.add(e47)
session.commit()
e48 = ShortTextEntry(entry="Adrian Smith", votes=0, heading =h14 , lists =r12 , user=user1)
session.add(e48)
session.commit()
e49 = TwoDecimal(entry="1500000000.00", votes=0, heading =h15 , lists =r12 , user=user1)
session.add(e49)
session.commit()
e50 = DateEntry(entry="2010-01-04", votes=0, heading =h16 , lists =r12 , user=user2)
session.add(e50)
session.commit()
e51 = ShortTextEntry(entry="Dubai, UAE", votes=0, heading =h17 , lists =r12 , user=user3)
session.add(e51)
session.commit()


print "Success! It seems!"



