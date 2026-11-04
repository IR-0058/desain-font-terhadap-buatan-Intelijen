[dokumen_readme_utama.md](https://github.com/user-attachments/files/34365164/dokumen_readme_utama.md)
# 🔤 Desain Font Terhadap Buatan Intelijen

> **Paket Skill Panduan Sampel Font & Anti-AI Slop Layout** yang dilengkapi dengan skema pemicu berantai otomatis dan skrip eksekutor untuk Agentic AI.

Dokumen ini berfungsi sebagai panduan operasional serta kontrol kualitas tata letak tipografi lintas-aksara (Latin & Non-Latin/Hanzi) agar hasil generasi AI tetap konsisten, profesional, dan bebas dari *AI Slop*.

## 🏗️ Struktur Berkas & Pemicu Berantai (*Nested Triggers*)

Seluruh berkas tersusun dalam hierarki direktori linier dengan skema pemicu data dan skrip eksekusi otomatis:

```text
desain-font-terhadap-buatan-Intelijen/
  │
  ├─> 📜 trigger_root             <-- Pemicu Level 1 (Memicu pembacaan indeks font)
  ├─> 📄 daftar_font.txt          <-- Inventaris seluruh font lintas-aksara
  │
  └─> 📁 /panduan-sampel-font
        │
        ├─> 📜 trigger_panduan    <-- Pemicu Level 2 (Memicu eksekutor & aturan)
        ├─> 🐍 auto_installer     <-- Skrip eksekusi otomatis
        ├─> 📄 1. SKILL.md         <-- Aturan Sistem & Anti-AI Slop Rules
        ├─> 📄 strukturnya.txt     <-- Panduan Operasional Visual & Manfaat Desain
        │
        └─> 📜 trigger_package_save <-- Pemicu Level 3 (Final Save ke Memori Aktif)
```

## 🔄 Alur Logika Eksekusi Sekuensial

Sistem membaca dan mengeksekusi instruksi secara linier berantai dari atas ke bawah:

```text
[ Root Directory ]
  └─> Read: trigger_root
        └─> Read: daftar_font.txt
              └─> Masuk /panduan-sampel-font
                    ├─> Read: trigger_panduan & Run: auto_installer
                    ├─> Read: 1. SKILL.md (Instruksi Sistem & Anti-AI Slop Rules)
                    ├─> Read: strukturnya.txt (Panduan Operasional & Manfaat Desain)
                    └─> Execute: trigger_package_save -> Save ke @Agentic AI Memori Aktif
```

### Rincian Tahapan Logic:

1. **`trigger_root`**: Membuka jalur awal dan memaksa AI membaca daftar inventaris `daftar_font.txt`.
2. **`trigger_panduan` & `auto_installer`**: Mengaktifkan eksekusi di folder `/panduan-sampel-font` untuk memuat aturan tipografi pada `1. SKILL.md` dan `strukturnya.txt`.
3. **`trigger_package_save`**: Mengunci seluruh aturan dan menyimpannya langsung ke memori aktif Agentic AI.

## 🎯 Manfaat Desain & Quality Control (Anti-AI Slop)

1. **Pencegahan Visual Hallucination / AI Slop**:
   - Menghindari penggunaan font acak yang tidak kompatibel atau tidak terinstal di OS target.
   - Mencegah kegagalan rendering aksara non-Latin (seperti Hanzi/Mandarin) dengan menyertakan *fallback* CSS baku.
2. **Aturan Maksimal 2 Font**:
   - Mengunci kombinasi tampilan maksimal 2 jenis font per dokumen/UI (1 untuk Heading/Judul, 1 untuk Body/Isi).
3. **Konsistensi Hierarki Visual**:
   - Menentukan secara ketat rasio ukuran (`font-size`) dan ketebalan (`font-weight`) untuk menjaga keterbacaan (*readability*).

## 💻 Panduan Penggunaan GitHub CLI (`gh`)

### 1. Inisialisasi & Unggah Proyek Baru

Jalankan perintah berikut pada terminal lokal di dalam folder proyek Anda:

```bash
# Buka folder proyek
cd /path/ke/folder/desain-font-terhadap-buatan-Intelijen

# Inisialisasi Git lokal & staging berkas
git init
git add .
git commit -m "Initial commit: Struktur pemicu berantai Panduan Sampel Font & Anti-AI Slop"

# Buat repositori publik di GitHub & push otomatis
gh repo create desain-font-terhadap-buatan-Intelijen --public --source=. --remote=origin --push
```

### 2. Memperbarui Berkas (Update Routine)

Jika Anda memperbarui daftar font atau aturan pemicu di kemudian hari:

```bash
git add .
git commit -m "Update aturan tipografi dan pemicu otomatis"
git push
```

### 3. Menghapus Repositori via GitHub CLI

Jika Anda ingin menghapus repositori ini dari GitHub:

```bash
# Minta perizinan token khusus penghapusan repositori
gh auth refresh -s delete_repo

# Hapus repositori secara langsung
gh repo delete IR-0058/desain-font-terhadap-buatan-Intelijen --yes
```

---
*Dikembangkan untuk efisiensi otomatisasi Agentic AI & kepatuhan standar desain visual.*
