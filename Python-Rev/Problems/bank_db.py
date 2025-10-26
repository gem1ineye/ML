import sqlite3   # 🧩 Import the SQLite library

# 🔗 Connect (or create) a database file named 'bank.db'
conn = sqlite3.connect('bank.db')

# 🧭 Create a cursor object for executing SQL statements
cursor = conn.cursor()

# 🧱 Create 'customer' table — stores customer details
cursor.execute('''
CREATE TABLE IF NOT EXISTS customer (
    cust_id INTEGER PRIMARY KEY,   -- Unique ID for each customer
    name TEXT NOT NULL,            -- Customer's name
    address TEXT,                  -- Customer's address
    email TEXT UNIQUE              -- Email must be unique
)
''')

# 🧾 Create 'account' table — stores account details
cursor.execute('''
CREATE TABLE IF NOT EXISTS account (
    account_id INTEGER PRIMARY KEY,  -- Unique account number
    cust_id INTEGER,                 -- Linked to customer table
    acc_type TEXT,                   -- Account type (e.g., Savings, Current)
    balance REAL DEFAULT 0,          -- Account balance
    FOREIGN KEY (cust_id) REFERENCES customer(cust_id) -- Link to customer
)
''')

# 💰 Create 'transaction' table — stores all account transactions
cursor.execute('''
CREATE TABLE IF NOT EXISTS bank_transaction (
    trans_id INTEGER PRIMARY KEY,    -- Unique transaction ID
    acc_id INTEGER,                  -- References account table
    trans_type TEXT,                 -- Type (Deposit / Withdraw)
    amount REAL,                     -- Amount of transaction
    date DATE,                       -- Transaction date
    FOREIGN KEY (acc_id) REFERENCES account(account_id)  -- ✅ Correct spelling
)
''')

# ⚡ Commit changes and close the connection
conn.commit()
conn.close()

print("✅ Bank database and tables created successfully!")
