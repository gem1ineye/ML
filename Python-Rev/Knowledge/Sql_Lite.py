import sqlite3

# Step 1: Connect to SQLite (creates file if not exists)
conn = sqlite3.connect("test_db.sqlite")

# Step 2: Create a cursor object
cur = conn.cursor()


