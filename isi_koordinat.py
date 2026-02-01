import sqlite3
import requests
import time

def ambil_geo(ip):
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
data_kosong = c.fetchall()

print(f"Sedang memproses {len(data_kosong)} IP. Tunggu bentar ya...")

for row in data_kosong:
    ip = row[0]
    negara, latitude, longitude = ambil_geo(ip)
    print(f"IP {ip} -> {negara} ({latitude}, {longitude})")
    
    c.execute("UPDATE logs SET country=?, lat=?, lon=? WHERE ip_address=?", 
              (negara, latitude, longitude, ip))
    conn.commit()
    time.sleep(1.2) # Biar gak kena blokir API gratisan

conn.close()
print("Selesai! Sekarang coba refresh Grafana kamu.")
