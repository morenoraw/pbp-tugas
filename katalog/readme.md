# Tugas 2 : Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Projek ini dibuat untuk menyelesaikan tugas.
Terdeploy di Heroku https://tugas2-morenoraw.herokuapp.com/

## 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![MVT Diagram](https://github.com/morenoraw/pbp-tugas2/blob/main/image.png?raw=true)

1. Pertama, *user* / *client* akan melakukan sebuah *request* ke server melalui tautan url atau form, lalu Django akan mencocokan url yang di-*request* dengan url yang sudah ada di **urls.py**.

2. Setiap url yang ada akan di *forward* ke fungsi yang berada di **views.py** yang akan memanggil fungsi *view*.

3. Fungsi view tersebut akan meng*query* database dengan memanggil objek yang ada di **models.py** untuk menghubung.

4. Lalu, fungsinya akan mengembalikan *response* berformat HTML.

5. Terakhir, hasilnya akan dirender oleh template yang akan menampilkan konten ke klien.

## 2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual Environment digunakan untuk membedakan *dependencies* dan *library* sehingga tidak akan merusak proyek atau sistem versi sebelumnya yang memiliki *dependencies* masing-masing atau lainnya.

Tanpa Virtual Environment, tentu bisa membuat aplikasi web berbasis Django, namun akan lebih berantakan dan kemungkinan kerusakan karena *overlap* *dependencies* setiap proyek lebih tinggi bila aplikasi tersebut 

## 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

1. Membuat sebuah fungsi pada **views.py** yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.

Dalam **views.py**, hal yang dilakukan adalah membuat fungsi show_katalog dengan parameter request dari user. Setelah itu, katalog.html akan dirender dengan context pengembalian fungsi render yang muncul di halaman HTML.

2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada **views.py**.

Routing dengan mengisi 'path('katalog/', include('katalog.urls'))' di **urls.py** di folder project_django.

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.

Dilakukan dengan mengambil data yang berada di konteks lalu dalam HTML menggunakan sintaks khusus seperti contohnya '{{nama}}'.

4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Deployment dilakukan melalui herokuapp. Dalam heroku, mengambil API Key dan nama aplikasi dan memasukkannya ke Secrets dalam github agar terhubung dengan repository.

## Identitas

Moreno Rassya Wibisana
2106752003