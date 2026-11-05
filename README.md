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

🎨 Cara Cepat Menggunakan Skill .LOGIC (panduan-sampel-font)🔗 Sumber Repositori:
👉 GitHub — IR-0058/desain-font-terhadap-buatan-Intelijen📥 Langkah 1 — Unduh Repositori[!TIP]
Petunjuk Cepat: Anda hanya perlu mengunduh file ZIP sekali untuk mendapatkan seluruh instruksi dan daftar font.Buka repositori GitHub melalui tautan di atas.Klik tombol hijau Code $\rightarrow$ Pilih 📥 Download ZIP.Ekstrak file ZIP di folder lokal komputer Anda.Pastikan isi folder memuat struktur berikut:📦 desain-font-terhadap-buatan-Intelijen
 ┣ 📄 README.md
 ┗ 📂 panduan-sampel-font/
    ┣ 📜 1. SKILL.md             <-- (Instruksi Utama Skill)
    ┣ 📜 PLATFORM_SETUP.md        <-- (Panduan Lanjutan Platform)
    ┣ 📄 daftar_font.txt         <-- (Daftar & Spesifikasi Font)
    ┣ 📄 strukturnya.txt
    ┣ 🐍 auto_installer.py        <-- (Skrip Pemasangan Otomatis)
    ┗ 📂 adapters/                <-- (Khusus Claude, Gemini, Copilot, dll.)
⚙️ Langkah 2 — Panduan Langkah-demi-Langkah Pemasangan per PlatformPilih platform/aplikasi AI yang Anda gunakan di browser Google Chrome atau desktop:🔵 1. Google Chrome — Gemini (gemini.google.com)Metode A: Menggunakan Fitur Gems (Permanen)Buka gemini.google.com di Google Chrome.Di panel sebelah kiri, klik Gems Manager (atau Create Gem / Gem Builder).Beri nama Gem, contoh: Logic Font Assistant.Buka berkas 1. SKILL.md dengan Notepad/Text Editor, salin seluruh isinya, lalu tempelkan (paste) ke kolom Instructions di Gem.Klik Save. Sekarang Anda bisa memakai skill ini kapan saja lewat menu Gems.Metode B: Melalui Chat Biasa / Side Panel ChromeBuka chat Gemini di Google Chrome.Klik ikon 📎 Lampirkan File / Upload File.Unggah file 1. SKILL.md dan daftar_font.txt.Ketik kebutuhan dokumen Anda di kolom chat.🟢 2. ChatGPT (chatgpt.com)Metode A: Menggunakan Custom GPT (Permanen untuk ChatGPT Plus/Team/Pro)Buka chatgpt.com $\rightarrow$ Klik Explore GPTs $\rightarrow$ Klik + Create.Masuk ke tab Configure.Masukkan nama: Font & Layout Designer.Scroll ke bawah ke bagian Knowledge $\rightarrow$ Klik Upload files.Unggah berkas 1. SKILL.md dan daftar_font.txt.Klik Save / Publish (Only me / Anyone with link).Metode B: Chat Biasa (ChatGPT Gratis)Buka percakapan baru di ChatGPT.Klik ikon 📎 (Plus/Attach) $\rightarrow$ Unggah 1. SKILL.md.Tuliskan permintaan dokumen Anda.🟠 3. Anthropic Claude (claude.ai)Metode A: Menggunakan Claude Projects (Rekomendasi)Buka claude.ai $\rightarrow$ Klik menu Projects $\rightarrow$ Create Project.Beri nama proyek (misal: Desain Dokumen & Font).Di kolom Project Knowledge, klik Add Content / Upload.Unggah berkas 1. SKILL.md dan daftar_font.txt.Mulai percakapan di dalam project tersebut.Metode B: Claude Code / Terminal CLISalin folder panduan-sampel-font/ ke direktori lokal:
~/.claude/skills/panduan-sampel-font/SKILL.mdClaude Code akan mendeteksi skill secara otomatis.🟣 4. Microsoft Copilot & Aplikasi AI Lainnya (Web / Desktop)Buka browser atau aplikasi AI pilihan Anda (Microsoft Copilot, Perplexity, Poe, Ollama GUI, dll).Lampirkan file 1. SKILL.md pada pesan pertama sesi chat baru.Atau buka file 1. SKILL.md, salin teks instruksi utamanya, dan tempelkan sebagai system prompt / instruksi awal.🐍 5. Pemasangan Otomatis (Skrip Python)Jika Anda menggunakan lingkungan lokal/CLI:Buka Terminal / Command Prompt di folder hasil ekstraksi ZIP.Jalankan perintah:python panduan-sampel-font/auto_installer.py
Skrip akan memasang adapter secara otomatis ke sistem/AI lokal Anda.🚀 Langkah 3 — Cara Menggunakan Dalam Percakapan[!NOTE]
Setelah skill terpasang di platform AI pilihan Anda, Anda TIDAK PERLU menjalankan prompt rumit untuk menggabungkan file. Cukup ketik langsung kebutuhan dokumen Anda!+-----------------------------------------------------------------------+
|                              ALUR KERJA                               |
|                                                                       |
|  [ Input Pengguna ] ---> ( Turn 1: Menu Kategori & Analisis )         |
|                                 |                                     |
|                                 v                                     |
|                          ( Turn 2: Draf & Rekomendasi Font )          |
|                                 |                                     |
|                                 v                                     |
|                          ( Turn 3: Konfirmasi & Output Final )        |
+-----------------------------------------------------------------------+
💬 Contoh Prompt Siap Pakai:🟢 "Saya ingin membuat dokumen proposal bisnis formal untuk klien perbankan."🔵 "Buatkan draf laporan penelitian ilmiah dengan format font yang sesuai."🔴 "Saya butuh desain pamflet promosi produk UMKM makanan lokal."🔄 Penjelasan Alur Kerja (Turn 1 – Turn 3):Turn 1 — Menu Kategori:AI menganalisis kebutuhan dokumen Anda dan menampilkan pilihan kategori beserta arah hierarki visual.Turn 2 — Rekomendasi Font & Draf Konten:AI menyusun draf isi dokumen sekaligus memberikan rekomendasi kombinasi font (Latin / Non-Latin / Mandarin) yang presisi.Turn 3 — Konfirmasi & Finalisasi:Anda mengonfirmasi pasangan font pilihan, lalu AI mengunci format serta memberikan panduan penataan spesifikasi cetak/digital lengkap.
