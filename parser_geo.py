import sqlite3
import requests
import time

def get_location(ip):
    try:
        # API gratis (jangan terlalu cepat manggilnya biar ga diblokir)
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        return response.get('country', 'Unknown'), response.get('city', 'Unknown')
    except:
        return "Unknown", "Unknown"

conn = sqlite3.connect('siem.db')
c = conn.cursor()

# Ambil IP yang lokasinya masih kosong
c.execute("SELECT DISTINCT ip_address FROM logs WHERE country IS NULL")
ips = c.fetchall()

for row in ips:
    ip = row[0]
    country, city = get_location(ip)
    print(f"IP {ip} berasal dari {country}, {city}")
    c.execute("UPDATE logs SET country = ?, city = ? WHERE ip_address = ?", (country, city, ip))
    conn.commit()
    time.sleep(1.5) # Jeda dikit biar gak kena limit API

conn.close()
