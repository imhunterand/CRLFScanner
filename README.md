# CRLFScanner

## Deskripsi Proyek

CRLFScanner adalah alat pemindai yang dikembangkan untuk mendeteksi kerentanan CRLF Injection pada aplikasi web. Injeksi CRLF adalah kerentanan keamanan web yang memungkinkan penyerang menyuntikkan karakter carriage return (CR) dan linefeed (LF) ke dalam input aplikasi web, yang dapat menyebabkan berbagai jenis serangan seperti HTTP Response Splitting, Header Injection, dan manipulasi konten. Alat ini dirancang untuk membantu pengembang dan profesional keamanan web dalam mengidentifikasi dan mengatasi kerentanan ini.

## Fitur
- **Pemindaian CRLF Injection**: Mendeteksi injeksi CRLF dengan berbagai payload.
- **Multi-threading**: Meningkatkan kecepatan pemindaian menggunakan beberapa thread.
- **Pemindaian berbasis daftar URL**: Mendukung pemindaian banyak URL sekaligus.
- **Pencatatan hasil**: Menyimpan hasil pemindaian dalam format CSV.
- **Analisis respons**: Menganalisis respons untuk deteksi yang lebih akurat.

## Struktur Proyek
```js
CRLFScanner/
├── payloads/
│ ├── payloads.txt
├── results/
│ ├── results.csv
├── src/
│ ├── init.py
│ ├── crlf_scanner.py
│ ├── multi_threading.py
│ ├── url_loader.py
│ ├── logger.py
│ └── response_analyzer.py
├── README.md
├── requirements.txt
└── run_scanner.py
```
## Instalasi

1. **Clone repositori ini**:
   ```sh
   git clone https://github.com/imhunterand/CRLFScanner.git
   cd CRLFScanner
```
2. Instalasi Dependensi:
```
pip install -r requirements.txt
pip3 install -r requirements.txt
```
## Cara Penggunaan
**Menyiapkan Daftar URL dan Payload**
 * Daftar URL: Simpan URL target dalam file teks, satu URL per baris. Contoh:

```
http://example.com/vulnerable_endpoint1
http://example.com/vulnerable_endpoint2
```
 * Daftar Payload: Simpan payload CRLF dalam file `payloads/payloads.txt`, satu payload per baris. Contoh:

```
%0d%0aInjected-Header: CRLF
%0d%0aTest-Header: Test
%0d%0aX-Injected-Header: X-Test
```
## Menjalankan Automatic Tool
Jalankan alat scanner dengan perintah berikut:
```
python run_scanner.py -u urls.txt -o results/results.csv
```
**Parameter:**
 * `-u, --urls`: File path dari daftar URL.
 * `-o, --output`: File path untuk hasil pemindaian dalam format CSV.
 * `-p, --payloads`: File path dari daftar payload (opsional, default: payloads/payloads.txt).
 * `-t, --threads`: Jumlah thread untuk pemindaian (opsional, default: 10).

Contoh Penggunaan Python2
```
python run_scanner.py -u urls.txt -o results/results.csv -p payloads/payloads.txt -t 5
```
Contoh Penggunaan Python3
```
python3 run_scanner.py -u urls.txt -o results/results.csv -p payloads/payloads.txt -t 5
```
## Hasil Pemindaian
Hasil pemindaian akan disimpan dalam file CSV di direktori `results/`. Setiap baris dalam file CSV berisi informasi berikut:
 * **URL:** URL yang dipindai.
 * **Payload:** Payload yang digunakan.
 * **Result:** Hasil pemindaian (Vulnerable/Not Vulnerable/Error).

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan fork repositori ini dan ajukan pull request dengan perubahan yang Anda buat. Pastikan untuk menambahkan deskripsi yang jelas tentang perubahan Anda.

Kontak
Untuk pertanyaan atau dukungan, silakan hubungi imhunterand@cyberservices.com.

