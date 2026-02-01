import sqlite3
import requests
import time

def get_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if response.get('status') == 'success':
            return response.get('country')
        return "Unknown"
    except:
        return "Unknown"

conn = sqlite3.connect('siem.db')
c = conn.cursor()

c.execute("SELECT DISTINCT ip_address FROM logs WHERE country IS NULL OR country = ''")
rows = c.fetchall()

print(f"Ditemukan {len(rows)} IP baru. Mulai mencari lokasi...")

for row in rows:
    ip = row[0]
    country = get_location(ip)
    print(f"IP: {ip} -> Negara: {country}")
    
    c.execute("UPDATE logs SET country = ? WHERE ip_address = ?", (country, ip))
    conn.commit()
    time.sleep(1.5)

conn.close()
print("Selesai! Cek dashboard Grafana kamu lagi.")
