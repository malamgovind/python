import sqlite3

conn = sqlite3.connect("34_sqlite3/000_demo.db")

cursor = conn.cursor()

cursor.execute("""

SELECT * FROM student
ORDER by age

""")

datas = cursor.fetchall()
for data in datas:
    print(data)

conn.close()