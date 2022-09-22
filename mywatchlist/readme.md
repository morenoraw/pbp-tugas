# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django
Projek ini dibuat untuk menyelesaikan tugas. Terdeploy di Heroku https://tugas2-morenoraw.herokuapp.com/mywatchlist/

# Jelaskan perbedaan antara JSON, XML, dan HTML!
* JSON (_JavaScript Object Notation_) merupakan suatu format yang dibuat dalam JavaScript untuk merepresentasikan data dalam bentuk key dan value dan digunakan untuk melakukan penyimpanan dan pertukaran data dengan cepat karena strukturnya yang dapat menyimpan data dalam bentuk array, namun sulit untuk dibaca oleh manusia.
* XML: XML (_eXtensible Markup Language_)  merupakan bentuk markup language yang menyimpan data dalam format teks sederhana seperti tree yang mirip dengan HTML untuk menyederhanakan proses penyimpanan dan pengiriman data antar server. Format ini cenderung mudah dibaca oleh manusia dibandingkan format JSON, namun pertukaran data akan lebih lama dari JSON.
* HTML: HTML  atau _Hyper Text Markup Language_ adalah bahasa markup yang digunakan untuk membuat halaman web. Bedanya _HTML_ dari _XML_ adalah penggunaannya untuk menampilkan data bukan untuk mengangkut data. _HTML_ adalah kombinasi dari _Hypertext_ dan bahasa _Markup_. _Hypertext_ mendefinisikan link antara halaman web. Bahasa markup digunakan untuk mendefinisikan dokumen teks dalam tag yang mendefinisikan struktur halaman web. Bahasa ini digunakan untuk membubuhi keterangan (membuat catatan untuk komputer) teks sehingga mesin dapat memahaminya dan memanipulasi teks yang sesuai.

# Alasan diperlukan data delivery dalam pengimplementasian platform
Karena ada client dan server, maka pada suatu platform seringkali terdapat pertukaran data antar mereka. Data delivery diperuntukkan untuk memudahkan suatu platform dalam melakukan pengiriman data. Format yang sering digunakan adalah diantara HTML, JSON, dan XML. Biasanya ada dua jenis data yang dipakai, yaitu data yang bersifat statis dan dinamis. Data yang statis merupakan data yang kemungkinan besar tidak akan diubah dan jarang diakses. Sementara data dinamis adalah data yang terupdate secara periodik. Dalam sebuah platform, tentunya informasi baru akan selalu ada. Pemrograman sangat berhubungan dengan informasi sehingga data biasanya bersifat dinamis. Oleh karena itu, kedinamisan data ini akan sangat terbantu oleh Data delivery (transmisi data).

# Langkah-langkah implementasi
1. Membuat Apps baru bernama mywatchlist lalu menambahkan path mywatchlist di direktori project_django pada file settings.py dan pada file urls.py

    ```shell
    INSTALLED_APPS = [
        ...
        'mywatchlist',
    ]
    ```

    ```shell
    urlpatterns = [
        ...
        path('katalog/', include('katalog.urls')),
        path('mywatchlist/', include('mywatchlist.urls')),
    ]

    ```

2. menambahkan sebuah class MyWatchList dengan parameter models.Model pada models.py yang ada pada direktori mywatchlist. yaitu:

    ```shell
    class WatchlistItem(models.Model):
        title = models.CharField(max_length=255)
        rating = models.FloatField()
        release_date = models.CharField(max_length=255)
        review = models.TextField()
        watched = models.TextField()
    ```

3. Membuat file bernama "initial_watchlist_data.json" dalam fixtures lalu menambahkan data sebagai objek dari model MyWatchList

4. Buka terminal (cmd) dan menjalankan perintah ini agar melakukan migrasi skema model ke database Django lokal:

   ```shell
   python manage.py makemigrations
   ```

   ```shell
   python manage.py migrate
   ```

5. Menjalankan perintah ini untuk mengambil data pada initial_watchlist_data.json pada database Django lokal:

   ```shell
   python manage.py loaddata initial_watchlist_data.json
   ```
   
6. Membuat file-file html yang ingin ditampilkan (mywatchlist.html)
7. Membuat fungsi pada file views.py yang berada di folder mywatchlist (show_watchlist, show_xml, show_json)
8. Membuat routing dengan cara menambahkan urlpatterns pada file urls.py di folder mywatchlist agar fungsinya bisa diakses dalam url tertentu
9. Menambahkan Class dan fungsi dalam test.py agar bisa unit test dan tidak ada masalah.

    ```shell
    # Contoh (format diganti sesuai formatnya)
    class WatchlistTestCases(TestCase):
    def test_format(self):
        response = Client().get('/mywatchlist/format/')
        self.assertEqual(response.status_code,200)
    ```

10. Menambahkan isi Procfile agar melakukan data delivery di aplikasi heroku.
    ```shell
    release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_watchlist_data.json'
    web: gunicorn project_django.wsgi --log-file -
    ```
11. Push ke GitHub dengan menjalankan
    ```shell
    git add -A
    git commit -m "Telah menyelesaikan Tugas 3."
    git push origin main
    ```
# Postman
## HTML
![image-html](https://github.com/morenoraw/pbp-tugas2/blob/main/image-html.png?raw=true)

## XML
![image-xml](https://github.com/morenoraw/pbp-tugas2/blob/main/image-xml.png?raw=true)

## JSON
![image-json](https://github.com/morenoraw/pbp-tugas2/blob/main/image-json.png?raw=true)