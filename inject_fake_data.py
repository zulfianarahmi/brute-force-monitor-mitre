import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('siem.db')
c = conn.cursor()

users = ['root', 'admin', 'user', 'ubuntu', 'oracle', 'test', 'support']
ips = [
    '103.252.200.1', '1.1.1.1', '45.125.65.12', 
    '185.220.101.43', '192.168.1.5', '91.241.19.84'
]

print("Menyuntikkan data palsu...")

for i in range(180):  
    user = random.choice(users)
    ip = random.choice(ips)
    dt = datetime.now() - timedelta(minutes=random.randint(1, 1000))
    timestamp = dt.strftime('%b %d %H:%M:%S')
    
    c.execute("INSERT INTO logs (timestamp, ip_address, username, status) VALUES (?, ?, ?, ?)",
              (timestamp, ip, user, "Failed"))

conn.commit()
conn.close()
print("Selesai! Sekarang cek Grafana kamu.")
