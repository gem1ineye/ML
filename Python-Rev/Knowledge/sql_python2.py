import sqlite3   # 🧩 Import the SQLite library (built-in with Python)

# 🔗 Connect to (or create) a database named 'univFromPy.db'
# 👉 If this file doesn't exist, SQLite automatically creates it in the current directory.
conn = sqlite3.connect('univFromPy.db')

# 🧭 Create a cursor object to execute SQL commands
cursor = conn.cursor()

# 📝 Take user input for department details
dno = input('Enter Dept no: ')        # Example: 10
dnam = input('Enter Department name: ')  # Example: CSE

# 🧱 Insert the new department record into the 'dept' table
# ⚠️ Using f-string here works, but it’s vulnerable to SQL injection.
#    For safety, it's better to use parameterized queries (see below).
cursor.execute(f'INSERT INTO dept VALUES ({dno}, "{dnam}")')

# 💾 Commit the transaction so changes are saved to the database
conn.commit()

# 🚪 Close the cursor and connection to free up resources
cursor.close()
conn.close()

print("✅ Department added successfully!")
