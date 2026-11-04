#!/usr/bin/env python3
"""Local package validator and project-instruction adapter installer.

This script does NOT connect to AI services, alter model weights, or save cloud memories.
It only validates this package and can copy plain-text instruction files into a local repo.
"""
from __future__ import annotations
import argparse
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REQUIRED = ["trigger_root.json", "trigger_panduan.json", "trigger_package_save.json", "1. SKILL.md", "strukturnya.txt", "daftar_font.txt", "PLATFORM_SETUP.md"]
ADAPTERS = {
    "AGENTS.md": HERE / "adapters" / "AGENTS.md",
    "GEMINI.md": HERE / "adapters" / "GEMINI.md",
    "CLAUDE.md": HERE / "adapters" / "CLAUDE.md",
    ".github/copilot-instructions.md": HERE / "adapters" / "copilot-instructions.md",
    ".cursor/rules/anti-ai-slop.mdc": HERE / "adapters" / "anti-ai-slop.mdc",
}

def check() -> bool:
    errors = []
    for name in REQUIRED:
        if not (HERE / name).is_file():
            errors.append(f"File wajib tidak ditemukan: {name}")
    for name in ("trigger_root.json", "trigger_panduan.json", "trigger_package_save.json"):
        p = HERE / name
        if p.exists():
            try:
                json.loads(p.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"JSON tidak valid ({name}): {exc}")
    try:
        root = json.loads((HERE / "trigger_root.json").read_text(encoding="utf-8"))
        chain = root.get("execution_chain", [])
        if chain != ["trigger_root", "trigger_panduan", "trigger_package_save"]:
            errors.append("Urutan trigger_root -> trigger_panduan -> trigger_package_save tidak sesuai.")
    except Exception:
        pass
    skill = (HERE / "1. SKILL.md").read_text(encoding="utf-8") if (HERE / "1. SKILL.md").exists() else ""
    for term in ("dua keluarga font", "CJK", "hallucination", "Jangan pernah"):
        if term.lower() not in skill.lower():
            errors.append(f"Aturan skill belum memuat frasa pemeriksaan: {term}")
    if errors:
        print("[FAIL] Validasi paket gagal:")
        for e in errors:
            print(" -", e)
        return False
    print("[OK] Struktur dan JSON valid.")
    print("[OK] Rantai trigger: trigger_root -> trigger_panduan -> trigger_package_save.")
    print("[OK] Aturan font, fallback CJK, dan anti-hallucination ditemukan.")
    print("[INFO] Ini hanya validasi lokal; tidak ada AI cloud/plugin/memori model yang diubah.")
    return True

def install_local(target: Path, force: bool = False) -> int:
    target = target.expanduser().resolve()
    if not target.exists() or not target.is_dir():
        print(f"[FAIL] Folder target tidak ada atau bukan direktori: {target}")
        return 2
    written = 0
    for relative, source in ADAPTERS.items():
        if not source.is_file():
            print(f"[SKIP] Adapter tidak ditemukan: {source}")
            continue
        dest = target / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and not force:
            print(f"[SKIP] Sudah ada (tidak ditimpa): {dest}")
            continue
        if dest.exists() and force:
            backup = dest.with_suffix(dest.suffix + ".bak")
            shutil.copy2(dest, backup)
            print(f"[BACKUP] {backup}")
        shutil.copy2(source, dest)
        print(f"[WRITE] {dest}")
        written += 1
    print(f"[DONE] {written} file instruksi lokal dibuat.")
    print("[LIMIT] File lokal hanya dipakai oleh agent/platform yang memang membaca format tersebut.")
    print("[LIMIT] Tidak ada koneksi atau penyimpanan otomatis ke akun cloud AI.")
    return 0

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate package and install local project instruction adapters.")
    parser.add_argument("--check", action="store_true", help="Validate the package (default action).")
    parser.add_argument("--install-local", metavar="PROJECT_DIR", help="Copy instruction adapters into a local project directory.")
    parser.add_argument("--force", action="store_true", help="Back up and replace existing adapter files.")
    args = parser.parse_args()
    if not check():
        return 1
    if args.install_local:
        return install_local(Path(args.install_local), args.force)
    return 0

if __name__ == "__main__":
    sys.exit(main())
