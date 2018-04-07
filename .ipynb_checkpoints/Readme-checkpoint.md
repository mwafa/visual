# Tugas Instrumentasi Visual

Project ini di dedikasikan untuk tugas matakuliah **Instrumentasi Sistem Visual**

## Instalasi visTF


Untuk instalasi dengan peritah **pip** pada terminal, yaitu:

```
python -m pip install http://bit.ly/visualDTNTF 
```

atau dengan:

```
python3 -m pip install http://bit.ly/visualDTNTF
```

## Memulai

### Membuat efek bulat-bulat

```python
from visTF import uts

image = uts.bulat('example/image/example.jpg')
image.make()
```

### [Contoh Hasil](example/ipynb)

Klik ling berikut untuk melihat [Contoh penggunaan](example/ipynb)

Berikut ini contoh hasilnya:

Sebelum:

![before](example/image/example.jpg)

Sesudah:

![before](example/result/example.jpg)

#### Setting Ukuran Lingkaran

```python
# image.setting(s,r)
image.setting(30,20)
```

```
.setting([s=20,[r=20]])

   s   = jarak antar titik arah horizontal
   r   = maksimum jari-jari lingkaran
```

#### Menyimpan hasil

```python
lokasi = r"folderke/file.jpg"
image.simpan(lokasi)
```



