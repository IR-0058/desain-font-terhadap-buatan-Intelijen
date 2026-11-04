# Panduan Alur Kerja Repositori (Internal & Multi-AI Compatibility)

Repositori ini memuat **Skill Panduan Sampel Font & Anti-AI Slop Layout** yang dilengkapi pemicu berantai (*nested triggers*) serta pembagian folder sesuai kemampuan pembacaan berkas AI.

---

## 📂 Struktur Folder Repositori

```text
desain-font-terhadap-buatan-Intelijen/
│
├── 📁 /mode-1-file-instant/            <-- [KHUSUS AI 1 FILE / PROMPT ONLY]
│   └── 📄 BUNDLE_1FILE_TRIGGER_SKILL.md  (GABUNGAN: Triggers + Anti-AI Slop + Font Index)
│
├── 📁 /mode-2-file-lite/               <-- [KHUSUS AI 2 FILE LIMIT]
│   ├── 📜 1_TRIGGERS_AND_INDEX.json     (Level 1 & 2 Triggers + Daftar Font)
│   └── 📄 2_SKILL_AND_RULES.md          (Aturan Anti-AI Slop Layout)
│
└── 📁 /panduan-sampel-font/            <-- [KHUSUS AGENTIC / FULL CODE AI]
    ├── 📜 trigger_root.json
    ├── 📜 trigger_panduan.json
    ├── 📜 trigger_package_save.json
    ├── 🐍 auto_installer.py
    ├── 📄 1. SKILL.md
    └── 📄 strukturnya.txt
```

---

## 🎯 Aturan Kualitas Anti-AI Slop

1. **Maksimal 2 Font per Desain**: 1 Font Utama (Heading/Display) + 1 Font Sekunder (Body).
2. **Fallback Aksara Non-Latin Wajib**: Menyediakan font CJK/Hanzi valid (STHeiti, PingFang SC, SimSun, STKaiti).
3. **Pencegahan Visual Hallucination**: Dilarang menggunakan nama font fiktif atau bobot font (*font-weight*) acak.
