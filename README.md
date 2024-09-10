# ZALOHRA

Proyek Django sebagai tugas mata kuliah Pemrograman Berbasis Platform (PBP) Ganjil 2024/2025 oleh Rizqya Az Zahra Putri - 230644936.

🔗 Tautan PWS _deployment_: [Zalohra](http://rizqya-az-zalohra.pbp.cs.ui.ac.id/)

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
4. Masih di direktori lokal, membuat file `requirements.txt` yang berisi daftar _dependencies_ yang akan diperlukan.
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
9. Menambahkan berkas `.gitignore`
10. Membuat _branch_ utama baru dengan nama "main" menggunakan perintah:
    ```
    git branch -M main
    ```
11. Menghubungkan direktori lokal dengan repositori di GitHub menggunakan perintah:
    ```
    git remote add origin https://github.com/rizqyazzahra/Zalohra.git
    ```
12. Melakukan _add_, _commit_, dan _push_ dari direktori lokal ke repositori GitHub


#### Membuat aplikasi dengan nama `main` pada proyek tersebut.
1. Di direktori utama Zalora, membuat aplikasi baru bernama 'main' menggunakan perintah:
   ```
   python manage.py startapp main
   ```
2. Mendaftarkan aplikasi 'main' ke variabel INSTALLED_APPS yang ada di dalam berkas `settings.py`


#### Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib (name, price, description)
1. Mengisi berkas `models.py` pada direktori aplikasi main dengan kode:
   ```
   from django.db import models

   class Product(models.Model):
      name = models.CharField(max_length=255)
      price = models.IntegerField()
      description = models.TextField()
   ```
2. Membuat migrasi model dengan perintah berikut:
   ```
   python manage.py makemigrations
   ```
3. Melakukan migrasi ke dalam basis data lokal dengan perintah berikut:
   ```
   python manage.py migrate
   ```


####  Membuat sebuah fungsi pada `views.py`
1. Membuat direktori baru bernama 'template' di dalam direktori aplikasi 'main'
2. Membuat berkas baru bernama 'main.html' dan menambahkan data-data seperti nama aplikasi, nama, dan kelas
3. Menambahkan fungsi `show_main` pada berkas `views.py` yang berisi dictionary yang berisi data (nama aplikasi, nama, dan kelas) untuk dikirimkan ke tampilan


#### Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`
1. Membuat berkas `urls.py` di dalam direktori `main` dan mengisi dengan:
   ```
   from django.urls import path
   from main.views import show_main

   app_name = 'main'
   
   urlpatterns = [
       path('', show_main, name='show_main'),
   ]
   ```
2. Membuka berkas `urls.py` di dalam direktori proyek `Zalohra` dan mengisi dengan:
   ```
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('main.urls')),
   ]
   ```

#### Melakukan _deployment_ ke PWS
1. Mengakses _website_ PWS dan membuat proyek baru bernama 'Zalohra'
2. Menambahkan URL _deployment_ PWS pada variabel ALLOWED_HOSTS yang ada di dalam berkas `settings.py` di proyek 'Zahlora'
3. Melakukan _add_, _commit_, dan _push_ lokal ke repositori GitHub
4. Menjalankan perintah pada _Project Command_ di halaman PWS
5. Menjalankan perintah ``` git branch -M main ``` untuk kembali mengubah nama _branch_ utama menjadi `main`
6. Lihat status _deployment_

### 2. Bagan Request Client ke Web Aplikasi Berbasis Django Beserta Responnya

### 3. Fungsi Git dalam Pengembangan Perangkat Lunak

### 4. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

### 5. Mengapa model pada Django disebut sebagai ORM?
