# ANTI-AI-SLOP DESIGN INTELLIGENCE — UNIVERSAL 1-FILE BUNDLE
Version: 3.0.0 | Language: Indonesian | Use: paste as system/project/Gem/Agent instruction where supported

## TRIGGER CHAIN
On read, follow this logical sequence (manual if the host does not support automation):
1. `trigger_root`: read the font index and route to the typography skill.
2. `trigger_panduan`: apply the design and validation rules below.
3. `trigger_package_save`: prepare a platform-specific persistence action and report only verified status.

**Important:** text triggers are not executable plugins. Reading this file does not install software, change model weights, or automatically save an account memory.

## CORE RULES
- Maximum **two primary font families** per design: one Heading/Display + one Body. Use one family when sufficient.
- Font fallback for glyph coverage is a compatibility chain, not an extra decorative font style. If a strict two-file-font limit applies, use two verified multi-script families only.
- Use real, target-platform-supported font names and weights only. Never invent fonts, foundries, licenses, language coverage, glyphs, or preview claims.
- Include CJK/Hanzi fallback only when those characters are present or expected. Verify target operating system and actual glyph coverage.
- Do not introduce unrequested text, logos, icons, watermarks, objects, shadows, glow, textures, or visual effects.
- Do not claim a screenshot/render/font availability has been tested unless it has actually been tested.
- For important text in AI-generated images, generate a clean visual and typeset the text separately when exact spelling/glyph fidelity matters.

## FONT INDEX
Latin: Arial; Times New Roman; Helvetica; Calibri; Roboto; Open Sans.
Hanzi/CJK: STHeiti / 华文黑体; PingFang SC; SimSun / 中易宋体; STKaiti / 华文楷体.
OS fallback examples: Windows — Microsoft YaHei, SimSun, KaiTi; macOS/iOS — PingFang SC, STHeiti; Linux — Noto Sans CJK SC, Noto Serif CJK SC (if installed).
This is a reference index, not proof the fonts are installed. Verify before use.

## CSS TEMPLATE
```css
:root {
  --font-heading: "Roboto", "PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
  --font-body: "Open Sans", "SimSun", "Noto Serif CJK SC", serif;
}
h1, h2, h3 { font-family: var(--font-heading); }
body, p, li { font-family: var(--font-body); }
```
Fallbacks are selected only as required by installed fonts and glyph coverage; they are not meant to appear as simultaneous decorative styles.

## DESIGN VALIDATION
Before delivery: identify scripts; select one/two primary families; validate font availability/weight/glyphs or mark unverified; inspect hierarchy/contrast/line-height/overflow/clipping; remove unsupported/unrequested visuals; state what was actually checked.

## PLATFORM PERSISTENCE
Save these instructions through the service's own documented global instructions, project instructions, Gem/Skill, Agent, Brand Kit, or repository rules. The integration guide in `PLATFORM_SETUP.md` identifies known mechanisms and limits. If the service has no lasting instruction feature, use this file as a per-project or per-session prompt. Never state that all listed AI services have been updated.

## EXECUTION RULE
If the host cannot execute Python or read sibling files, continue using this complete one-file bundle. Do not fail merely because an automation trigger is unavailable.
