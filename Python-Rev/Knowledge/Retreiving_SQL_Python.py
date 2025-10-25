import sqlite3   # 🧩 Import the SQLite library (built-in with Python)

# 🔗 Connect to (or create) a database named 'univFromPy.db'
# 👉 If this file doesn't exist, SQLite automatically creates it in the current directory.
conn = sqlite3.connect('univFromPy.db')

# 🧭 Create a cursor object to execute SQL commands
cursor = conn.cursor()


row=cursor.execute('select * from dept')

t=row.fetchone()

print(t)

#While retrieving we dont have to commit because we are not saving anyting in Database


# 🚪 Close the cursor and connection to free up resources
cursor.close()
conn.close()


