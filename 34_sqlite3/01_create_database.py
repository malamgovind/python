import sqlite3

conn = sqlite3.connect("34_sqlite3/000_demo.db")

print("database created")

conn.close()