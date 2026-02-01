import sqlite3

conn = sqlite3.connect('siem.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME,
        ip_address TEXT,
        username TEXT,
        status TEXT
    )
''')

conn.commit()
conn.close()
print("Database siem.db berhasil dibuat!")
