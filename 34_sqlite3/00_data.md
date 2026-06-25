sqlite3 એ Python નું Built-in Database Module છે 
જે SQLite Database Files સાથે 
Connection,SQL Query Execution, CRUD Operations, Transactions અને
Persistent Data Storage માટે ઉપયોગ થાય છે.

SQLite એક Database Management System (DBMS) છે.

-- connect() database સાથે connection બનાવે છે.
-- (Python ↔ Database વચ્ચે bridge બનાવે છે.
   Database file open કરે છે. 
   Database માં read/write કરવાની permission આપે છે.
   )

-- Cursor database ને command મોકલે છે.

{
    અહીં fetchall() ફક્ત SELECT query માટે કામ કરે છે.

    UPDATE, INSERT, DELETE પછી fetchall() કરશો તો: khali empty ave che 

    aetle na lakhiye to chale 
}

-------------------------------------------------------------------
┌─────────┐
│ Python  │
└────┬────┘
     │
     │ connect()
     ▼
┌─────────┐
│  conn   │
└────┬────┘
     │
     │ cursor()
     ▼
┌─────────┐
│ cursor  │
└────┬────┘
     │
     │ execute()
     ▼
┌─────────────┐
│ Database    │
└─────────────┘
     ▲
     │
     │ fetchall()
     │
┌─────────┐
│ Python  │
└─────────┘

------------------------------------------------------------

sqlite3
│
├── Connection
├── Cursor
├── SQL
│   ├── DDL
│   ├── DML
│   └── DQL
├── CRUD
├── Transactions
├── Commit
├── Rollback
├── Primary Key
├── ACID
└── Database File

---------- ==-- ** commands ** --== ----------

CREATE TABLE table_name (...);

INSERT INTO table_name (...)
VALUES (...);

SELECT * FROM table_name;

SELECT * FROM table_name
WHERE condition;

UPDATE table_name
SET column=value
WHERE condition;

DELETE FROM table_name
WHERE condition;

DROP TABLE table_name;

======================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. CREATE TABLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CREATE TABLE student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

Memory Flow

CREATE TABLE
      │
      ▼
Table Name (student)
      │
      ▼
Columns Define
(id, name, age)
      │
      ▼
Table Created
      │
      ▼
Database Store


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. INSERT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INSERT INTO student (name, age)
VALUES ('hari', 22);

Memory Flow

INSERT INTO
      │
      ▼
student Table
      │
      ▼
(name, age)
Columns Select
      │
      ▼
VALUES
('hari', 22)
      │
      ▼
New Row Added


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. SELECT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SELECT * FROM student;

Memory Flow

SELECT *
      │
      ▼
All Columns
      │
      ▼
FROM student
      │
      ▼
Read Data
      │
      ▼
Return Result


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. WHERE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SELECT * FROM student
WHERE age = 22;

Memory Flow

student Table
      │
      ▼
Check Every Row
      │
      ▼
age = 22 ?
   ┌──┴──┐
   │     │
 YES    NO
   │     │
   ▼     ▼
Return Skip


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. UPDATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UPDATE student
SET age = 25
WHERE name = 'hari';

Memory Flow

UPDATE student
      │
      ▼
Find Row
(name='hari')
      │
      ▼
SET age = 25
      │
      ▼
Value Updated


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. DELETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DELETE FROM student
WHERE name = 'hari';

Memory Flow

DELETE FROM student
         │
         ▼
Find Row
(name='hari')
         │
         ▼
Delete Row
         │
         ▼
Row Removed


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. ORDER BY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SELECT * FROM student
ORDER BY age;

Memory Flow

student Table
      │
      ▼
age Column
      │
      ▼
Sort Data
      │
      ▼
Return Sorted Result


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8. LIMIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SELECT * FROM student
LIMIT 3;

Memory Flow

All Rows
    │
    ▼
Take First 3
    │
    ▼
Return Result


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9. COUNT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SELECT COUNT(*) FROM student;

Memory Flow

student Table
      │
      ▼
Count Rows
      │
      ▼
Return Total


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
10. DROP TABLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DROP TABLE student;

Memory Flow

student Table
      │
      ▼
Delete Structure
      │
      ▼
Delete Data
      │
      ▼
Table Removed