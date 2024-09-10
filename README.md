# ZALOHRA

Proyek Django sebagai tugas mata kuliah Pemrograman Berbasis Platform (PBP) Ganjil 2024/2025 oleh Rizqya Az Zahra Putri - 230644936.

Tautan PWS deployment: [Zalohra](http://rizqya-az-zalohra.pbp.cs.ui.ac.id/)

---
## Tugas 2
### 1. Langkah Implementasi
#### Membuat sebuah proyek Django baru.
1. Membuat direktori lokal bernama “Zalohra” lalu masuk ke dalam direktori tersebut
2. Membuka _command prompt_ dan membuat _virtual environment_ dengan menjalankan perintah:
```
py -m venv env
```
3. Mengaktifkan _virtual environment_ menggunakan perintah:
```
env\Scripts\activate
```
4. Masih di direktori lokal, membuat file requirements.txt yang berisi daftar dependencies yang akan diperlukan.
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
5. Melakukan instalasi terhadap dependencies dengan perintah:
```
pip install -r requirements.txt
```
6. Membuat project Django bernama 'Zalohra' dengan perintah:
```
django-admin startproject Zalohra .
```
7. Menambahkan string pada ALLOWED_HOST di settings.py untuk keperluan deployment:
```
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```
