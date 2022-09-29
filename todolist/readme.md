# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
Projek ini dibuat untuk menyelesaikan tugas. Terdeploy di Heroku https://tugas-morenoraw.herokuapp.com/todolist/

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF adalah **Cross-Site Request Forgery**. **Request Forgery** adalah salah satu perbuatan untuk membuat suatu request namun dibuat-buat. Hal ini merupakan sebuah cara untuk melakukan sebuah kejahatan internet karena request yang dilakukan biasanya adalah request yang berbahaya. Maka dari itu, Django menyediakan sebuah fitur untuk melawan **CSRF Token** yang merupakan kode rahasia acak yang unik untuk setiap situs tertentu. Setiap form yang dikirimkan oleh web kepada user, akan dikirimkan bersama CSRF Token sebagai proteksi dari serangan web berbahaya yang meniru seperti behavior request asli.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Tentu bisa! form.as_table merupakan salah satu cara untuk memudahkan kita membuat form yang akan menerima input karena semuanya sudah di assign secara otomatis. Secara sekilas, caranya adalah diantara start tag dan end tag form, kita dapat mengisi dengan `<input><\input>` sesuai dengan isi form yang kita inginkan. Setelah itu tambahkan `<input>` yang memiliki type submit untuk mensubmit form tersebut.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
1. Dalam kasus ini, User akan memencet button yang sudah di link dengan suatu function pada `views.py`.
2. Lalu, akan di route ke sebuah function yang akan mendapatkan request dan returnnya render `forms.html` yang akan menerima input user
3. Kemudian data yang diberikan user pada forms diambil kepada function lalu ditampilkan pada `show_todolist`.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
Saya melakukan ini dengan membuat aplikasi baru pada django kemudian masukkan nama apps pada `settings.py` di `project_django`.
2. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
Menambahkan alamat di `urls.py` yang berada di `project.django`.
3. Membuat sebuah model Task yang memiliki atribut sebagai berikut:
a. user untuk menghubungkan task dengan pengguna yang membuat task tersebut.
b. date untuk mendeskripsikan tanggal pembuatan task.
c. title untuk mendeskripsikan judul task.
d. description untuk mendeskripsikan deskripsi task.
Saya membuat model ini di `models.py`, lalu saya masukkan ke class Task yang berisikan hal-hal tersebut.
4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
Saya menambahkan fungsi di `views.py` dan halaman di templates mengenai registrasi juga login dan logout.
5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
Halaman utama tersebut saya buat dalam folder `templates`.
6. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
Maka dari itu, saya membuat class baru yang bernama `TaskAdd` dalam `taskform.py`.
7. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:
`http://localhost:8000/todolist` berisi halaman utama yang memuat tabel task.
`http://localhost:8000/todolist/login` berisi form login.
`http://localhost:8000/todolist/register` berisi form registrasi akun.
`http://localhost:8000/todolist/create-task` berisi form pembuatan task.
`http://localhost:8000/todolist/logout` berisi mekanisme logout.
Hal-hal ini saya lakukan kepada `urls.py` yang berada di aplikasi.
8. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Saya melakukan push seperti biasa ke git yang telah saya buat, karena saya sudah setup sebelumnya di secrets -> HEROKU_API_KEY & HEROKU_APP_NAME. Sekarang saya mengganti ke aplikasi `tugas-morenoraw` karena agar namanya rapih dan tidak terpaku kepada tugas ke 2.
9. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.<br>
Akun 1: username = morenoraw, password = Moreno123 <br>
Akun 2: username = morenoraws, password = Moreno123