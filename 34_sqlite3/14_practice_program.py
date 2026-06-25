import sqlite3

conn = sqlite3.connect("34_sqlite3/000_demo.db")

cursor = conn.cursor()

cursor.execute(""" 

CREATE TABLE employee(
id INTEGER PRIMARY KEY,
name TEXT,
salary INTEGER
)

""")

conn.commit()

cursor.execute("""

INSERT INTO employee(name, salary)
VALUES('MG', 50000)

 """)

conn.commit()

cursor.execute("SELECT * FROM employee")

datas = cursor.fetchall()

for data in datas:
    print(data)

conn.close()