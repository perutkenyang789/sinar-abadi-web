# Welcome to Toko Sinar Abadi
<h4>Website URL: http://ida-made-sinarabadi.pbp.cs.ui.ac.id/</h4>

---

<h2>Checklist Implementation Process</h2>
1. Membuat repositori di GitHub dengan nama **`sinar-abadi-web`**.
1. Membuat repositori lokal di laptop saya dengan nama **`Tugas 2`**.
1. Menghubungkan repositori lokal dengan repositori online di GitHub.
1. Meng-install dependencies melalui `requirements.txt`:
    ```bash
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
1. Memulai project menggunakan perintah:
    ```bash
    django-admin startproject mental_health_tracker
    ```
1. Memulai project baru di PWS dan melakukan deploy project di [website](http://ida-made-sinarabadi.pbp.cs.ui.ac.id/).
1. Mengubah bagian `ALLOWED_HOSTS` pada `settings.py` menjadi:
    ```python
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "ida-made-sinarabadi.pbp.cs.ui.ac.id"]
    ```
1. Membuat aplikasi baru dengan nama **`main`**.
1. Membuat template dasar di file `main.html`.
1. Membuat model **`Product`** dengan atribut `name`, `price`, `description`, dan `color`.
1. Mengintegrasikan View dan Template dalam komponen Model-View-Template (MVT).
1. Mengonfigurasi URL di aplikasi **`main`** dan proyek secara keseluruhan.

<h2>Fungsi git dalam pengembangan perangkat lunak</h2>
'Git' merupakan sebuah Version Control System. 'Git' bukanlah satu-satunya Version Control System yang ada. Contoh lainnya adalah 'Helix Core'. Yang penting dalam pengembangan perangkat lunak ini adalah Version Control System ini. Version Control System sangat essential dalam workflow pengembangan perangkat lunak. Version Control System mendukung proses kerja sama dalam pengembangan perangkat lunak dengan memastikan setiap anggota tim dapat mengakses versi terbaru dari file yang telah dikerjakan juga oleh anggota lain dalam tim. Seluruh file ini akan dikumpulkan menjadi satu para repositori utama yang bertindak sebagai server.
Apabila kita ambil 'Git' sebagai contoh, 'Git' adalah sebuah Distributed Version Control System yang membuat setiap anggota dalam tim memiliki salinan dari projek (atau bagian dari projek) pada repositori lokal di perangkat mereka masing-masing. Kegunaan lain dari 'Git' juga kita bisa memonitor perkembangan dari proyek yang sedang dikembangkan. Versi lama dari proyek tersebut juga akan disimpan oleh 'Git' dan bisa kita akses kapan saja, bahkan bisa melanjutkan proyek dari versi itu saja.

<h2>Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?</h2>
1. **Relatif Mudah Dipahami**: Django adalah sebuah framework yang berjalan dengan kode python. Python sekarang ini dikenal sebagai salah satu bahasa pemrograman yang paling mudah untuk dipelajari dan kerap menjadi bahasa pertama yang dipelajari oleh seseorang yang baru menyentuh dunia programming. Python pun menjadi salah satu bahasa yang paling mudah untuk dipahami karena syntax yang mudah untuk dicerna menggunakan logika awam manusia. Oleh karena itu, framework django akan menjadi lebih familier untuk dipelajari apabila seseorang ingin memulai pembelajaran pengembangan perangkat lunak, atau pengembangan aplikasi web secara spesifik, yang hanya membutuhkan pengetahuan yang cukup pada bahasa python.
1. **Community Support yang besar**: Django telah digunakan oleh banyak orang selama lebih dari 10 tahun. Dengan keberadaan yang sudah cukup lama tentunya akan membawa besarnya angka pengguna pula. Dari banyaknya pengguna inilah lahir Communiy Support yang besar bagi Django. Apabila seseorang mengalami kesulitan dalam mempelajari Django, dengan mencari informasi di Google saja sudah bisa menemukan banyak sekali referensi yang bisa menjadi solusi bagi kesulitan mereka

<h2>Mengapa model pada Django disebut sebagai ORM?</h2>
Model di Django disebut sebagai ORM (Object-Relational Mapping) karena Django menyediakan cara untuk menghubungkan database relasional dengan kode Python menggunakan objek. Setiap tabel di database direpresentasikan sebagai kelas Python, dan setiap kolom dalam tabel adalah atribut dari kelas tersebut. ORM ini memungkinkan pengembang untuk berinteraksi dengan database menggunakan kode Python, tanpa perlu menulis query SQL secara langsung. ORM membantu mengelola data dengan lebih efisien dan mempermudah integrasi antara aplikasi dan database.