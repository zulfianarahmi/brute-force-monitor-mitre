import re
import sqlite3

log_pattern = r"(\w{3}\s+\d+\s\d+:\d+:\d+).*Failed password for (?:invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)"

def parse_logs():
    conn = sqlite3.connect('siem.db')
    c = conn.cursor()
    
    with open('/var/log/auth.log', 'r') as f:
        for line in f:
            match = re.search(log_pattern, line)
            if match:
                timestamp, username, ip = match.groups()
                c.execute("INSERT INTO logs (timestamp, ip_address, username, status) VALUES (?, ?, ?, ?)",
                          (timestamp, ip, username, "Failed"))
    
    conn.commit()
    conn.close()
    print("Data log berhasil dipindahkan ke SQLite!")

if __name__ == "__main__":
    parse_logs()
