# Tugas 6: Javascript dan AJAX

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming adalah paradigma programming untuk sebuah aplikasi atau sistem yang tidak bisa diotak-atik di tengah jalan. Hal ini dikarenakan metode pemanggilan function atau request yang hanya bisa dilakukan satu-satu (synchronous). Contohnya, web yang synchronous ketika pagenya dibuka oleh user maka dia harus refresh untuk melihat perubahan yang baru.

Asynchronous programming adalah paradigma untuk sebuah sistem yang bisa update atau berubah tanpa harus dijalankan ulang. Hal ini dikarenakan sistem bisa multitasking dan menjalankan banyak hal sekaligus (sambil jalan sambil update). Contohnya, web yang asynchronous bisa mengubah tampilan sambil dibuka oleh user.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming adalah paradigma dimana program bergantung pada 'event' yang terjadi pada sistem atau aplikasi. Event yang dimaksud dapat berupa perubahan waktu, button click, button hover, key press, dll. Contohnya, pada tugas 6 kita membuat modal (yang sudah ada di html) yang hanya akan muncul jika tombol New Task dipencet.

## Jelaskan penerapan asynchronous programming pada AJAX.
Pemrograman asinkron di AJAX membuat penundaan pengambilan data dapat dihindari. Itu membuat pengguna dapat terus berinteraksi dengan halaman saat AJAX memproses permintaan di latar belakang. Kemudian, ketika server mengirimkan respons kembali, AJAX akan memperbarui data di halaman dengan mulus.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON, saya buat ini didalam views.py.
2. Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat. saya tambahkan di urls.
3. Lakukan pengambilan task menggunakan AJAX GET. Saya masukkan di todolist_ajax.html.
4. Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
6. Buatlah view baru untuk menambahkan task baru ke dalam database.
7. Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.
8. Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add
9. Tutup modal setelah penambahan task telah berhasil dilakukan.
10. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page. Saya lakukan dengan menambahkan fungsi async.