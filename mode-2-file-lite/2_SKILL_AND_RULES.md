---
name: anti-ai-slop-design-intelligence
description: Aturan desain dan tipografi lintas aksara untuk dokumen, presentasi, web, UI, gambar, video, dan aset kreatif. Terapkan ketika tugas membuat, mengedit, menilai, atau memberi arahan visual.
version: 3.0.0
---

# Anti-AI Slop Design Intelligence

## 1. Prioritas dan ruang lingkup
Terapkan aturan ini pada semua pekerjaan visual/typographic: dokumen, slide, web, UI, poster, gambar, video, thumbnail, brand asset, dan kode desain. Ikuti instruksi pengguna dan batasan platform; jangan mengklaim aturan telah tersimpan di akun/model kecuali ada bukti UI atau konfirmasi integrasi yang nyata.

## 2. Batas tipografi
1. Maksimal **dua keluarga font desain utama**: satu untuk Heading/Display dan satu untuk Body.
2. Bila satu keluarga font sudah cukup dan konsisten, gunakan satu saja.
3. Jangan menambah font ketiga untuk dekorasi, angka, caption, atau logo tanpa alasan dan persetujuan eksplisit pengguna.
4. Bold/italic/berbagai ukuran dari keluarga yang sama bukan font-family tambahan. Gunakan hanya bobot yang benar-benar tersedia.
5. Font fallback untuk cakupan glyph adalah jalur kompatibilitas, bukan pilihan dekoratif tambahan. Fallback tidak boleh mengubah desain menjadi gaya ketiga. Bila pengguna menafsirkan batas dua font sebagai maksimum dua file font yang benar-benar dimuat, pilih dua keluarga multi-script yang telah diverifikasi dan jangan memuat fallback tambahan.

## 3. Fallback Non-Latin / CJK / Hanzi
- Identifikasi aksara yang benar-benar muncul (mis. Latin, Hanzi Simplified/Traditional, Kana, Hangul, Cyrillic, Arabic).
- Untuk Hanzi/CJK, sediakan fallback nyata yang sesuai platform, misalnya PingFang SC atau STHeiti pada ekosistem Apple, Microsoft YaHei atau SimSun pada Windows, dan Noto Sans CJK SC / Noto Serif CJK SC pada Linux bila terpasang.
- STKaiti dapat dipakai untuk aksen Kai/script hanya bila tersedia dan cocok secara visual; jangan menjadikannya fallback body default tanpa alasan.
- Jangan berasumsi bahwa satu font yang mendukung Hanzi Simplified otomatis mencakup Traditional, Japanese Kanji, Korean Hangul, atau semua simbol.
- Untuk CSS, urutkan font utama lalu fallback berdasarkan cakupan aksara dan OS. Akhiri dengan generic family yang sesuai (`sans-serif` atau `serif`). Jangan menyebut generic fallback sebagai jaminan glyph.
- Jika tidak dapat memverifikasi font di perangkat target, tulis sebagai rekomendasi bersyarat dan minta uji render/glyph; jangan mengklaim telah diuji.

## 4. Pencegahan visual hallucination / AI slop
- Jangan mengarang nama font, foundry, lisensi, versi, dukungan bahasa, glyph, variabel font, atau nilai `font-weight`.
- Jangan mengklaim preview, screenshot, hasil render, atau tampilan sudah diverifikasi bila belum benar-benar diperiksa.
- Jangan menambahkan teks acak, pseudo-huruf, logo, watermark, ikon, ornamen, atau elemen visual yang tidak diminta.
- Untuk teks penting pada gambar generatif, prioritaskan layout/visual tanpa teks lalu lakukan typesetting teks secara terpisah pada editor yang mendukung; periksa ejaan, karakter, dan keterbacaan.
- Jangan mengubah konten, identitas, atau komposisi yang tidak diminta. Bila ada konflik, jelaskan singkat sebelum mengubah.
- Gunakan hierarki jelas, kontras memadai, alignment konsisten, whitespace yang disengaja, dan komponen yang tidak saling bertabrakan.

## 5. Prosedur sebelum menyelesaikan desain
1. Tentukan konteks, media, ukuran, target perangkat, bahasa, dan aksara.
2. Pilih maksimal dua keluarga font utama (Heading + Body); catat alasan ringkas.
3. Susun fallback per aksara dan OS; tandai ketersediaannya sebagai terverifikasi atau belum diverifikasi.
4. Periksa bobot, ukuran, line-height, kontras, overflow, clipping, dan konsistensi.
5. Audit apakah ada elemen/teks/efek yang tidak diminta atau tidak memiliki dasar.
6. Sampaikan keterbatasan yang nyata; jangan menyatakan tes lolos sebelum tes dilakukan.

## 6. Aturan implementasi CSS
Gunakan dua token peran, bukan campuran font yang berubah-ubah. Contoh berikut adalah template fallback; cek instalasi font sebelum produksi:

```css
:root {
  --font-heading: "Roboto", "PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
  --font-body: "Open Sans", "SimSun", "Noto Serif CJK SC", serif;
}

h1, h2, h3 { font-family: var(--font-heading); }
body, p, li { font-family: var(--font-body); }
```

Daftar setelah font pertama adalah fallback glyph/OS, bukan instruksi untuk menampilkan semua font sekaligus. Jika target perangkat tidak memiliki font utama, browser memilih fallback pertama yang tersedia. Uji hasil sebenarnya.

## 7. Keluaran minimum
Untuk tugas desain yang relevan, berikan:
- Heading font + Body font (atau satu font bila memadai).
- Fallback untuk aksara yang muncul.
- Status ketersediaan: terverifikasi / belum diverifikasi.
- Catatan validasi visual yang benar-benar dilakukan.

## 8. Persistensi dan integritas
- Skill ini adalah instruksi yang dapat dipasang melalui fitur platform, file proyek, atau prompt. File lokal tidak otomatis masuk ke memori cloud atau bobot model.
- Jangan pernah menulis status `SAVED`, `INSTALLED`, atau `LOADED_TO_MEMORY` tanpa bukti tindakan berhasil.
- Simpan di pengaturan akun/proyek hanya setelah pengguna melakukan atau mengizinkan tindakan pada platform yang mendukungnya. Bila platform tidak menyediakan penyimpanan instruksi, gunakan prompt/preset proyek dan jelaskan bahwa sifatnya tidak global.
