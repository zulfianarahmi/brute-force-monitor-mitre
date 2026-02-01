import sqlite3
import requests
import time

def get_geo(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if r.get('status') == 'success':
            return r.get('country'), r.get('lat'), r.get('lon')
        return "Unknown", 0, 0
    except:
        return "Unknown", 0, 0

conn = sqlite3.connect('siem.db')
c = conn.cursor()

try:
    c.execute("ALTER TABLE logs ADD COLUMN lat REAL")
    c.execute("ALTER TABLE logs ADD COLUMN lon REAL")
except:
    pass 

c.execute("SELECT DISTINCT ip_address FROM logs WHERE country IS NULL OR country = ''")
rows = c.fetchall()

print(f"Mengolah {len(rows)} IP baru...")

for row in rows:
    ip = row[0]
    country, lat, lon = get_geo(ip)
    print(f"IP: {ip} -> {country}")
    c.execute("UPDATE logs SET country=?, lat=?, lon=? WHERE ip_address=?", (country, lat, lon, ip))
    conn.commit()
    time.sleep(1.2) 

conn.close()
print("Selesai! Sekarang cek Grafana kamu.")
