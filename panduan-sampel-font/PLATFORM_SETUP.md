# Platform adoption & persistence guide

**Scope:** daftar di bawah memetakan jalur integrasi yang paling masuk akal, bukan menyatakan bahwa paket ini sudah terpasang pada semua layanan. Fitur, nama menu, plan, dan ketersediaan dapat berubah. Status penyimpanan harus diuji di akun yang digunakan.

## Mekanisme persisten yang terdokumentasi

| Layanan | Jalur penyimpanan | Batas penting |
|---|---|---|
| ChatGPT | Project settings → Project instructions; gunakan Custom Instructions bila tersedia | Instruksi proyek hanya berlaku di proyek tersebut; memori bukan penyimpanan sempurna untuk seluruh isi file. |
| Google Gemini | Buat Gem, isi Instructions, unggah SKILL.md pada Knowledge, lalu klik Save. Dokumen bantuan mengumumkan transisi Gems ke Skills untuk akun pribadi mulai November 2026. | Pastikan status setelah transisi pada akun masing-masing. |
| Microsoft Copilot | Copilot Chat → Settings → Chat settings → Personalization → Custom instructions → Save instructions | Tergantung jenis akun/tenant dan ketersediaan fitur. |
| Claude | Profile Preferences untuk preferensi umum; Project Instructions dan Project Knowledge untuk proyek | Preferensi akun dan instruksi proyek punya lingkup berbeda. |
| Canva Magic Studio | Brand → Brand Kits → Brand voice | Pedoman Brand voice memiliki batas 500 karakter; ini bukan pemasangan SKILL penuh. |
| GitHub Copilot | Tambahkan `.github/copilot-instructions.md` pada repositori; path-specific instructions bila perlu | Berlaku pada fitur/IDE Copilot yang mendukung custom instructions. |
| Notion AI | Settings → Notion AI → Instructions; Custom Agents memiliki instructions masing-masing | Personal Notion Agent instructions tidak otomatis mengubah instruksi Custom Agents. |
| Cursor AI | Customize → Rules untuk User Rules; `.cursor/rules/*.mdc` untuk Project Rules | Aturan global dan aturan repositori punya scope berbeda. |
| Midjourney | Personalization profile / Style Reference | Preferensi estetika, bukan instruksi permanen yang menjamin jumlah font atau teks akurat. |

## Daftar layanan yang diminta

| Platform | Jalur integrasi yang direkomendasikan | Ruang lingkup / catatan |
|---|---|---|
| ChatGPT (OpenAI) | Project instructions / Custom Instructions; upload this skill as project knowledge where supported | Persistent at project/account scope; not model-weight memory. |
| Google Gemini | Custom Gem instructions + attach skill as Knowledge; note transition from Gems to Skills announced for Nov 2026 on personal accounts | Saved Gem/Skill scope; save explicitly after preview. |
| Microsoft Copilot | Chat settings > Personalization > Custom instructions | Account/workspace personalization; availability may depend on account type. |
| Claude (Anthropic) | Profile Preferences and/or Project Instructions; attach SKILL.md as project knowledge | Account preference or project scope. |
| Canva Magic Studio | Brand Kit > Brand voice; paste condensed rules and keep full skill as external project reference | Brand voice is narrower than a full skill; Canva documents a 500-character guidance limit. |
| DeepL Translate | Use glossary/style rules for terminology; paste relevant rule in task context | Terminology glossary is not a universal AI system prompt. |
| DeepSeek | System prompt in a supported API/client, or paste bundle into task/project prompt | Depends on interface; no cross-product global persistence assumed. |
| Character.AI | Character definition/persona or chat setup, if the active product surface allows it | Character-scoped, not account-wide model memory. |
| Perplexity AI | Space/custom instruction feature if visible; otherwise use the one-file prompt per Space/task | Feature and plan dependent; verify saved state. |
| Midjourney | Personalization profile / Style Reference for aesthetic preference; include typography constraints in each relevant prompt | Style profile is not a full policy or font-rendering guarantee. |
| Grok (xAI / X) | Paste the compact rule in each task or use an approved connected knowledge store | Do not assume a persistent instruction field; verify current UI. |
| JanitorAI | Character/system prompt or preset, where exposed | Character/preset scoped; not global memory. |
| Grammarly AI | Brand/style guide or writing preferences, if available in the workspace | Writing-style guidance, not a visual-design plugin. |
| QuillBot | Saved writing preference/preset where available; otherwise paste per task | Do not assume global design-rule persistence. |
| CapCut AI | Project template/brand preset and prompt; keep a copy of the skill in project notes | Project-scoped; no universal AI policy install. |
| Adobe Firefly | Brand/style reference or project prompt; attach skill to a team workflow where supported | Visual reference is not equivalent to persistent system instructions. |
| GitHub Copilot | Create `.github/copilot-instructions.md`; optional path-specific instructions | Repository-persistent for supported Copilot features. |
| Notion AI | Settings > Notion AI > Instructions; Custom Agents need their own instructions | Personal Notion Agent instructions and Custom Agent instructions are separate. |
| ElevenLabs | Project/voice workflow notes; paste only rules relevant to visual/text deliverables | Voice settings do not make typography rules global. |
| Suno AI | Song/project prompt or reusable style text | Prompt/preset scope; typography rule is relevant only for associated artwork. |
| Udio | Song/project prompt or reusable style text | Prompt/preset scope; typography rule is relevant only for associated artwork. |
| Runway (Gen-2 / Gen-3) | Project prompt and visual reference; keep typography constraints in project notes | Project/task scope unless a dedicated instruction store is shown. |
| Luma Dream Machine | Prompt and reusable visual reference | Prompt/reference scope; verify text rendering separately. |
| Kling AI | Prompt/project reference | Prompt/project scope; no global skill assumed. |
| Pika Labs | Prompt or project preset | Prompt/project scope; no global skill assumed. |
| Leonardo.Ai | Style/preset/profile plus prompt constraints | Style profiles guide appearance; do not equate with persistent policy. |
| Cursor AI | Global User Rules and/or `.cursor/rules/anti-ai-slop.mdc` | Global user rules can sync; project rules can be version controlled. |
| v0.dev (Vercel) | Project prompt/knowledge or reusable design-system instructions | Use per project unless the current UI offers a saved global instruction setting. |
| Hugging Face | Model/deployment system prompt or Space configuration controlled by the deployment owner | Depends on model wrapper and deployment; not a universal Hugging Face setting. |
| Civitai | Saved workflow/prompt metadata | Workflow/preset scope; no common global instruction layer assumed. |
| Stable Diffusion (WebUI / ComfyUI) | Save prompt templates, styles, or ComfyUI workflow with notes | Local workflow persistence; must explicitly load the workflow/template. |
| Ideogram | Prompt and reusable style/reference settings where available | Do not assume persistent typography policy. |
| Magnific AI | Project/prompt notes and repeatable enhancement preset | Project/task scope. |
| NovelAI | Preset/lorebook or prompt template for the relevant project | Preset scoped; visual-font rules may need manual application. |
| Humata.ai | Workspace/document context and prompt | Workspace/session context; confirm any saved instructions feature. |
| Haiper AI | Prompt/project template | Prompt/project scope. |
| Meshy 3D | Project prompt and asset notes | Project scope; typography applies to textures/UI labels only when present. |
| Tripo3D | Project prompt and asset notes | Project scope; typography applies to textures/UI labels only when present. |
| Sora (OpenAI) | Use ChatGPT Project instructions for planning where applicable; include constraints in Sora prompt | Do not assume Sora itself inherits ChatGPT Memory or project instructions. |
| Tome AI | Prompt/project notes | Project/task scope; verify saved settings. |
| Gamma App | Brand theme/brand settings or presentation project instructions | Theme controls are not a substitute for complete skill instructions. |
| Otter.ai | Meeting vocabulary/instructions or workspace settings when available | Meeting transcription preferences do not enforce visual design rules. |
| Descript | Project/brand templates and project notes | Project-scope workflow guidance. |
| InVideo AI | Brand kit or project prompt, when available | Brand assets may persist; include typography rule in project prompt. |
| HeyGen | Brand kit/brand voice and video project prompt | Brand settings apply within supported creation workflows. |
| Synthesia | Brand kit/template and project instructions | Brand/template scope; verify supported fields in workspace. |
| Scribe AI | Workspace style/template preferences where available | If no instruction field, use task prompt and edit checklist. |
| Phind | Session prompt or project-level instruction if offered | No global persistence assumed. |
| Codeium | Use current product's workspace/global rules if available; otherwise project instruction file | Product naming/features can change; verify current Windsurf/Codeium UI. |
| Replit Ghostwriter | Project instruction file or Agent prompt, if supported by the active Replit Agent | Project scope; verify the supported filename/feature before relying on it. |
| AlphaFold (DeepMind) | Wrap the research workflow with a separate agent/system prompt | Scientific model/tool, not a general-purpose assistant plugin host. |
| MusicLM / AudioLM | Prompt/config in the research or serving wrapper | Model-level serving configuration; not a shared chat memory. |
| AutoGPT / BabyAGI | Agent task/system instructions and project config | Depends on the deployed agent framework and its storage. |
| OpenDevin / Devin | Repository instructions and agent task/policy configuration | Agent/repository scope; permission and execution behavior remain platform-controlled. |
| Vicuna / Alpaca | System prompt in the serving UI/API/chat template | Depends on the inference wrapper; not built into the model weights. |
| WizardLM | System prompt in the serving UI/API/chat template | Depends on inference wrapper. |
| ChatGLM | System prompt/chat template in the API or UI wrapper | Depends on deployment; no common global memory. |
| StarCoder | IDE/repository instruction wrapper around the model | Model itself is not a shared persistent instruction service. |
| Bark | Prompt/config in the application wrapper; typography rules only for associated visual workflow | Audio model; no universal design skill plugin. |
| Reka AI | Prompt/context or workspace instructions if exposed by the current product | Verify platform feature; otherwise per-task prompt. |

## Catatan penerapan
- Untuk layanan yang memiliki kolom instruksi permanen, simpan versi ringkas pada kolom tersebut dan lampirkan `1. SKILL.md` atau bundle satu berkas sebagai knowledge/context jika didukung.
- Untuk generator gambar/video/audio, aturan ini terutama mengatur prompt, brief, brand kit, workflow, dan pemeriksaan hasil. Ia tidak dapat memaksa model menghasilkan teks/glyph dengan akurasi sempurna.
- Untuk model open-source/hosted model, aturan harus ditempatkan pada system prompt, chat template, aplikasi pembungkus, atau orchestrator. Mengubah prompt tidak mengubah bobot model.
- Jika platform tidak memiliki tempat menyimpan instruksi, gunakan bundle satu berkas di awal sesi atau simpan sebagai preset/workflow lokal. Statusnya bukan global dan bisa hilang saat sesi/proyek baru.

## Referensi resmi yang telah diperiksa
- OpenAI ChatGPT Projects: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- OpenAI Memory: https://help.openai.com/en/articles/8590148-memory-in-chatgpt
- Google Gemini Gems: https://support.google.com/gemini/answer/15146780
- Microsoft Copilot custom instructions: https://support.microsoft.com/en-us/microsoft-365-copilot/customize-how-microsoft-365-copilot-responds-to-you
- Anthropic Claude Projects: https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Anthropic Claude personalization: https://support.anthropic.com/en/articles/10185728-understanding-claude-s-personalization-features
- Canva Brand Voice: https://www.canva.com/help/brand-voice/
- GitHub Copilot custom instructions: https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/configure-custom-instructions/add-repository-instructions-in-your-ide
- Notion Agent instructions: https://www.notion.com/help/instructions-for-notion-agent
- Cursor Rules: https://cursor.com/docs/rules
- Midjourney Personalization: https://docs.midjourney.com/hc/en-us/articles/32433330574221-Personalization

**Pernyataan verifikasi:** hanya jalur di bagian “Mekanisme persisten yang terdokumentasi” di atas yang diklaim telah diverifikasi dengan dokumentasi resmi pada saat penyusunan. Untuk platform lain, isi tabel adalah rekomendasi integrasi generik, bukan klaim bahwa fitur/menu tersebut tersedia atau sudah disimpan.
