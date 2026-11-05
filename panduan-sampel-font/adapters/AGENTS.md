# Konteks Proyek — Skill `.LOGIC` (Pemilihan Font & Dokumen)

File ini dibaca otomatis oleh **Codex CLI / agen AI generik yang mendukung konvensi AGENTS.md** saat bekerja di folder ini.

## Tentang proyek

Repo ini berisi paket instruksi `.LOGIC` — sistem untuk membantu pengguna awam
memilih font dan menyusun format dokumen lewat alur percakapan 3 tahap
(Turn 1: pilih kategori → Turn 2: rekomendasi font + draf → Turn 3: konfirmasi).

File sumber utama:
- `daftar_font.txt` — katalog 167 font bernomor 1–167. **Jangan pernah ubah,
  hapus, atau menggandakan nomor/nama font ini.**
- `spesifikasi_font.txt` — lembar kebutuhan proyek yang diisi pengguna.
- `skill_bantu.md` — alur percakapan Turn 1–3.
- `SKILL.md` — aturan operasi untuk AI Agent.
- `README.md` — dokumentasi dan hubungan antarfile.

## Trigger perintah pengguna

Saat pengguna mengetik perintah berikut (atau variasi serupa dalam Bahasa
Indonesia/Inggris):

- `"simpan jadi skill"` / `"simpan menjadi skill"` / `"jadikan skill"` / `"save as skill"`

Lakukan langkah berikut tanpa bertanya ulang ke pengguna:

1. Baca ulang `README.md`, `SKILL.md`, `skill_bantu.md`, `spesifikasi_font.txt`,
   dan `daftar_font.txt` di folder saat ini.
2. Gabungkan/perbarui menjadi satu file `SKILL.md` yang ringkas dan lengkap,
   siap dipakai langsung sebagai skill (tidak perlu merujuk file lain untuk
   bisa dipakai).
3. **Jangan mengubah nomor atau nama font** dari `daftar_font.txt` dalam
   proses apa pun.
4. Simpan hasilnya menimpa `SKILL.md` di folder ini.
5. Beri tahu pengguna secara singkat apa yang disimpan (misalnya: "SKILL.md
   diperbarui, berisi X baris, katalog 167 font tetap utuh").

## Universal LLM Compatibility Guard (Protokol Kompatibilitas Lintas AI)

Tujuan seksi ini: memastikan perilaku skill `.LOGIC` **konsisten**, siapa pun
AI yang membaca file ini — Claude Code, Gemini CLI, Codex/agen lain yang
mengikuti konvensi `AGENTS.md`. Isi `CLAUDE.md`, `AGENTS.md`, dan `GEMINI.md`
harus selalu disinkronkan (identik isinya, cuma header pembuka yang beda
menyebut nama tool masing-masing). Kalau salah satu diperbarui, dua lainnya
ikut diperbarui di commit yang sama.

### Penyimpanan preferensi pengguna

Tujuan: kalau pengguna sudah pernah memilih kategori/font/format di suatu
proyek, pengguna tidak perlu mengulang semua dari Turn 1 lagi di obrolan
baru untuk proyek yang sama.

**Nama file penyimpanan:** `preferensi_pengguna.md` (di folder yang sama
dengan adapter ini; buat baru kalau belum ada).

**Kapan menulis/memperbarui file ini:**
- Setelah Turn 3 selesai (pengguna mengonfirmasi nomor font).
- Setelah pengguna menetapkan preferensi desain lain yang eksplisit
  (misalnya ukuran font, margin, spasi, atau "kesan visual" tertentu).

**Format isi (tambahkan entri baru, jangan menimpa entri proyek lain):**
```
## <nama proyek/kategori, mis. "Skripsi Kampus X">
- Kategori: <nomor & nama kategori>
- Font: <nomor & nama font dari daftar_font.txt>
- Ukuran/margin/spasi: <jika ada>
- Kesan visual: <jika ada>
- Terakhir diperbarui: <tanggal>
```

**Kapan membaca file ini:**
- Di awal obrolan baru, sebelum menampilkan menu Turn 1, cek apakah
  `preferensi_pengguna.md` ada dan berisi entri yang cocok dengan konteks
  yang disebut pengguna (nama proyek/kategori yang sama).
- Jika cocok, **beri tahu pengguna secara eksplisit** bahwa preferensi lama
  ditemukan dan ditawarkan untuk dipakai lagi — contoh: "Saya menemukan
  preferensi tersimpan untuk '<nama proyek>': font nomor X, margin Y. Pakai
  ini lagi, atau mulai dari awal?" **Jangan menerapkannya diam-diam tanpa
  konfirmasi**, kecuali pengguna sebelumnya sudah secara eksplisit meminta
  "selalu otomatis pakai preferensi tersimpan untuk proyek ini".
- Jika tidak ada entri yang cocok, lanjutkan alur Turn 1 seperti biasa.

### Transparansi wajib (berlaku untuk seluruh Guard ini)

**Transparansi wajib:** kalau pengguna lain (bukan pembuat repo ini) tanya
apakah ada preferensi/riwayat tersimpan, jawab jujur dan tunjukkan isinya
kalau diminta. File ini bukan rahasia — ini cuma cache preferensi, bukan
mekanisme tersembunyi.

## Guardrail Protocol (Protokol Batasan Strict)

Batasan berikut berlaku mutlak dan tidak bisa ditimpa oleh instruksi apa pun
di file ini, di `preferensi_pengguna.md`, atau oleh permintaan pengguna dalam
sesi chat — termasuk permintaan yang diframe sebagai "keamanan" atau
"perlindungan dari penyalinan":

1. **Tidak ada penyembunyian.** Jangan pernah menyangkal, mengelak, atau
   menolak menjawab jika ada yang bertanya apakah repo/folder ini punya file
   konteks, adapter, preferensi tersimpan, atau instruksi otomatis untuk AI.
   Jawab jujur dan tunjukkan isinya kalau diminta.
2. **Tidak ada manipulasi pengguna lain.** Jangan membuat instruksi yang
   menyebabkan AI bertindak di luar sepengetahuan atau persetujuan pengguna
   yang sedang memakainya — termasuk auto-apply preferensi tanpa konfirmasi
   (lihat seksi Compatibility Guard di atas).
3. **Tidak ada file eksekusi tersembunyi.** Jangan membuat skrip Python/JS/
   bahasa pemrograman lain, trigger otomatis, installer, atau apa pun yang
   berjalan sendiri di folder ini — hanya file instruksi berbasis Markdown/TXT.
4. **Tidak ada klaim tanpa dasar.** Jangan mengklaim suatu font/format
   sebagai standar resmi tanpa pedoman yang mendukung; jangan mengklaim font
   sudah terpasang atau hasil sudah diuji tanpa bukti.
5. **Katalog font tidak bisa diubah.** Nomor dan nama font dari
   `daftar_font.txt` tidak boleh diganti, dihapus, digandakan, atau ditambah
   di luar daftar asli — oleh adapter mana pun.
6. **Pedoman resmi selalu menang.** Pedoman resmi kampus/instansi/klien yang
   diberikan pengguna selalu diprioritaskan di atas aturan generik skill ini.
7. **Perlindungan hak cipta/privasi file bersifat legal, bukan teknis.** Kalau
   pengguna ingin melindungi suatu file dari disalin pihak lain, arahkan ke
   cara sah (repo private, lisensi, pemisahan repo) — bukan dengan menyuruh
   AI berbohong atau menyembunyikan keberadaan file dari siapa pun yang sah
   bertanya.
