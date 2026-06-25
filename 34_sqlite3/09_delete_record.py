import sqlite3

conn = sqlite3.connect("34_sqlite3/000_demo.db")

cursor = conn.cursor()

cursor.execute("""
DELETE FROM student
WHERE name = 'parth'
""")

conn.commit()
conn.close()