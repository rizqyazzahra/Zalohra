# ZALOHRA

Proyek Django sebagai tugas mata kuliah Pemrograman Berbasis Platform (PBP) Ganjil 2024/2025 oleh Rizqya Az Zahra Putri - 230644936.

🔗Tautan PWS _deployment_: [Zalohra](http://rizqya-az-zalohra.pbp.cs.ui.ac.id/)

---
## Tugas 2: Implementasi Model-View-Template (MVT) pada Django
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
4. Masih di direktori lokal, membuat file requirements.txt yang berisi daftar _dependencies_ yang akan diperlukan.
  ```
  django
  gunicorn
  whitenoise
  psycopg2-binary
  requests
  urllib3
  ```
5. Melakukan instalasi terhadap _dependencies_ dengan perintah:
  ```
  pip install -r requirements.txt
  ```
6. Membuat proyek Django bernama 'Zalohra' dengan perintah:
  ```
  django-admin startproject Zalohra .
  ```
7. Menambahkan string pada ALLOWED_HOST di settings.py untuk keperluan _deployment_:
  ```
  ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
  ```
8. Membuat repositori baru di GitHub dengan nama 'Zalohra'
9. Menambahkan berkas .gitignore
10. Membuat _branch_ utama baru dengan nama "main" menggunakan perintah:
  ```
  git branch -M main
  ```
11. Menghubungkan direktori lokal dengan repositori di GitHub menggunakan perintah:
  ```
  git remote add origin https://github.com/rizqyazzahra/Zalohra.git
  ```
12. Melakukan _add_, __commit__, dan __push__ dari direktori lokal ke repositori GitHub
