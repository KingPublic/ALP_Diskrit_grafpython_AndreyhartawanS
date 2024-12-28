# Implementasi Teori Graf Menggunakan Python

Proyek ini bertujuan untuk mengimplementasikan teori graf menggunakan Python dan library NetworkX. Program ini menyediakan berbagai metode untuk mempelajari graf, seperti menambah simpul (node), menambah sisi (edge), menghitung jalur terpendek, dan memvisualisasikan graf. Selain itu, program ini mencakup metode tambahan untuk analisis lebih lanjut terhadap graf.

## Kebutuhan Sistem
- Python 3.x
- Library Python:
  - `networkx`
  - `matplotlib`

Pastikan library yang diperlukan sudah terinstal. Gunakan perintah berikut untuk menginstal:
```bash
pip install networkx matplotlib
```

## Struktur Kode
Kode diimplementasikan dalam kelas `Graf` yang memiliki berbagai metode untuk memanipulasi dan menganalisis graf.

## Panduan Penggunaan

### 1. Membuat Objek Graf
Untuk memulai, buat objek graf dengan:
```python
graph = Graf()
```

### 2. Menambah Simpul (Node)
Tambahkan simpul ke dalam graf menggunakan metode `add_node`:
```python
graph.add_node(1)
graph.add_node(2)
```

### 3. Menambah Sisi (Edge)
Tambahkan sisi dengan bobot menggunakan metode `add_edge`:
```python
graph.add_edge(1, 2, weight=4.5)
```

### 4. Visualisasi Graf
Gunakan metode `visualize_graph` untuk melihat graf secara visual:
```python
graph.visualize_graph()
```

### 5. Menghitung Jalur Terpendek
Hitung jalur terpendek antara dua simpul menggunakan metode `shortest_path`:
```python
print(graph.shortest_path(1, 5))
```

### 6. Visualisasi Jalur Terpendek
Tampilkan jalur terpendek secara visual dengan metode `visual_shortest_path`:
```python
graph.visual_shortest_path(1, 5)
```

### 7. Metode Tambahan
Program ini juga menyediakan metode tambahan untuk analisis graf:

#### a. `is_connected()`
Memeriksa apakah graf terhubung.
```python
print(graph.is_connected())
```

#### b. `node_degrees()`
Mengembalikan derajat dari setiap simpul.
```python
print(graph.node_degrees())
```

#### c. `connected_components()`
Mengembalikan daftar komponen terhubung dalam graf.
```python
print(graph.connected_components())
```

#### d. `graph_diameter()`
Mengembalikan diameter graf (panjang jalur terpanjang di graf yang terhubung).
```python
print(graph.graph_diameter())
```

#### e. `has_cycle()`
Memeriksa apakah graf memiliki siklus.
```python
print(graph.has_cycle())
```

#### f. `find_sirkuit()`
Menemukan semua sirkuit (lintasan tertutup) dalam graf.
```python
print(graph.find_sirkuit())
```

#### g. `panjang_sirkuit()`
Mengembalikan panjang setiap sirkuit dalam graf.
```python
print(graph.panjang_sirkuit())
```

## Contoh Implementasi
Berikut adalah contoh penggunaan program:
```python
# Membuat graf
graph = Graf()

# Menambah node
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)

# Menambah edge
graph.add_edge(1, 2, weight=4.5)
graph.add_edge(2, 3, weight=3.2)
graph.add_edge(3, 1, weight=2.7)

# Visualisasi graf
graph.visualize_graph()

# Jalur terpendek
print("Jalur terpendek dari 1 ke 3:", graph.shortest_path(1, 3))

# Visualisasi jalur terpendek
graph.visual_shortest_path(1, 3)

# Analisis tambahan
print("Apakah graf terhubung?:", graph.is_connected())
print("Derajat simpul:", graph.node_degrees())
print("Komponen terhubung:", graph.connected_components())
print("Diameter graf:", graph.graph_diameter())
print("Apakah graf memiliki siklus?:", graph.has_cycle())
print("Sirkuit dalam graf:", graph.find_sirkuit())
print("Panjang setiap sirkuit:", graph.panjang_sirkuit())
```

## Hasil
- Visualisasi graf dan jalur terpendek.
- Informasi lengkap tentang struktur graf seperti komponen terhubung, derajat simpul, diameter, dan sirkuit.

## Download
Silahkan clone github ini dan test sendiri : https://github.com/ 

## Kesimpulan

Program ini merupakan implementasi praktis dari teori graf menggunakan Python. Dengan memanfaatkan library NetworkX, program ini memungkinkan pengguna untuk memanipulasi dan menganalisis graf secara efisien. Fitur seperti visualisasi, perhitungan jalur terpendek, deteksi sirkuit, dan analisis struktur graf memberikan alat yang berguna untuk mempelajari teori graf secara mendalam. Dengan panduan langkah demi langkah dan fungsi yang terstruktur, program ini cocok untuk digunakan baik untuk pembelajaran maupun analisis graf secara umum.

