import sqlite3

conn = sqlite3.connect("34_sqlite3/000_demo.db")

cursor = conn.cursor()

cursor.execute(
    """SELECT * FROM student
    WHERE age = 20
    """
)

data = cursor.fetchall()
print(data)
conn.close()