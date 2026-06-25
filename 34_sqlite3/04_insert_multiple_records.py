import sqlite3

conn = sqlite3.connect("34_sqlite3/000_demo.db")

cursor = conn.cursor()

students = [
    ("govind", 20),
    ("hari", 22), 
    ("parth", 21)
]

cursor.executemany("""
INSERT INTO student
(name, age)
VALUES
(?, ?)
 """, students)
print("data successfully inserted")
conn.commit()
conn.close()