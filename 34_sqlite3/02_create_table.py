# cursor()
# ↓
# SQL Query Execute કરવા માટે વપરાય છે.

# Connection
# ↓
# Cursor
# ↓
# Execute SQL
# ↓
# Commit
# ↓
# Save

import sqlite3

conn = sqlite3.connect("34_sqlite3/000_demo.db")

cursor = conn.cursor()

cursor.execute(""" 
CREATE TABLE student (
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER
)
""")
print("table created")
conn.commit()
conn.close()