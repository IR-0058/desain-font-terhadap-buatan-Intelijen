# Panduan Alur Kerja Repositori: desain-font-terhadap-buatan-Intelijen

Repositori ini memuat **Skill Panduan Sampel Font & Anti-AI Slop Layout** yang dilengkapi pemicu berantai (*nested triggers*) serta pembagian folder sesuai kapasitas pembacaan berkas berbagai platform AI.

---

## 📂 Struktur Berkas & Pembagian Folder

```text
desain-font-terhadap-buatan-Intelijen/
│
├── 📁 mode-1-file-instant/            <-- [KHUSUS AI 1 BERKAS / PROMPT TEXT]
│   └── BUNDLE_1FILE_TRIGGER_SKILL.md  (Gabungan Triggers + Anti-AI Slop + Indeks Font)
│
├── 📁 mode-2-file-lite/               <-- [KHUSUS AI LIMIT 2 BERKAS]
│   ├── 1_TRIGGERS_AND_INDEX.json     (Pemicu Level 1 & 2 + Indeks Font)
│   └── 2_SKILL_AND_RULES.md          (Aturan Anti-AI Slop)
│
└── 📁 panduan-sampel-font/            <-- [KHUSUS AGENTIC / FULL CODE AI]
    ├── trigger_root.json
    ├── trigger_panduan.json
    ├── trigger_package_save.json
    ├── auto_installer.py
    ├── 1. SKILL.md
    └── strukturnya.txt
```

---

## 🚀 Cara Mengoperasikan di Agentic AI

### 1. Cara 1: Lewat Perintah Sederhana (Cara Tercepat / Text Prompt)

Jika AI tidak memiliki fitur pembacaan file/link repositori eksternal, cukup salin dan tempel perintah pemicu sederhana ini ke dalam chatbox:

> **Salin Prompt Ini:**
> *"Jalankan pemicu berantai: trigger_root -> trigger_panduan -> trigger_package_save. Terapkan aturan Anti-AI Slop: maksimal 2 font per desain (1 Heading + 1 Body), sediakan fallback aksara Non-Latin (Hanzi/CJK), dan hindari visual hallucination."*

---

### 2. Cara 2: Lewat Berkas `.zip` (Upload Langsung)

Jika menggunakan AI yang mendukung instruksi pengunggahan berkas/folder:

1. Unggah berkas `desain-font-terhadap-buatan-Intelijen-master.zip` ke dalam sesi chatbox.
2. Ketik instruksi pemicu sederhana berikut:

> **Salin Prompt Ini:**
> *"Ekstrak berkas .zip ini dan jalankan pemicu berantai trigger_root hingga trigger_package_save. Simpan aturan Anti-AI Slop ke dalam memori aktif."*

---

## 🎯 Aturan Kualitas Anti-AI Slop (Aktif)

1. **Maksimal 2 Font per Desain**: Hanya mengombinasikan 1 Font Utama (Heading/Display) dan 1 Font Sekunder (Body Text).
2. **Fallback Aksara Non-Latin Wajib**: Menyediakan stack CSS font CJK/Hanzi valid (*STHeiti, PingFang SC, SimSun, STKaiti*).
3. **Pencegahan Visual Hallucination**: Menghindari penggunaan nama font fiktif atau variasi bobot font (*font-weight*) acak.
