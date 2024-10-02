# ZALOHRA

Proyek Django sebagai tugas mata kuliah Pemrograman Berbasis Platform (PBP) Ganjil 2024/2025 oleh Rizqya Az Zahra Putri - 2306244936.

🔗 Tautan PWS _deployment_: [Zalohra](http://rizqya-az-zalohra.pbp.cs.ui.ac.id/)

### Daftar Isi
* [Tugas 2: Implementasi Model-View-Template (MVT) pada Django](#tugas-2-implementasi-model-view-template-mvt-pada-django)
* [Tugas 3: Implementasi Form dan Data Delivery pada Django](#tugas-3-implementasi-form-dan-data-delivery-pada-django)
* [Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django](#tugas-4-implementasi-autentikasi-session-dan-cookies-pada-django)
  
---
## Tugas 2: Implementasi Model-View-Template (MVT) pada Django
### 1. Langkah Implementasi
#### Membuat sebuah proyek Django baru.
1. Membuat direktori lokal bernama 'Zalohra' lalu masuk ke dalam direktori tersebut
2. Membuka _command prompt_ dan membuat _virtual environment_ dengan menjalankan perintah:
   ```python
   py -m venv env
   ```
3. Mengaktifkan _virtual environment_ menggunakan perintah:
   ```python
   env\Scripts\activate
   ```
4. Masih di direktori lokal, membuat file `requirements.txt` yang berisi daftar _dependencies_ yang akan diperlukan.
   ```python
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```
5. Melakukan instalasi terhadap _dependencies_ dengan perintah:
   ```python
   pip install -r requirements.txt
   ```
6. Membuat proyek Django bernama 'Zalohra' dengan perintah:
   ```python
   django-admin startproject Zalohra .
   ```
7. Menambahkan string pada ALLOWED_HOST di `settings.py` untuk keperluan _deployment_:
   ```python
   ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   ```
8. Membuat repositori baru di GitHub dengan nama 'Zalohra'
9. Menambahkan berkas `.gitignore`
10. Membuat _branch_ utama baru dengan nama `main` menggunakan perintah:
    ```python
    git branch -M main
    ```
11. Menghubungkan direktori lokal dengan repositori di GitHub menggunakan perintah:
    ```python
    git remote add origin https://github.com/rizqyazzahra/Zalohra.git
    ```
12. Melakukan _add_, _commit_, dan _push_ dari direktori lokal ke repositori GitHub


#### Membuat aplikasi dengan nama `main` pada proyek tersebut.
1. Di direktori utama Zalora, membuat aplikasi baru bernama `main` menggunakan perintah:
   ```python
   python manage.py startapp main
   ```
2. Mendaftarkan aplikasi `main` ke variabel INSTALLED_APPS yang ada di dalam berkas `settings.py`


#### Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib (name, price, description)
1. Mengisi berkas `models.py` pada direktori aplikasi main dengan kode:
   ```python
   from django.db import models

   class Product(models.Model):
      name = models.CharField(max_length=255)
      price = models.IntegerField()
      description = models.TextField()
   ```
2. Membuat migrasi model dengan perintah berikut:
   ```python
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
   ```python
   from django.urls import path
   from main.views import show_main

   app_name = 'main'
   
   urlpatterns = [
       path('', show_main, name='show_main'),
   ]
   ```
2. Membuka berkas `urls.py` di dalam direktori proyek `Zalohra` dan mengisi dengan:
   ```python
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


---
## Tugas 3: Implementasi Form dan Data Delivery pada Django
### 1. Jelaskan mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?
_Data delivery_ sangat penting dalam pengimplementasian platform karena memegang peran dalam memastikan pengiriman data dari server ke _client_ dan sebaliknya berjalan secara efisien, cepat, dan aman. Hal ini mendukung responsivitas platform, memberikan akses informasi _real-time_, serta menjaga keamanan data melalui enkripsi dan autentikasi. Selain itu, _data delivery_ mengoptimalkan kinerja jaringan, memastikan sinkronisasi data antar pengguna atau sistem, dan membantu mengelola lalu lintas data agar tidak terjadi keterlambatan, terutama saat melayani pengguna dalam jumlah besar.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Jika membandingkan XML dengan JSON tentunya memiliki kelebihan dan kekurangannya masing-masing. JSON sendiri lebih populer daripada XML karena sintaksnya yang lebih sederhana dan ringkas membuat lebih mudah dibaca, diproses, dan diintegrasikan dengan berbagai aplikasi web modern dan bahasa pemrograman, terutama JavaScript. Sementara XML memiliki kompleksitas yang lebih tinggi, sehingga lebih cocok untuk skenario tertentu yang memerlukan struktur data yang lebih kompleks dan validasi data yang ketat.

### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django memiliki fungsi untuk memvalidasi data yang telah diinput pengguna ke dalam form. Hal ini dilakukan dengan mengecek apakah data sesuai dengan aturan validasi yang didefinisikan pada field dalam form. Jika data valid, method ini akan mengembalikan nilai `True` dan jika tidak valid, maka akan mengembalikan nilai `False`.

Method ini dibutuhkan untuk mencegah penyimpanan data yang tidak valid ke dalam database, menjaga integritas data, dan mempermudah pengelolaan jika ada error saat dimasukkan data yang tidak sesuai.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` merupakan sebuah random _secure_ token sebagai lapisan validasi tambahan yang unik per sesi pengisian form dan terdiri dari nilai yang besar agar sulit ditebak oleh penyerang. `csrf_token` ini digunakan untuk melindungi aplikasi web dari serangan _Cross-Site Request Forgery_ (CSRF). Serangan CSRF terjadi ketika penyerang mengirimkan permintaan berbahaya ke server atas nama pengguna yang telah terautentikasi tanpa sepengetahuan mereka. Jika kita tidak menambahkan `csrf_token`,  server tidak dapat membedakan permintaan yang diterima berasal dari sumber yang sah atau bukan, sehingga penyerang dapat menyalahgunakan sesi pengguna untuk melakukan tindakan yang tidak diinginkan.

Penyerang memanfaatkan hal tersebut dengan:
- Mengubah pengaturan akun pengguna tanpa sepengetahuan pengguna
- Membuat sebuah form di situs berbahaya yang secara diam-diam mengirimkan permintaan ke aplikasi Django target, menggunakan kredensial pengguna yang sedang login, untuk melakukan tindakan seperti mengubah password, melakukan transaksi, atau menghapus data tanpa sepengetahuan pengguna

### 5. Langkah Implementasi _Checklist_
#### Membuat input `form`
1. Membuat `forms.py` di direktori `main` dengan isi
   ```python
   from django.forms import ModelForm
   from main.models import Product

   class ProductForm(ModelForm):
       class Meta:
           model = Product
           fields = ["name", "price", "description", "image"]
   ```
2. Menambahkan beberapa _import_ pada berkas `views.py` di direktori `main`
   ```python
   from django.shortcuts import render, redirect   # Menambahkan import redirect
   from main.forms import ProductForm
   from main.models import Product
   ```
3. Menambahkan method `create_product` untuk menambah entri database di file `views.py` di direktori `main`
   ```python
   def create_product(request):
      form = ProductForm(request.POST or None)

      if form.is_valid() and request.method == "POST":
         form.save()
         return redirect('main:show_main')

         context = {'form': form}
         return render(request, "create_product.html", context)
   ```
4. Mengubahlah fungsi `show_main` yang ada pada berkas `views.py`
   ```python
   def show_main(request):
      products = Product.objects.all()

      context = {
         'apps_name' : 'Zalohra',
         'name': 'Rizqya Az Zahra Putri',
         'class': 'PBP F',
         'products': products
      }
      return render(request, "main.html", context
   ```
5. Meng-_import_ fungsi `create_product` pada berkas `urls.py` yang ada pada direktori `main` dan routing URL ke dalam variabel `urlpatterns` pada `urls.py` di `main`
   ```python
   from main.views import show_main, create_product

   ...
   urlpatterns = [
      ...
      path('create-product', create_product, name='create_product'),
   ]
   ```
6. Memuat berkas HTML baru dengan nama `create_product.html` pada direktori `main/templates` dan isi dengan
   ```python
   {% extends 'base.html' %} 
   {% block content %}
   <h1>Add New Product</h1>
   
   <form method="POST">
     {% csrf_token %}
     <table>
       {{ form.as_table }}
       <tr>
         <td></td>
         <td>
           <input type="submit" value="Add Product" />
         </td>
       </tr>
     </table>
   </form>
   
   {% endblock %}
   ```
7. Menambahkan folder `templates` di direktori utama dan membuat `base.html` sebagai basis dari laman-laman lain
8. Menambahkan lokasi folder `templates` tersebut ke variabel `TEMPLATES` yang ada di berkas `settings.py` pada direktori proyek `Zalohra`
   ```python
   ...
   'DIRS': [BASE_DIR / 'templates'],
   ...
   ```
9. Mengimplementasikan database ke dalam laman utama `main.html` dan juga menjadi perpanjangan dari `base.html` di direktori utama

#### Menambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML _by ID_, dan JSON _by ID_
1. Meng-_import_ HttpResponse dan Serializer pada berkas `views.py` di direktori `main`
   ```python
   from django.http import HttpResponse
   from django.core import serializers
   ```
2. Menambahkan fungsi-fungsi yang diperlukan untuk menampilkan XML dan JSON
   ```python
   def show_xml(request):
      data = Product.objects.all()

   def show_json(request):
       data = Product.objects.all()
   
   def show_xml_by_id(request, id):
       data = Product.objects.filter(pk=id)
   
   def show_json_by_id(request, id):
       data = Product.objects.filter(pk=id)
    ```
3. Menambahkan _return function_ berupa `HttpResponse`
   ```python
   def show_xml(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   
   def show_xml_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   
   def show_json_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

#### Membuat routing URL untuk masing-masing `views` yang telah ditambahkan
Menambahkan URL routing di dalam `urls.py` yang ada di direktori `main`
```python
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
...
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```


### 💻 Hasil Akses URL pada Postman
#### XML
![Screenshot (1336)](https://github.com/user-attachments/assets/07bf2145-1c7d-486c-b4d5-c4979d900dc3)

#### JSON
![Screenshot (1337)](https://github.com/user-attachments/assets/1e5c4157-bd9f-49f7-bf2e-aa658d1400eb)

#### XML by ID
![Screenshot (1339)](https://github.com/user-attachments/assets/e4164752-2c46-45d6-a6bc-f8286b0a79a2)

#### JSON by ID
![Screenshot (1340)](https://github.com/user-attachments/assets/817bb3c5-8231-41de-a1ae-3b5fcf5a45fd)

---
## Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django
### 1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`?
* `HttpResponseRedirect()` merupakan kelas bawaan Django yang mengembalikan respons HTTP 302 untuk mengarahkan pengguna (_redirect_) ke URL tertentu. Untuk penggunaannya, biasanya perlu menyertakan URL secara eksplisit sebagai string dalam parameter.
* `redirect()` merupakan _shortcut function_ dari Django yang digunakan untuk mengalihkan pengguna ke URL tertentu dan mengembalikan respons HTTP yang fungsinya sama seperti `HttpResponseRedirect()`. Namun, `redirect()` lebih fleksibel dan mudah digunakan karena dapat menerima berbagai tipe argumen seperti nama URL, nama view, atau objek model.

### 2. Jelaskan cara kerja penghubungan model `Product` dengan `User`!
Penghubungan model `Product` dengan `User` dilakukan dengan menggunakan `ForeignKey`. `ForeignKey` menghubungkan tiap objek `Product` dengan satu user melalui sebuah relasi, dimana sebuah _product_ pasti terasosiasikan dengan seorang user dan satu user dapat memiliki banyak _product_ (relasi _many-to-one_).
Contoh:
```python
from django.contrib.auth.models import User

class Product(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   ...
```
`ForeignKey` menunjukkan bahwa setiap `Product` terkait dengan satu `User` yang membuat atau memiliki produk tersebut. `on_delete=models.CASCADE` memastikan bahwa jika pengguna user, maka semua produk yang terkait juga akan dihapus.

### 3. Apa perbedaan antara _authentication_ dan _authorization_, apakah yang dilakukan saat pengguna _login_? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
_Authentication_ adalah proses memverifikasi identitas pengguna, biasanya dengan memeriksa kredensial seperti _username_ dan _password_. Sedangkan _authorization_ adalah proses untuk menentukan hak akses pengguna terhadap _resource_ setelah autentikasi. Biasanya melibatkan pengecekan apakah pengguna memiliki izin untuk melakukan tindakan tertentu seperti melihat halaman, mengedit data, atau mengakses fitur khusus.

Saat pengguna _login_, _authentication_ dilakukan untuk memastikan bahwa identitas yang mereka masukkan sesuai dengan data di _database_. Setelah proses _authentication_ berhasil, dalam kata lain pengguna berhasil _login_, Django melakukan _authorization_ dengan memeriksa izin pengguna setiap kali mereka mencoba mengakses halaman atau fitur yang membutuhkan otorisasi. Django akan melihat apakah mereka memiliki hak akses _resource_ tertentu.

Django mengimplementasikan _authentication_ menggunakan sistem autentikasi bawaan yang menangani login dan logout pengguna, seperti `authenticate()` dan `login()`. Sementara untuk _Authorization_, Django memiliki sistem _permissions_ bawaan yang mengelola izin dan peran pengguna yang dapat diatur pada view atau model tertentu, menggunakan _decorator_ seperti `@login_required` dan `@permission_required`.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari _cookies_ dan apakah semua _cookies_ aman digunakan?
Django mengingat pengguna yang telah _login_ menggunakan sesi yang disimpan dalam _cookies_. Ketika pengguna _login_, Django membuat _session_ untuk pengguna dan menyimpan _session_ ID di _cookies_ dalam browser pengguna. _Cookies_ ini yang memungkinkan Django untuk mengenali pengguna saat mereka kembali ke aplikasi. Saat pengguna mengunjungi halaman lain, _cookie_ dikirimkan ke server dan Django membaca _session_ ID dari cookie dan mengaitkan _session_ tersebut dengan pengguna yang telah _login_ atau diautentikasi.

Kegunaan lain dari _cookies_, yaitu melacak aktivitas pengguna, mempersonalisasi konten pengguna, dan menyimpan pengaturan atau preferensi pengguna, seperti bahasa, mode gelap atau terang, atau preferensi tampilan lainnya.

Untuk aspek keamanan, tidak semua _cookies_ aman. Ada beberapa risiko terkait dengan penggunaan _cookies_. _Third-party tracking cookies_ sering digunakan untuk melacak pengguna di berbagai situs tanpa sepengetahuan mereka, yang menimbulkan masalah privasi. Selain itu, _cookies_ yang tidak dilindungi dengan baik dapat rentan terhadap serangan _Cross-Site Scripting_ (XSS) dan _Cross-Site Request Forgery_ (CSRF). Maka dari itu, untuk memastikan _cookies_ lebih aman perlu memberi _cookies_ atribut `HTTPOnly` untuk mencegah akses _cookies_ melalui JavaScript dan juga atribut `Secure` untuk memastikan _cookie_ hanya dikirimkan melalui koneksi terenkripsi (HTTPS).

### 5. Langkah Implementasi _Checklist_
#### Mengimplementasikan fungsi registrasi, login, dan logout
* Registrasi
  1. Membuat fungsi dan form registrasi dengan menambahkan _import_ `UserCreationForm` dan `messages` serta fungsi `register` pada `views.py` pada subdirektori `main`
     ```python
      from django.contrib.auth.forms import UserCreationForm
      from django.contrib import messages
      ...
      def register(request):
         form = UserCreationForm()
   
         if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
               form.save()
               messages.success(request, 'Your account has been successfully created!')
               return redirect('main:login')
         context = {'form':form}
         return render(request, 'register.html', context)
      
      ```
  2. Membuat berkas baru `register.html` pada direktori `main/templates` untuk menampilkan form registrasi.
* Login
  1. Membuat fungsi `login_user` dan meng-_import_ `authenticate`, `login`, dan `AuthenticationForm` pada `views.py`
     ```python
     from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
     from django.contrib.auth import authenticate, login
     ...
     def login_user(request):
        if request.method == 'POST':
           form = AuthenticationForm(data=request.POST)
   
           if form.is_valid():
               user = form.get_user()
               login(request, user)
               return redirect('main:show_main')
   
        else:
           form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
     ```
  2. Membuat berkas baru bernama `login.html` pada direktori `main/templates` untuk menampilkan form _login_.
* Logout
  1. Menambahkan fungsi `logout_user` dan meng-_import_ `logout` pada `views.py` yang berisi
     ```python
     from django.contrib.auth import logout
     ...
     def logout_user(request):
        logout(request)
        return redirect('main:login')
     ```
  3. Menambahkan _button_ untuk logout di berkas `main.html`
     
  Kemudian melakukan _routing_ dengan meng-import `register`, `login`, dan `logout` pada berkas `urls.py` di subdirektori `main`
  ```python
  from main.views import register, login_user, logout_user
  ...
  urlpatterns = [
     ...
     path('register/', register, name='register'),
     path('login/', login_user, name='login'),
     path('logout/', logout_user, name='logout'),
      ]
  ```

  Setelah halaman register, login, dan logout dapat diakses, menambahkan kode berikut pada berkas `views.py` untuk merestriksi akses user ke halaman utama.
  ```python
  from django.contrib.auth.decorators import login_required
     ...
  
      @login_required(login_url='/login')
      def show_main(request):
        ...
  ```

####  Membuat dua akun pengguna dengan masing-masing tiga _dummy data_ di lokal
Untuk membuat dua akun, cukup dengan melakukan dua kali registrasi user dengan akun yang berbeda. Saya membuat dua akun dengan username `RizqyaAzZahraPutri` dan `RizqyaAzZahra`, lalu menambahkan tiga data untuk setiap akunnya.
* Bukti pembuatan akun dan _dummy data_
  ##### User 1 (RizqyaAzZahraPutri)
  ![Screenshot 2024-09-24 200952](https://github.com/user-attachments/assets/8a1d3847-3333-412b-bf40-d90f90d24805)
  
  ##### User 2 (RizqyaAzZahra)
  ![Screenshot 2024-09-24 200221](https://github.com/user-attachments/assets/ab289dbb-7b5b-44f6-a79c-7b6a6687a37a)

####  Menghubungkan model `Product` dengan `User`
1. Menambahkan kode berikut pada berkas `models.py` di direktori `main`
   ```python
   from django.contrib.auth.models import User
   ...

   class Product(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      ...
   ```
2. Mengubah potongan kode pada fungsi `create_product` di `views.py`
   ```python
   def create_product(request):
      form = ProductForm(request.POST or None)

      if form.is_valid() and request.method == "POST":
         product = form.save(commit=False)
         product.user = request.user
         product.save()
         return redirect('main:show_main')

      context = {'form': form}
      return render(request, "create_product.html", context)
   ```
3. Mengubah value dari `products` dan `context` pada fungsi `show_main` menjadi
   ```python
   def show_main(request):
      products = Product.objects.filter(user=request.user)

      context = {
        'apps_name' : 'Zalohra',
        'name': request.user.username,
        ...
      }
   ```
4. Melakukan migrasi model
5. Meng-_import_ `os` dan mengganti variabel DEBUG di berkas `settings.py` menjadi sebagai berikut
   ```python
   import os
   ...
   PRODUCTION = os.getenv("PRODUCTION", False)
   DEBUG = not PRODUCTION
   ...
   ```

####  Menampilkan detail informasi pengguna yang sedang _logged in_ seperti _username_ dan menerapkan `cookies`
1. Meng-_import_ beberapa modul dan memodifikasi fungsi `login_user` pada blok `if form.is_valid()` menjadi sebagai berikut
   ```python
   import datetime
   from django.http import HttpResponseRedirect
   from django.urls import reverse
   ...
   def login_user(request):
       ...
       if form.is_valid():
           user = form.get_user()
           login(request, user)
           response = HttpResponseRedirect(reverse("main:show_main"))
           response.set_cookie('last_login', str(datetime.datetime.now()))
           return response
   ...
   ```
2. Menambahkan potongan kode berikut ke dalam variabel `context`
   ```python
   context = {
      ...
      'last_login': request.COOKIES['last_login'],
   }
   ```
3. Memodifikasi fungsi `logout_user` menjadi seperti ini
   ```python
   def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
   ```
4. Menambahkan potongan kode berikut pada berkas `main.html`
   ```python
   ...
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ...
   ```   

## Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS
### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
1. Inline CSS, yang ditulis langsung pada elemen HTML menggunakan atribut style, memiliki prioritas tertinggi. Contoh:
   ```python
   <h1 style="color: blue;">Judul</h1>
   ```
2. ID selectors: Selector yang menggunakan ID elemen (misalnya `#header`). Hanya berlaku untuk elemen dengan ID tertentu. Memiliki prioritas yang lebih tinggi daripada class dan element selector. Contoh:
   ```python
   #header { color: white; }
   ```
3. Class selectors, attribute selectors, dan pseudo-class selectors: Selector berbasis class (`.class`), attribute (`[type="text"]`), dan pseudo-class (`:hover`, `:focus`) memiliki prioritas yang lebih rendah daripada ID, tetapi lebih tinggi daripada tag/element selectors. Contoh:
   ```python
   .content { color: green; }
   ```
4. Element (type) selectors dan pseudo-elements: Selector berbasis elemen HTML (misalnya `div`, `p`, `h1`) serta pseudo-elements (`::before`, `::after`) memiliki prioritas rendah.
   ```python
   Contoh: p { color: green; }
   ```
5. Universal selectors (`*`) memiliki prioritas terendah.


### 2. Mengapa _responsive design_ menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan _responsive design_!
_Responsive design_ menjadi konsep penting dalam pengembangan aplikasi web karena kebutuhan untuk membuat situs web atau aplikasi dapat diakses dengan optimal di berbagai perangkat dengan ukuran layar yang berbeda, seperti _desktop_, _smartphone_, dan tablet guna meningkatkan pengalaman pengguna di semua perangkat.

Contoh aplikasi yang sudah menerapkan _responsive design_:
* YouTube
* Pinterest
* Instagram

Contoh aplikasi yang belum menerapkan _responsive design_:
* 

### 3. Jelaskan perbedaan antara _margin_, _border_, dan _padding_, serta cara untuk mengimplementasikan ketiga hal tersebut!
* **Margin**, yaitu ruang kosong di luar elemen, yang memisahkan elemen tersebut dari elemen lain. Berfungsi untuk mengatur jarak antara elemen satu dengan yang lain.
* **Border**, yaitu garis yang mengelilingi elemen, berada di antara margin dan padding.
Berfungsi untuk memberi bingkai atau batas visual pada elemen.
* **Padding**, yaitu ruang di dalam elemen, antara konten elemen dan border. Padding juga dapat memiliki warna yang sama dengan _background_ elemen. Berfungi untuk memberi jarak antara konten elemen (seperti teks atau gambar) dengan border elemen.

Cara implementasi:
```python
.element {
    margin: 20px;
    padding: 15px;
    border: 2px solid black;
}
```

### 4. Jelaskan konsep _flex box_ dan _grid layout_ beserta kegunaannya!
**_Flexbox_** adalah metode tata letak satu dimensi, yang berarti mengatur elemen secara linear, baik secara horizontal (baris) atau vertikal (kolom).
Kegunaan _Flexbox_:
* Mengatur item dalam satu baris atau kolom.
* Mengatur tata letak yang fleksibel, seperti menu navigasi, galeri gambar, atau bagian konten yang disusun dalam satu dimensi (baris atau kolom).
* Membuat tata letak yang responsif tanpa perlu menggunakan properti _float_ atau _positioning_.

  **_Grid Layout_** adalah metode tata letak dua dimensi, yang memungkinkan untuk mengatur elemen dalam baris dan kolom. _Grid_ lebih kompleks dibandingkan _flexbox_ dan memberikan kontrol yang lebih mendetail dalam mengatur struktur elemen secara vertikal dan horizontal.
Kegunaan _Grid Layout_:
* Mengatur tata letak halaman web yang lebih kompleks di mana posisi elemen harus dikelola dalam dua dimensi (baris dan kolom).

### 5. Langkah Implementasi _Checklist_
####  Implementasi fungsi untuk menghapus dan mengedit _product_.
1. Membuat fungsi baru dengan nama `edit_product` dan `delete_product` pada `views.py` di folder `main`
   ```pyhton
   ...
   def edit_product(request, id):
     product = Product.objects.get(pk = id)
     form = ProductForm(request.POST or None, instance=product)

     if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

     context = {'form': form}
     return render(request, "edit_product.html", context)

   def delete_product(request, id):
        product = Product.objects.get(pk = id)
        product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
   ```
2. Tambahkan _import_ pada file `views.py`
   ```python
   from django.shortcuts import .., reverse
   from django.http import .., HttpResponseRedirect
   ```
3. Membuat berkas HTML baru dengan nama `edit_product.html` pada subdirektori `main/templates`
   ```python
   {% extends 'base.html' %}
    {% load static %}    
    {% block content %}    
    <h1>Edit Product</h1>
    
    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Edit Product"/>
                </td>
            </tr>
        </table>
    </form>
    
    {% endblock %}
   ```
4. Melakukan _routing_ dengan _import_ dan menambahkan _path url_.
   ```python
   from main.views import edit_product, delete_product
   ...
   urlpatterns = [
     ...
     path('edit-product/<uuid:id>', edit_product, name='edit_product'),
     path('delete/<uuid:id>', delete_product, name='delete_product'),
   ]
   ```
5. Menambahkan potongan code sebagai berikut agar tombol yang sudah dibuat muncul pada halaman web.
   ```python
   ...
    <tr>
        ...
        <td>
            <a href="{% url 'main:edit_product' product.pk %}">
                <button>
                    Edit
                </button>
            </a>
        </td>
        <td>
            <a href="{% url 'main:delete_product' product.pk %}">
                <button>
                    Delete
                </button>
            </a>
        </td>
    </tr>
    ...
   ```


#### Kustomisasi desain pada template HTML
1. Karena saya menggunakan Tailwind untuk _styling_ aplikasi Zalohra, saya pertama menyambungkan template django dengan taiwind dengan menambahkan script CDN tailwind di file `base.html`
```python
<head>
{% block meta %}
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
{% endblock meta %}
<script src="https://cdn.tailwindcss.com">
</script>
</head>
```
2. Konfigurasi static files, pada `settings.py` menambahkan _middleware_ WhiteNoise.
   ```python
   ...
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
        ...
    ]
    ...
   ```
3. Memastikan variabel `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL` sudah dikonfigurasikan
   ```python
   ...
    STATIC_URL = '/static/'
    if DEBUG:
        STATICFILES_DIRS = [
            BASE_DIR / 'static'
        ]
    else:
        STATIC_ROOT = BASE_DIR / 'static' 
    ...
   ```
4. Membuat file 'global.css' di `/static/css` pada root directory dan dihubungkan dengan script Tailwind di `base.html`
   ```python
   ...
   <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
   ...
   ```
#### Kustomisasi halaman _login_, _register_, dan tambah _product_.

#### Kustomisasi halaman daftar _product_.

#### Membuat dua buah _button_ untuk mengedit dan menghapus _product_ pada setiap _card product_

#### Membuat _responsive navigation bar_
1. Membuat berkas HTML baru dengan nama `navbar.html` pada folder `templates/` di root directory dan diisi dengan template yang diinginkan
2. Menautkan `navbar` ke dalam `main.html`, `create_product.html`, dan `edit_product.html` yang berada di subdirektori `main/templates/`, seperti ini:
   ```python
   {% extends 'base.html' %}
   {% block content %}
   {% include 'navbar.html' %}
   ...
   {% endblock content%}
   ```
