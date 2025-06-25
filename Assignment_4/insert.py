import sqlite3
conn = sqlite3.connect("database.db")
#Executing one at a time by commenting others because only one insertion can done at single time
# conn.execute('''
# INSERT INTO User_Details(usnm,pass,mobile,email) values("Suraj","Suraj_123","8596741245","Suraj@gmail.com")
# ''')
# conn.execute('''
# INSERT INTO Student(S_id,S_Name,S_mail,S_mobile) values(1,"varun","varun@gmail.com","9874124585")
# ''')
conn.execute('''
INSERT INTO Employee(E_id,e_name,e_mail,e_mobile) values("1","Tapesh","tapesh@gmail.com","7845968574")
''')
conn.commit()
conn.close()