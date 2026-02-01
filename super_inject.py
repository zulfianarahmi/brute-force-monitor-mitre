import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('siem.db')
c = conn.cursor()

# Daftar IP dari berbagai negara (China, USA, Russia, Brazil, Germany, Indonesia)
global_ips = [
    '223.5.5.5', '8.8.8.8', '95.161.226.250', '200.221.2.45', 
    '1.1.1.1', '103.10.125.1', '31.13.127.1', '185.220.101.43',
    '45.125.65.12', '103.252.200.1', '91.241.19.84', '141.101.123.30'
]
usernames = ['admin', 'root', 'user', 'guest', 'oracle', 'test', 'ubuntu', 'support']

print("Menyuntikkan data serangan global...")

for i in range(200):
    ip = random.choice(global_ips)
    user = random.choice(usernames)
    dt = datetime.now() - timedelta(minutes=random.randint(1, 5000))
    ts = dt.strftime('%b %d %H:%M:%S')
    
    c.execute("INSERT INTO logs (timestamp, ip_address, username, status) VALUES (?, ?, ?, ?)",
              (ts, ip, user, "Failed"))

conn.commit()
conn.close()
print("200 Data serangan baru berhasil ditambahkan!")
