# Welcome to Toko Sinar Abadi
#### Website URL: http://ida-made-tokosinarabadi.pbp.cs.ui.ac.id/

---

## Checklist Implementation Process
>Tugas 2
1. Membuat repositori di GitHub dengan nama **`sinar-abadi-web`**.
2. Membuat repositori lokal di laptop saya dengan nama **`Tugas 2`**.
3. Menghubungkan repositori lokal dengan repositori online di GitHub.
4. Meng-install dependencies melalui `requirements.txt`:
    ```bash
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
5. Memulai project menggunakan perintah:
    ```bash
    django-admin startproject mental_health_tracker
    ```
6. Memulai project baru di PWS dan melakukan deploy project di [website](http://ida-made-tokosinarabadi.pbp.cs.ui.ac.id/).
7. Mengubah bagian `ALLOWED_HOSTS` pada `settings.py` menjadi:
    ```python
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "http://ida-made-tokosinarabadi.pbp.cs.ui.ac.id/"]
    ```
8. Membuat aplikasi baru dengan nama **`main`**.
9. Membuat template dasar di file `main.html`.
10. Membuat model **`Product`** dengan atribut `name`, `price`, `description`, dan `color`.
11. Mengintegrasikan View dan Template dalam komponen Model-View-Template (MVT).
12. Mengonfigurasi URL di aplikasi **`main`** dan proyek secara keseluruhan.

## Visualisasi alur request/response
![Visualisasi alur web request/response](img/flow-bagan.png)

## Fungsi git dalam pengembangan perangkat lunak
'Git' merupakan sebuah Version Control System. 'Git' bukanlah satu-satunya Version Control System yang ada. Contoh lainnya adalah 'Helix Core'. Yang penting dalam pengembangan perangkat lunak ini adalah Version Control System ini. Version Control System sangat essential dalam workflow pengembangan perangkat lunak. Version Control System mendukung proses kerja sama dalam pengembangan perangkat lunak dengan memastikan setiap anggota tim dapat mengakses versi terbaru dari file yang telah dikerjakan juga oleh anggota lain dalam tim. Seluruh file ini akan dikumpulkan menjadi satu para repositori utama yang bertindak sebagai server.
Apabila kita ambil 'Git' sebagai contoh, 'Git' adalah sebuah Distributed Version Control System yang membuat setiap anggota dalam tim memiliki salinan dari projek (atau bagian dari projek) pada repositori lokal di perangkat mereka masing-masing. Kegunaan lain dari 'Git' juga kita bisa memonitor perkembangan dari proyek yang sedang dikembangkan. Versi lama dari proyek tersebut juga akan disimpan oleh 'Git' dan bisa kita akses kapan saja, bahkan bisa melanjutkan proyek dari versi itu saja.

## Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
1. **Relatif Mudah Dipahami**: Django adalah sebuah framework yang berjalan dengan kode python. Python sekarang ini dikenal sebagai salah satu bahasa pemrograman yang paling mudah untuk dipelajari dan kerap menjadi bahasa pertama yang dipelajari oleh seseorang yang baru menyentuh dunia programming. Python pun menjadi salah satu bahasa yang paling mudah untuk dipahami karena syntax yang mudah untuk dicerna menggunakan logika awam manusia. Oleh karena itu, framework django akan menjadi lebih familier untuk dipelajari apabila seseorang ingin memulai pembelajaran pengembangan perangkat lunak, atau pengembangan aplikasi web secara spesifik, yang hanya membutuhkan pengetahuan yang cukup pada bahasa python.
1. **Community Support yang besar**: Django telah digunakan oleh banyak orang selama lebih dari 10 tahun. Dengan keberadaan yang sudah cukup lama tentunya akan membawa besarnya angka pengguna pula. Dari banyaknya pengguna inilah lahir Communiy Support yang besar bagi Django. Apabila seseorang mengalami kesulitan dalam mempelajari Django, dengan mencari informasi di Google saja sudah bisa menemukan banyak sekali referensi yang bisa menjadi solusi bagi kesulitan mereka

## Mengapa model pada Django disebut sebagai ORM?
Model di Django disebut sebagai ORM (Object-Relational Mapping) karena Django menyediakan cara untuk menghubungkan database relasional dengan kode Python menggunakan objek. Setiap tabel di database direpresentasikan sebagai kelas Python, dan setiap kolom dalam tabel adalah atribut dari kelas tersebut. ORM ini memungkinkan pengembang untuk berinteraksi dengan database menggunakan kode Python, tanpa perlu menulis query SQL secara langsung. ORM membantu mengelola data dengan lebih efisien dan mempermudah integrasi antara aplikasi dan database.

---
## Checklist Implementation Process
>Tugas 3
1. Saya memulai dengan men-deploy ulang projek django saya ke PWS dengan URL http://ida-made-tokosinarabadi.pbp.cs.ui.ac.id/
2. Mengimplementasi Skeleton menjadi kerangka views projek. Membuat template dengan file `base.html`.
    ```
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            {% block meta %} {% endblock meta %}
        </head>

        <body>
            {% block content %} {% endblock content %}
        </body>
    </html>
    ```
3. Menerapkan UUID sebagai Primary Key dari Product
    ```python
    import uuid
    ...
    class Product(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ```
4. Membuat input form dan display-nya
    | `main.html`    | `create_product.html` |
    |----------------|-----------------------|
    | ![main.html](img/main.jpg) | ![create_product.html](img/create_product.jpg) |
5. Memanmbahkan fungsi untuk melihat objek dalam format XML, JSON, XML by ID, dan JSON by ID
    - Menambahkan 4 fungsi views untuk menghandle request dan respose
        ```python
        # Format XML
        def show_xml(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        # Format JSON
        def show_json(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

        # Format XML by ID
        def show_xml_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        # Format JSON by ID
        def show_json_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ```
    - Melakukan URL routing untuk keempat views
        ```python
        from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
        ...
        urlpatterns = [
            ...
            path('xml/', show_xml, name='show_xml'),
            path('json/', show_json, name='show_json'),
            path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
        ]
        ```

## URL view menggunakan `postman`
| Format | Screenshot |
| :----: | :----: |
| **XML** | ![XML view](img/xml_view.jpg) |
| **XML by ID** | ![XML by ID view](img/xml_by_id_view.jpg) |
| **JSON** | ![JSON view](img/json_view.jpg) |
| **JSON by ID** | ![JSON by ID view](img/json_by_id_view.jpg) |

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery menjadi elemen yang penting dalam pengimplementasian sebuah platform karena dengannya, aplikasi dapat menampilkan dan menyediakan informasi yang paling up-to-date. Data delivery juga dapat bermanfaat apabila platform tersebut dikembangkan dalam sebuah ekosistem. Data dapat dengan mudah diakses oleh berbagai layanan dalam ekosistem tersebut.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Terdapat beberapa hal yang menjadi kelebihan dari `JSON` jika dibandingkan dengan `xml':
- Tidak menggunakan *end tag* `</..>`
- Lebih ringan dan mudah dibaca oleh manusia
- Lebih efisien dalam hal ukuran data dan kecepatan parsing

Oleh karena itu, menurut saya `JSON` lebih baik daripada `XML`. Sebagai seorang manusia mencoba membaca keduanya sebenarnya juga sama-sama mudah, namun ketidakberadaan *end tag* pada `JSON` memberikan penulisan yang lebih rapi untuk dibaca.

Yang mungkin menjadi alasan akan popularitas `JSON` dibandingkan `XML` adalah efisiensinya secara *space* dan *runtime*. Dalam proses *parsing*, `XML` harus di-*parsing* menggunakan `XML Parser`.

## Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django digunakan untuk memeriksa apakah data yang dikirimkan melalui form memenuhi semua kriteria validasi yang telah ditentukan sebelumnya. Method ini mengembalikan nilai boolean `True` atau `False`. Method ini dibutuhkan untuk memastikan bahwa data yang diterima oleh aplikasi adalah data yang benar dan sesuai dengan kriteria yang telah ditetapkan, sehingga bisa mencegah kesalahan dan masalah keamanan.

## Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` digunakan untuk mencegah sebuah serangan bernama *Cross-Site Request Forgery* (CSRF). Serangan ini bekerja melalui `valid user` yang mendapatkan sesi yang valid pada sebuah halaman resmi. Penyerang akan membuat user tersebut mengakses sebuah situs yang ia buat untuk mendapatkan akses terhadap sesi dari user tersebut. Dalam sesi tersebut, peyerang dapat mengirimkan request tak diinginkan, melakukan transaksi yang tak diinginkan, hingga merubah data dalam situs web tersebut.

Dengan `csrf_token`, server akan memproses token ini terhadap user sebelum menjalankan seuatu transaksi yang menjamin keamanan dari user.