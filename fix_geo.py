import sqlite3
import requests
import time

def get_geo(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if r.get('status') == 'success':
            return r.get('country'), r.get('lat'), r.get('lon')
    except:
        pass
    return "Unknown", 0, 0

conn = sqlite3.connect('siem.db')
c = conn.cursor()

c.execute("SELECT DISTINCT ip_address FROM logs WHERE lat IS NULL OR lat = 0")
rows = c.fetchall()

print(f"Mengisi koordinat untuk {len(rows)} data...")

for row in rows:
    ip = row[0]
    country, lat, lon = get_geo(ip)
    print(f"Updating {ip} -> {country} ({lat}, {lon})")
    c.execute("UPDATE logs SET country=?, lat=?, lon=? WHERE ip_address=?", (country, lat, lon, ip))
    conn.commit()
    time.sleep(1.2) # Jeda biar gak diblokir

conn.close()
print("Selesai! Sekarang cek lagi di Grafana.")
