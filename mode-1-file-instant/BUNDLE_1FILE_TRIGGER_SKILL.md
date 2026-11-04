# ALL-IN-ONE TRIGGER & SKILL: Panduan Sampel Font & Anti-AI Slop

## 1. PEMICU BERANTAI AUTOMATIS (NESTED TRIGGER)
[trigger_root] -> [trigger_panduan] -> [trigger_package_save]
Status: AUTO_EXECUTE_ON_READ

## 2. ATURAN UTAMA TIPOGRAFI (ANTI-AI SLOP RULES)
1. **Maksimal 2 Font per Desain**: HANYA boleh menggunakan 1 Font Utama (Display/Heading) dan 1 Font Sekunder (Body/Teks). Dilarang menumpuk >2 jenis font.
2. **Fallback Aksara Non-Latin Wajib**:
   - Latin: Arial, Helvetica, Roboto, Times New Roman, Calibri, Open Sans.
   - Hanzi Mandarin: STHeiti (华文黑体), PingFang SC, SimSun (中易宋体), STKaiti (华文楷体).
   - Stack CSS wajib memiliki fallback aksara lokal yang valid.
3. **Pencegahan Visual Hallucination**: Dilarang mengarang nama font fiktif atau menggunakan bobot font (font-weight) acak tanpa hierarki.

## 3. INVENTARIS FONT INDEX
1. Arial (Latin)
2. Times New Roman (Latin)
3. Helvetica (Latin)
4. Calibri (Latin)
5. Roboto (Latin)
6. Open Sans (Latin)
7. STHeiti / 华文黑体 (Hanzi Sans)
8. STKaiti / 华文楷体 (Hanzi Script)
9. SimSun / 中易宋体 (Hanzi Serif)
10. PingFang SC (Hanzi Sans)

## 4. PENYIMPANAN MEMORI
Simpan aturan di atas ke memori aktif sesi desain ini.
