# ZALOHRA

Proyek Django sebagai tugas mata kuliah Pemrograman Berbasis Platform (PBP) Ganjil 2024/2025 oleh Rizqya Az Zahra Putri - 2306244936.

🔗 Tautan PWS _deployment_: [Zalohra](http://rizqya-az-zalohra.pbp.cs.ui.ac.id/)

---
## Tugas 2: Implementasi Model-View-Template (MVT) pada Django
### 1. Langkah Implementasi
#### Membuat sebuah proyek Django baru.
1. Membuat direktori lokal bernama 'Zalohra' lalu masuk ke dalam direktori tersebut
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
7. Menambahkan string pada ALLOWED_HOST di `settings.py` untuk keperluan _deployment_:
   ```
   ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   ```
8. Membuat repositori baru di GitHub dengan nama 'Zalohra'
9. Menambahkan berkas `.gitignore`
10. Membuat _branch_ utama baru dengan nama `main` menggunakan perintah:
    ```
    git branch -M main
    ```
11. Menghubungkan direktori lokal dengan repositori di GitHub menggunakan perintah:
    ```
    git remote add origin https://github.com/rizqyazzahra/Zalohra.git
    ```
12. Melakukan _add_, _commit_, dan _push_ dari direktori lokal ke repositori GitHub


#### Membuat aplikasi dengan nama `main` pada proyek tersebut.
1. Di direktori utama Zalora, membuat aplikasi baru bernama `main` menggunakan perintah:
   ```
   python manage.py startapp main
   ```
2. Mendaftarkan aplikasi `main` ke variabel INSTALLED_APPS yang ada di dalam berkas `settings.py`


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
1. Membuat direktori baru bernama `template` di dalam direktori aplikasi `main`
2. Membuat berkas baru bernama `main.html` dan menambahkan data-data seperti nama aplikasi, nama, dan kelas
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
2. Menambahkan URL _deployment_ PWS pada variabel ALLOWED_HOSTS yang ada di dalam berkas `settings.py` di proyek 'Zalohra'
3. Melakukan _add_, _commit_, dan _push_ lokal ke repositori GitHub
4. Menjalankan perintah pada _Project Command_ di halaman PWS
5. Menjalankan perintah ``` git branch -M main ``` untuk kembali mengubah nama _branch_ utama menjadi `main`
6. Lihat status _deployment_


### 2. Bagan Request Client ke Web Aplikasi Berbasis Django Beserta Responnya
<img width="1924" alt="PBP tugas 2" src="https://github.com/user-attachments/assets/72500c30-30a3-4918-add3-9f4d540134d0">

Client (browser) akan mengirimkan request ke server. Lalu, server menerima request dan memprosesnya melalui web server. Permintaan diarahkan ke urls.py yang tugasnya memetakan URL dari request ke fungsi yang sesuai di views.py. Di views.py, request ditangani dan akan berinteraksi dengan models.py untuk mengambil atau menyimpan data ke basis data. Jika diperlukan, view akan menggunakan template HTML yang akan dikirimkan kembali ke client. Setelah data diproses dan template di-render, view akan menghasilkan respons. Respons ini akan ditampilkan oleh browser.


### 3. Fungsi Git dalam Pengembangan Perangkat Lunak
* Git memungkinkan _developer_ perangkat lunak untuk melacak setiap perubahan yang dilakukan pada kode proyek dan memulihkan versi kode sebelumnya jika diperlukan
* Git memfasilitasi agar dapat melakukan kolaborasi pengembangan proyek yang sama dengan banyak orang melalui kemampuan untuk mengelola _branch_ yang berbeda dan menggabungkan perubahan (_merge_) dengan aman kembali ke _branch_ utama dengan aman.
* Git yang memiliki sistem terdistribusi memungkinkan _developer_ untuk memiliki salinan lengkap dari seluruh riwayat proyek. Hal ini memungkinkan pekerjaan tanpa terhubung ke server pusat.
 

### 4. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django seringkali dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena memiliki struktur yang terorganisir dan mudah dipahami oleh pemula, yaitu arsitektur Model-View-Template (MVT) yang memisahkan logika aplikasi, interaksi database, dan antarmuka pengguna. Tak hanya itu, Django juga menyediakan banyak fitur bawaan yang dapat memudahkan dalam pengembangan perangkat lunak dengan cepat. Keamanan yang dirancang dengan baik dan fitur yang banyak dan beragam memudahkan pemula untuk belajar sambil membangun aplikasi yang aman.


### 5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena menyediakan cara untuk berinteraksi dengan basis data menggunakan objek Python daripada menulis _query_ SQL secara langsung. ORM memungkinkan pengembang untuk mendefinisikan struktur basis data dalam bentuk Python, di mana setiap kelas mewakili tabel dan atributnya mewakili kolom. Hal ini membuat interaksi dengan basis data jadi lebih mudah.
