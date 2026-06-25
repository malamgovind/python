import sqlite3

conn = sqlite3.connect("34_sqlite3/000_demo.db")

cursor = conn.cursor()

cursor.execute("""
UPDATE student
SET age = 25
WHERE name = 'hari'
"""
)

conn.commit()

cursor.execute("" \
"SELECT * FROM student"
)
datas = cursor.fetchall()
for data in datas:
    print(data)
    
conn.close()