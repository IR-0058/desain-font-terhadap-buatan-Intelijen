# 🔤 Desain Font Terhadap Buatan Intelijen

> **Panduan Operasional & Alur Eksekusi Agentic AI**: Berkas ini mengatur alur kerja sekuensial dan kontrol kualitas tipografi (*Anti-AI Slop Layout*) saat dibaca oleh sistem atau Agentic AI.

## 🏗️ Struktur Berkas & Pemicu Berantai (*Nested Triggers*)

Hierarki direktori dan pemicu sekuensial untuk alur kerja Agentic AI:

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
        └─> 📜 trigger_package_save <-- Pemicu Level 3 (Penyimpanan ke Memori Aktif)
```

## 🔄 Logika Eksekusi Otomatis

Alur kerja linier berantai dari root hingga penyimpanan memori aktif:

```text
[ Root Directory ]
  └─> Read: trigger_root
        └─> Read: daftar_font.txt
              └─> Masuk /panduan-sampel-font
                    ├─> Read: trigger_panduan & Run: auto_installer
                    ├─> Read: 1. SKILL.md (Instruksi Sistem & Anti-AI Slop Rules)
                    ├─> Read: strukturnya.txt (Panduan Operasional & Manfaat Desain)
                    └─> Execute: trigger_package_save -> Save ke Memori Aktif Agentic AI
```

## 🤖 Cara Pengoperasian & Eksekusi di Agentic AI

Anda dapat memicu alur eksekusi Agentic AI menggunakan salah satu dari dua cara di bawah ini:

### Opsi 1: Cara Tercepat (Komen Link GitHub & Prompt Direct) — *Tanpa Upload Berkas*

Gunakan cara ini untuk meminta Agentic AI membaca repositori GitHub Anda secara langsung menggunakan tautan (*link*):

1. **Format Komen Prompt di Chat AI**:
   Salin dan kirimkan salah satu perintah komen berikut di kolom chat:

   > `@Agentic AI baca https://github.com/IR-0058/desain-font-terhadap-buatan-Intelijen.git dan jalankan trigger_root`

   *Atau jika menggunakan perayap repositori/IDE (Cursor/VSCode):*

   > `Fetch repo https://github.com/IR-0058/desain-font-terhadap-buatan-Intelijen.git lalu jalankan sekuensial dari trigger_root sampai trigger_package_save`

2. **Eksekusi Otomatis**:
   AI akan langsung mengkloning/membaca repositori GitHub tersebut, mendeteksi `trigger_root`, membaca `daftar_font.txt`, mengeksekusi `auto_installer` di folder panduan, dan menyerap aturan di `1. SKILL.md` serta `strukturnya.txt`.

3. **Penguncian Memori**:
   Sistem mengakhiri alur pada `trigger_package_save` dan siap menerapkan aturan tipografi pada proyek Anda.

---

### Opsi 2: Upload Berkas `.zip` Langsung

Gunakan cara ini jika Anda ingin mengunggah berkas proyek dalam bentuk arsip compressed `.zip`:

1. **Unggah Berkas**:
   Unggah berkas `desain-font-terhadap-buatan-Intelijen.zip` (atau `model_font_triggered_project_v2.zip`) langsung ke kolom chat Agentic AI.

2. **Format Komen / Perintah Pengunggah**:
   Sertakan pesan singkat bersama berkas yang diunggah:

   > *"Tolong ekstrak zip ini, lalu jalankan alur pemicu berantai mulai dari `trigger_root` hingga `trigger_package_save`."*

3. **Penyimpanan Berantai**:
   AI mengekstrak folder, membaca indeks font, mengeksekusi skrip pendukung, dan mengunci seluruh aturan Anti-AI Slop ke dalam memori aktif.

---

## 🎯 Aturan Kontrol Kualitas (Anti-AI Slop)

1. **Pencegahan Visual Hallucination**: Menghindari penggunaan font acak yang tidak terinstal atau tidak kompatibel lintas platform.
2. **Batas Maksimal 2 Font**: Membatasi penggunaan font maksimal 2 jenis dalam satu tata letak/tampilan dokumen.
3. **Standar Konsistensi**: Menjaga rasio ukuran (`font-size`) dan ketebalan (`font-weight`) agar hasil desain AI tetap konsisten dan profesional.
