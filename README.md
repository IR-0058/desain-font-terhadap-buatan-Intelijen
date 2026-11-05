# Cara Cepat Pakai Skill `.LOGIC`
# Quick Way to Use the `.LOGIC` Skill

**Sumber / Source:** https://github.com/IR-0058/desain-font-terhadap-buatan-Intelijen

---

## Langkah 1 — Download ZIP
## Step 1 — Download the ZIP

**ID:** Buka repo di atas → tombol **Code** → **Download ZIP**. Ekstrak, pastikan ada folder `.LOGIC` berisi 5 file: `README.md`, `SKILL.md`, `daftar_font.txt`, `spesifikasi_font.txt`, `skill_bantu.md`.

**EN:** Open the repo above → **Code** button → **Download ZIP**. Extract it, make sure the `.LOGIC` folder with 5 files is there: `README.md`, `SKILL.md`, `daftar_font.txt`, `spesifikasi_font.txt`, `skill_bantu.md`.

---

## Langkah 2 — Lempar ke AI + Prompt
## Step 2 — Feed it to the AI + Prompt

**ID:** Buka chat baru dengan AI apa pun yang kamu pakai (Claude, ChatGPT, Gemini, dll), unggah/lampirkan kelima file tadi, lalu ketik prompt ini:

**EN:** Open a new chat with whichever AI you use (Claude, ChatGPT, Gemini, etc.), upload/attach all five files, then type this prompt:

```
Gabungkan isi README.md, SKILL.md, skill_bantu.md, spesifikasi_font.txt,
dan daftar_font.txt menjadi SATU file SKILL.md yang ringkas dan lengkap,
yang bisa langsung dipakai sebagai skill untuk memandu pengguna memilih
font dan menyusun dokumen lewat alur Turn 1-3. Jangan ubah nomor/nama
font. Format sebagai satu file markdown siap pakai.
```

```
Merge the contents of README.md, SKILL.md, skill_bantu.md,
spesifikasi_font.txt, and daftar_font.txt into ONE concise, complete
SKILL.md file that can be used directly as a skill to guide users
through font selection and document structuring via the Turn 1-3
flow. Don't change any font numbers/names. Format it as a single
ready-to-use markdown file.
```

---

## Langkah 3 — Simpan sebagai SKILL.md di perangkat
## Step 3 — Save it as SKILL.md on your device

**ID:** Setelah AI mengeluarkan hasilnya, simpan sebagai file `SKILL.md` di folder lokal perangkatmu (misalnya `Documents/skills/font-logic/SKILL.md`).

**EN:** Once the AI outputs the result, save it as a `SKILL.md` file in a local folder on your device (e.g. `Documents/skills/font-logic/SKILL.md`).

---

## Langkah 4 — Pasang sesuai AI yang dipakai
## Step 4 — Load it depending on which AI you use

| AI | ID — Cara pasang | EN — How to load it |
|---|---|---|
| **Claude (web/app)** | Unggah `SKILL.md` ke **Project Knowledge** pada sebuah Project | Upload `SKILL.md` to **Project Knowledge** in a Project |
| **Claude Code / Cowork** | Taruh di `~/.claude/skills/<nama>/SKILL.md` (skill personal) | Place it at `~/.claude/skills/<name>/SKILL.md` (personal skill) |
| **ChatGPT** | Buat **Custom GPT** → masukkan `SKILL.md` ke bagian *Knowledge* | Create a **Custom GPT** → add `SKILL.md` under *Knowledge* |
| **Gemini** | Buat **Gem** baru → tempel isi `SKILL.md` ke instruksi Gem | Create a new **Gem** → paste `SKILL.md` content into the Gem's instructions |
| **AI lain / lainnya** | Lampirkan `SKILL.md` di awal chat setiap kali mulai sesi baru | Attach `SKILL.md` at the start of every new chat session |

---

## Langkah 5 — Mulai pakai
## Step 5 — Start using it

**ID:** Di chat baru (dengan `SKILL.md` sudah terpasang/terlampir), cukup ketik kebutuhan dokumenmu. AI akan otomatis menampilkan menu kategori (Turn 1), lanjut rekomendasi font + draf (Turn 2), lalu konfirmasi font (Turn 3).

**EN:** In a new chat (with `SKILL.md` already loaded/attached), just type what document you need. The AI will automatically show the category menu (Turn 1), then font recommendations + draft (Turn 2), then font confirmation (Turn 3).
