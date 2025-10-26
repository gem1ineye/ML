import sqlite3   # 🧩 Import the SQLite library

# 🔗 Connect (or create) a database file named 'bank.db'
conn = sqlite3.connect('bank.db')

# 🧭 Create a cursor object for executing SQL statements
cursor = conn.cursor()


cursor.execute('''
               insert into customer values
            (110,'ANIL','MUMBAI','anil@gmail.com'),
            (111,'SMITH','DELHI','smith@gmail.com')               
               
               ''')

cursor.execute('''
               insert into account values
               (101,110,'SAVINGS',2500.00),
               (102,111,'CHECKING',1200.25)
               
               ''')

cursor.execute('''
               insert into bank_transaction values
               (1,101,'deposit',500.00,'2025-07-04'),
               (2,102,'withdrawal',100.00,'2025-07-05')
               ''')

conn.commit()
conn.close