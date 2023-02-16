import sqlite3
conn=sqlite3.connect('Zard.db')
print("opened db successfully")

conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (1,'Ben',43,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (2,'Jack',65,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (3,'James',45,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (4,'Henry',78,'eMobilis')")


conn.commit()
print("records added successfully")
conn.close()
