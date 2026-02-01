# Brute Force Global Monitor
Link Medium : https://medium.com/@zulfianarahmi4/monitoring-serangan-brute-force-global-pakai-python-grafana-1cb8c4070e6b?postPublishedType=repub

Sebuah proyek monitoring keamanan siber mandiri (SIEM) yang dibangun dengan biaya nol rupiah untuk mendeteksi serangan **Brute Force (MITRE ATT&CK T1110)** pada sistem Linux/WSL secara real-time.

## Fitur Utama

* **Log Ingestion**: Otomatisasi pembacaan log autentikasi Linux (`/var/log/auth.log`) menggunakan Python.
* **Geo-Enrichment**: Konversi IP publik menjadi koordinat geografis (Lat/Lon) dan informasi negara asal.
* **Interactive Dashboard**: Visualisasi peta dunia, statistik serangan, dan target username paling populer menggunakan Grafana.
* **Containerized Deployment**: Seluruh infrastruktur visualisasi dibungkus dalam Docker untuk kemudahan setup.

## Tech Stack

* **Language**: Python 3.x
* **Database**: SQLite (Ringan & Cepat)
* **Visualization**: Grafana
* **Infrastructure**: Docker & Docker Compose
* **Environment**: Ubuntu (WSL2)

## Struktur Direktori

* `docker-compose.yml`: Konfigurasi container Grafana.
* `init_db.py`: Inisialisasi skema database SQLite.
* `parser.py`: Script untuk mengekstrak data dari `auth.log`.
* `isi_koordinat.py`: Menambahkan konteks geografis (Data Enrichment) ke database.
* `super_inject.py`: Generator data simulasi serangan global.
* `siem.db`: Database penyimpan log yang sudah terstruktur.

## Cara Menjalankan

1. **Clone Repository**:
```bash
git clone zulfianarahmi/brute-force-monitor-mitre
cd brute-force-global-monitor

```


2. **Setup Infrastruktur**:
Jalankan Grafana menggunakan Docker:
```bash
docker-compose up -d

```


3. **Persiapkan Database**:
```bash
python3 init_db.py

```


4. **Jalankan Parser & Enrichment**:
```bash
python3 parser.py
python3 isi_koordinat.py

```


5. **Akses Dashboard**:
Buka `localhost:3000` di browser dan hubungkan SQLite datasource ke file `siem.db`.

## Hasil Analisis

Project ini berhasil memetakan bahwa mayoritas serangan Brute Force menargetkan akun standar seperti `root`, `admin`, dan `user`. Dengan visualisasi ini, tim keamanan dapat melakukan *Geo-blocking* berbasis negara atau IP agresif secara lebih akurat.


