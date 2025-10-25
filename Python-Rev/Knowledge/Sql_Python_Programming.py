
import sqlite3

# 🔗 Connect to (or create) a database named 'univFromPy.db'
# If the file doesn't exist, SQLite automatically creates it
conn = sqlite3.connect('univFromPy.db')

# 🧭 Create a cursor object to execute SQL commands
cursor = conn.cursor()

# 🏗️ Execute an SQL command to create a table named 'dept'
# This table has two columns:
#   → deptno: integer, primary key (unique for each department)
#   → dname: text (department name)
cursor.execute('CREATE TABLE dept (deptno INTEGER PRIMARY KEY, dname TEXT)')

cursor.execute('''
CREATE TABLE students (
    rollno INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT,
    deptno INTEGER,
    FOREIGN KEY (deptno) REFERENCES dept(deptno)
)
''')

dno=input('Enter Dept no')
dnam=input('Enter Department name')

cursor.execute('f{insert into dept values ({dno},"{dnam}")}')

conn.commit()

cursor.close()

conn.close()