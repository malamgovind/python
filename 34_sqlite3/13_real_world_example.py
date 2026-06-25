import sqlite3

conn = sqlite3.connect("34_sqlite3/000_demo.db")

cursor = conn.cursor()

cursor.execute(""" 

CREATE TABLE IF NOT EXISTS student(

id INTEGER PRIMARY KEY, 
name TEXT

)

""")

cursor.execute(""" 

INSERT INTO student(name)
VALUES ('malamgovind')

""")

conn.commit()

cursor.execute("SELECT * FROM student")

datas = cursor.fetchall()

for data in datas:
    print(data)

conn.close()