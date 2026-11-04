# Kesimpulan dan Cara Menggunakan Anti-AI Slop Design Intelligence

**Versi paket:** 3.0.0  
**Bahasa:** Indonesia  
**Tujuan:** Menjadi panduan instruksi desain dan tipografi yang konsisten saat menggunakan berbagai AI, agent, dan workflow kreatif.

## 1. Kesimpulan

`desain-font-terhadap-buatan-Intelijen` adalah paket instruksi lintas-platform. Paket ini membantu AI atau agent menerapkan aturan desain yang lebih konsisten, terutama dalam pemilihan font, dukungan aksara Non-Latin, dan pencegahan elemen visual yang tidak diminta.

Aturan utamanya:

1. Gunakan maksimal **dua keluarga font utama** dalam satu desain: satu untuk **Heading/Display** dan satu untuk **Body**. Gunakan satu keluarga saja bila sudah memadai.
2. Sediakan fallback aksara seperti Hanzi/CJK, Kana, Hangul, atau aksara lain **ketika aksara tersebut memang muncul atau dibutuhkan**.
3. Gunakan nama font dan bobot yang nyata. Jangan mengarang ketersediaan font, lisensi, dukungan glyph, hasil render, atau preview.
4. Jangan menambahkan teks, logo, watermark, ikon, ornamen, objek, atau efek yang tidak diminta.
5. Jangan menyatakan aturan telah tersimpan permanen atau plugin telah terpasang tanpa bukti keberhasilan.

Paket ini menyediakan tiga mode pemakaian, rantai trigger, indeks font, panduan integrasi untuk **60 layanan/platform AI yang tercantum**, dan installer adapter instruksi untuk beberapa jenis proyek coding.

> **Batas penting:** Paket ini bukan plugin universal yang otomatis mengubah semua akun AI, model, atau memorinya. File JSON adalah spesifikasi urutan instruksi, bukan pemicu yang berjalan sendiri. Penyimpanan bergantung pada fitur resmi masing-masing platform atau file instruksi lokal yang benar-benar dibaca oleh agent.

## 2. Pilih mode yang sesuai

| Mode | Isi | Cocok untuk | Cara pakai |
|---|---|---|---|
| **Mode 1 — Instant** | `mode-1-file-instant/BUNDLE_1FILE_TRIGGER_SKILL.md` | AI yang hanya menerima satu file atau satu prompt | Unggah file tersebut sebagai instruksi/knowledge, atau salin seluruh isinya ke prompt/instruksi proyek. |
| **Mode 2 — Lite** | `mode-2-file-lite/1_TRIGGERS_AND_INDEX.json` dan `mode-2-file-lite/2_SKILL_AND_RULES.md` | AI dengan batas maksimal dua file | Berikan kedua file. Minta AI membaca JSON terlebih dahulu, lalu membaca dan menerapkan aturan Markdown. |
| **Mode 3 — Agentic / Full Code** | Folder `panduan-sampel-font/` | Agent yang dapat membaca file dan menjalankan Python di lingkungan lokal | Jalankan pemeriksaan paket, lalu pasang adapter ke folder proyek yang dituju bila diperlukan. |

**Rekomendasi:** Gunakan Mode 1 untuk pemakaian cepat, Mode 2 untuk platform dengan batas dua berkas, dan Mode 3 untuk proyek coding atau agent yang memiliki akses file lokal.

## 3. Cara kerja rantai trigger

Urutan logis paket adalah:

```text
trigger_root -> trigger_panduan -> trigger_package_save
```

- **`trigger_root`** membaca indeks font dan struktur paket, lalu menentukan alur yang sesuai.
- **`trigger_panduan`** menerapkan aturan tipografi, fallback aksara, dan pemeriksaan anti-visual-hallucination.
- **`trigger_package_save`** menyiapkan instruksi untuk mekanisme penyimpanan yang tersedia dan melaporkan status berdasarkan bukti.

Jika platform tidak bisa menjalankan JSON atau skrip, minta AI membaca file sebagai teks dan mengikuti urutan tersebut secara manual. JSON tidak mengeksekusi dirinya sendiri.

## 4. Cara menggunakan Mode 1

1. Buka `mode-1-file-instant/BUNDLE_1FILE_TRIGGER_SKILL.md`.
2. Unggah file ke bagian Instructions, Project Knowledge, Gem/Skill, Agent, atau tempat instruksi yang disediakan platform.
3. Jika platform tidak menyediakan tempat penyimpanan instruksi, tempelkan isi file sebagai prompt pada awal tugas.
4. Minta AI menerapkan aturan tersebut pada pekerjaan desain yang sedang dilakukan.

Contoh instruksi setelah file diberikan:

```text
Baca seluruh BUNDLE_1FILE_TRIGGER_SKILL.md dan terapkan aturan di dalamnya.
Ikuti urutan trigger_root -> trigger_panduan -> trigger_package_save.
Untuk tugas desain ini, batasi font utama maksimal satu Heading dan satu Body,
sediakan fallback aksara bila diperlukan, dan jangan menambahkan elemen visual
atau menyatakan validasi yang belum benar-benar dilakukan.
Laporkan batasan platform dan status penyimpanan secara jujur.
```

## 5. Cara menggunakan Mode 2

1. Unggah kedua file dari `mode-2-file-lite/` dalam satu percakapan atau ruang proyek.
2. Minta AI membaca `1_TRIGGERS_AND_INDEX.json` terlebih dahulu.
3. Setelah itu minta AI membaca `2_SKILL_AND_RULES.md` secara lengkap.
4. Minta AI menerapkan aturan pada pekerjaan yang relevan.

Prompt contoh:

```text
Baca kedua file yang saya lampirkan.
Urutannya: 1_TRIGGERS_AND_INDEX.json, kemudian 2_SKILL_AND_RULES.md.
Jalankan urutan instruksi trigger_root -> trigger_panduan -> trigger_package_save
secara konseptual. Terapkan seluruh aturan desain yang relevan dan laporkan
status penyimpanan hanya jika ada bukti.
```

## 6. Cara menggunakan Mode 3

### A. Validasi paket

Ekstrak repositori atau ZIP terlebih dahulu. Buka terminal pada folder `panduan-sampel-font`, lalu jalankan:

```powershell
python auto_installer.py --check
```

Pemeriksaan ini memvalidasi keberadaan file wajib, format JSON, urutan trigger, dan beberapa aturan inti. Pemeriksaan tersebut **hanya memvalidasi paket lokal**; bukan tes koneksi ke layanan AI.

### B. Pasang adapter instruksi ke proyek lokal

Jalankan perintah berikut dengan lokasi proyek Anda sendiri:

```powershell
python auto_installer.py --install-local "C:\PATH\KE\PROYEK"
```

Contoh:

```powershell
python auto_installer.py --install-local "D:\Project\website-portfolio"
```

Installer dapat menyalin adapter berikut ke proyek:

| File tujuan | Penggunaan |
|---|---|
| `AGENTS.md` | Instruksi umum untuk agent coding yang membaca file ini |
| `GEMINI.md` | Adapter instruksi untuk workflow Gemini/agent yang dikonfigurasi membacanya |
| `CLAUDE.md` | Adapter instruksi untuk workflow Claude/agent yang dikonfigurasi membacanya |
| `.github/copilot-instructions.md` | Instruksi repositori untuk fitur GitHub Copilot yang mendukungnya |
| `.cursor/rules/anti-ai-slop.mdc` | Project rule untuk Cursor |

Secara default, file yang sudah ada **tidak ditimpa**; installer akan melewatinya. Jika memang ingin mengganti file adapter yang sudah ada, gunakan:

```powershell
python auto_installer.py --install-local "C:\PATH\KE\PROYEK" --force
```

Dengan `--force`, file lama dicadangkan menggunakan akhiran `.bak` sebelum diganti. Periksa hasilnya setelah instalasi. Tidak semua aplikasi otomatis membaca setiap nama file; pastikan format tersebut didukung atau daftarkan file sebagai instruksi proyek secara manual.

### C. Periksa file yang dibuat

Masuk ke folder proyek tujuan, kemudian jalankan:

```powershell
git status
git diff --stat
```

Buka file adapter untuk memastikan instruksinya sesuai. Jangan commit file yang tidak Anda inginkan.

## 7. Aturan desain yang harus diterapkan

### Tipografi

- Maksimal dua keluarga font utama: Heading/Display dan Body.
- Bold, italic, dan ukuran berbeda dari keluarga font yang sama tidak dihitung sebagai keluarga font baru.
- Font fallback adalah jalur kompatibilitas glyph, bukan font dekoratif tambahan.
- Jangan menggunakan bobot font yang belum terbukti tersedia.

### Aksara Non-Latin

- Identifikasi aksara yang benar-benar ada pada konten.
- Untuk Hanzi/CJK, pilih fallback sesuai OS dan kebutuhan aksara. Contoh referensi: Microsoft YaHei atau SimSun pada Windows; PingFang SC pada Apple; Noto Sans CJK/Noto Serif CJK pada Linux jika terpasang.
- Jangan menganggap dukungan Hanzi Simplified otomatis berarti dukungan Traditional Chinese, Kanji Jepang, Hangul Korea, atau semua simbol.
- Jika font atau glyph belum diuji pada perangkat target, tandai **belum diverifikasi**.

### Anti-visual-hallucination

- Jangan mengarang nama font, lisensi, foundry, versi, bobot, dukungan bahasa, atau glyph.
- Jangan mengklaim screenshot, preview, atau hasil render telah diuji bila belum diperiksa.
- Jangan menambahkan tulisan acak, pseudo-huruf, logo, watermark, objek, atau efek yang tidak diminta.
- Untuk teks penting di gambar generatif, buat visual tanpa teks bila perlu, lalu tata teks secara terpisah dan periksa ejaan serta glyph-nya.

## 8. Cara menyimpan aturan pada berbagai platform

Gunakan `panduan-sampel-font/PLATFORM_SETUP.md` untuk melihat peta integrasi 60 layanan/platform yang diminta. Pilih jalur yang benar-benar tersedia pada akun dan versi aplikasi Anda, misalnya:

- **Instruksi akun:** preferensi atau custom instructions.
- **Instruksi proyek:** Project Instructions, workspace, atau project knowledge.
- **Skill/Gem/Agent:** simpan skill atau instruksi pada agent khusus jika tersedia.
- **Brand Kit/preset/template:** gunakan hanya untuk aturan yang memang didukung oleh fitur tersebut.
- **Prompt per tugas:** jika tidak ada fitur penyimpanan, sertakan bundle atau aturan ringkas pada setiap tugas.
- **File proyek/repo:** gunakan adapter lokal untuk agent coding yang mendukungnya.

Lingkup penyimpanan tidak selalu sama. Instruksi yang disimpan di satu proyek belum tentu berlaku untuk percakapan umum, akun lain, atau aplikasi AI yang berbeda. Fitur dan nama menu dapat berubah; verifikasi pada antarmuka layanan yang sedang digunakan.

## 9. Status penyimpanan yang boleh dilaporkan

Gunakan status berikut sesuai bukti:

| Status | Makna |
|---|---|
| `NOT_INSTALLED` | Belum ada tindakan penyimpanan yang berhasil dilakukan. |
| `INSTRUCTIONS_PREPARED` | Instruksi sudah disiapkan, tetapi belum disimpan pada platform. |
| `LOCAL_PROJECT_FILES_CREATED` | File adapter sudah berhasil dibuat pada path proyek lokal yang disebutkan. |
| `PLATFORM_SAVE_CONFIRMED` | Platform atau pengguna sudah mengonfirmasi penyimpanan berhasil. |

Jangan menyebut aturan telah tersimpan permanen di semua AI, plugin telah terpasang, atau memori model telah berubah tanpa bukti langsung.

## 10. Cara memperbarui repositori GitHub

Setelah menyalin file baru atau hasil pembaruan ke folder clone repositori:

```powershell
git status
git diff --stat
git add -A
git commit -m "Add Anti-AI Slop usage guide"
git push origin master
```

Gunakan nama branch yang benar bila repositori tidak memakai `master`. Jika push ditolak, jangan langsung memakai `--force`; periksa `git fetch`, status branch, dan perbedaan riwayat terlebih dahulu.

## 11. Checklist sebelum digunakan

- [ ] Mode sudah dipilih sesuai batas file dan kemampuan platform.
- [ ] AI membaca file instruksi yang benar.
- [ ] Font Heading dan Body tidak lebih dari dua keluarga utama.
- [ ] Fallback aksara disediakan jika diperlukan.
- [ ] Nama font, bobot, dan glyph tidak dikarang.
- [ ] Elemen visual tambahan tidak dibuat tanpa permintaan.
- [ ] Klaim preview/render hanya dibuat setelah pemeriksaan nyata.
- [ ] Status penyimpanan sesuai bukti.

## 12. Referensi file dalam paket

- `README.md` — ringkasan paket dan struktur.
- `mode-1-file-instant/BUNDLE_1FILE_TRIGGER_SKILL.md` — bundle satu file.
- `mode-2-file-lite/1_TRIGGERS_AND_INDEX.json` — pemicu dan indeks font Mode 2.
- `mode-2-file-lite/2_SKILL_AND_RULES.md` — aturan lengkap Mode 2.
- `panduan-sampel-font/trigger_root.json` — urutan orkestrasi.
- `panduan-sampel-font/trigger_panduan.json` — aturan dan pemeriksaan desain.
- `panduan-sampel-font/trigger_package_save.json` — kebijakan penyimpanan dan status.
- `panduan-sampel-font/1. SKILL.md` — skill utama.
- `panduan-sampel-font/daftar_font.txt` — indeks font.
- `panduan-sampel-font/PLATFORM_SETUP.md` — peta integrasi platform.
- `panduan-sampel-font/auto_installer.py` — pemeriksa paket dan installer adapter lokal.

---

**Kesimpulan akhir:** Paket ini menjadi standar instruksi yang dapat dibawa antar-platform. Pilih mode yang sesuai, berikan instruksi kepada AI/agent untuk membaca dan menerapkannya, lalu simpan pada fitur yang memang tersedia. Untuk proyek coding, gunakan installer lokal dan periksa file yang dihasilkan. Jangan menyamakan tersedianya file dengan pemasangan otomatis ke semua layanan AI.
