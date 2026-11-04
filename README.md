# desain-font-terhadap-buatan-Intelijen — v3.0.0

Paket ini mengemas aturan Anti-AI Slop dengan tiga cara distribusi sesuai batas file AI.

## Struktur
```text
desain-font-terhadap-buatan-Intelijen/
├── mode-1-file-instant/
│   └── BUNDLE_1FILE_TRIGGER_SKILL.md
├── mode-2-file-lite/
│   ├── 1_TRIGGERS_AND_INDEX.json
│   └── 2_SKILL_AND_RULES.md
└── panduan-sampel-font/
    ├── trigger_root.json
    ├── trigger_panduan.json
    ├── trigger_package_save.json
    ├── auto_installer.py
    ├── 1. SKILL.md
    ├── daftar_font.txt
    ├── strukturnya.txt
    ├── PLATFORM_SETUP.md
    └── adapters/
```

## Pilih mode
- **Mode 1:** unggah/salin satu Markdown ke AI yang hanya menerima satu berkas atau prompt.
- **Mode 2:** unggah dua berkas JSON + Markdown sesuai namanya.
- **Mode 3:** untuk agent yang dapat membaca file dan menjalankan Python. Jalankan `python auto_installer.py --check` dari folder `panduan-sampel-font`.

## Instalasi lokal untuk repo coding
```bash
python auto_installer.py --install-local "PATH_KE_REPO"
```
Skrip membuat adapter `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, dan `.cursor/rules/anti-ai-slop.mdc`. File yang sudah ada tidak ditimpa kecuali menggunakan `--force` (akan dibuat backup `.bak`).

## Yang paket ini tidak lakukan
- Tidak memasang satu plugin universal ke 58+ layanan AI.
- Tidak mengubah bobot/otak model.
- Tidak menulis ke akun cloud tanpa fitur resmi, autentikasi, izin, dan tindakan pengguna.
- Tidak dapat menjamin bahwa setiap generator visual mematuhi tipografi atau merender Hanzi dengan akurat.

Status “permanen” hanya benar dalam scope yang disimpan: akun, Gem/Skill, proyek, repo, agent, brand kit, atau workflow tertentu. Lihat `panduan-sampel-font/PLATFORM_SETUP.md`.
