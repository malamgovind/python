import sqlite3

conn = sqlite3.connect("34_sqlite3/000_demo.db")

cursor = conn.cursor()

cursor.execute(""" 
INSERT INTO student
(name, age)
VALUES
('govindone', 20)
 """)
print("data inserted into student table")
conn.commit()
conn.close()