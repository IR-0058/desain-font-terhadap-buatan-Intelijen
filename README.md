# 🎨 Cara Cepat Menggunakan Skill .LOGIC (`panduan-sampel-font`)

<p align="left">
  <img src="https://img.shields.io/badge/Status-Ready-brightgreen?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Version-2.0-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Platform-Claude%20%7C%20ChatGPT%20%7C%20Gemini-orange?style=for-the-badge" alt="Platforms">
</p>

---

🔗 **Sumber Repositori:**  
👉 [GitHub — `IR-0058/desain-font-terhadap-buatan-Intelijen`](https://github.com/IR-0058/desain-font-terhadap-buatan-Intelijen)

---

## 📥 Langkah 1 — Unduh Repositori

> [!TIP]
> **Petunjuk Cepat:** Anda hanya perlu mengunduh file ZIP sekali untuk mendapatkan seluruh instruksi dan daftar font.

1. Buka repositori GitHub melalui tautan di atas.
2. Klik tombol hijau **`Code`** $\rightarrow$ Pilih 📥 **`Download ZIP`**.
3. Ekstrak file ZIP di perangkat Anda.
4. Pastikan struktur berkas di dalam folder memuat:

```text
📦 desain-font-terhadap-buatan-Intelijen
 ┣ 📄 README.md
 ┗ 📂 panduan-sampel-font/
    ┣ 📜 1. SKILL.md             <-- (Instruksi Utama Skill)
    ┣ 📜 PLATFORM_SETUP.md        <-- (Panduan Lanjutan)
    ┣ 📄 daftar_font.txt         <-- (Basis Data Font)
    ┣ 📄 strukturnya.txt
    ┣ 🐍 auto_installer.py        <-- (Skrip Pemasangan Otomatis)
    ┗ 📂 adapters/                <-- (Khusus Claude, Gemini, Copilot, dll.)
```

---

## ⚙️ Langkah 2 — Pemasangan Sesuai Platform AI

Pilih metode di bawah ini sesuai dengan platform AI yang Anda gunakan:

| Platform AI | Status | 🛠️ Cara Memasang / Memuat |
| :--- | :---: | :--- |
| <img src="https://img.shields.io/badge/Claude-705846?style=flat-square&logo=anthropic&logoColor=white"/> | `Recommended` | Buat **Project** baru $\rightarrow$ Buka **Project Knowledge** $\rightarrow$ Unggah `1. SKILL.md` & `daftar_font.txt`. |
| <img src="https://img.shields.io/badge/Claude_Code-111111?style=flat-square&logo=terminal&logoColor=white"/> | `Advanced` | Salin folder `panduan-sampel-font/` ke direktori lokal `~/.claude/skills/panduan-sampel-font/SKILL.md`. |
| <img src="https://img.shields.io/badge/ChatGPT-74aa9c?style=flat-square&logo=openai&logoColor=white"/> | `Popular` | Pilih **Explore GPTs** $\rightarrow$ **Create** $\rightarrow$ Di tab **Configure**, unggah `1. SKILL.md` & `daftar_font.txt` ke bagian **Knowledge**. |
| <img src="https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white"/> | `Easy` | Buat **Gem** baru $\rightarrow$ Salin seluruh isi file `1. SKILL.md`, lalu tempelkan (*paste*) ke kolom **Instructions**. |
| <img src="https://img.shields.io/badge/Python_Script-3776AB?style=flat-square&logo=python&logoColor=white"/> | `Auto` | Jalankan `python auto_installer.py` di terminal lokal Anda untuk memasang adapter secara otomatis. |
| <img src="https://img.shields.io/badge/Chat_Biasa-Gray?style=flat-square"/> | `Quick` | Lampirkan file `1. SKILL.md` (dan `daftar_font.txt`) langsung di kolom percakapan saat membuka chat baru. |

---

## 🚀 Langkah 3 — Cara Menggunakan Dalam Percakapan

> [!NOTE]
> Setelah skill terpasang, Anda **TIDAK PERLU** memasukkan prompt penggabungan file. Cukup ketik langsung kebutuhan dokumen Anda!

### 💬 Contoh Prompt Siap Pakai:

> 🟢 *"Saya ingin membuat dokumen proposal bisnis formal untuk klien perbankan."*  
> 🔵 *"Buatkan draf laporan penelitian ilmiah dengan format font yang sesuai."*

---

### 🔄 Alur Kerja Otomatis AI (`Turn 1` – `Turn 3`):

```mermaid
graph TD
    A[🟡 Turn 1: Analisis & Kategori] --> B[🔵 Turn 2: Draf & Opsi Font]
    B --> C[🟢 Turn 3: Konfirmasi & Output Final]
```

1. <mark><b>Turn 1 — Menu Kategori:</b></mark>  
   AI menganalisis kebutuhan dokumen Anda dan menampilkan pilihan kategori beserta arah desain awal.

2. <mark><b>Turn 2 — Rekomendasi Font & Draf:</b></mark>  
   AI membuat draf isi dokumen sekaligus memberikan rekomendasi kombinasi font (Latin / Non-Latin / Mandarin) yang estetis dan berhierarki.

3. <mark><b>Turn 3 — Konfirmasi & Finalisasi:</b></mark>  
   Anda memilih pasangan font yang diinginkan, lalu AI mengunci format serta memberikan rincian teknis penataan dokumen.
