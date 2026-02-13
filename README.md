# Backstage Report Engine

Konverterer Word-dokumenter (.docx) til Backstage's visuelle identitet som HTML med A4-sider.

## Features

- Automatisk forside med titel, dokumenttype og beskrivelse
- Auto-genereret indholdsfortegnelse med sidetal
- Backstage fonte (FH Lecturis + Helvetica Neue)
- Backstage farver (#001270, #3e5cfe)
- Semantiske call-out boxes (Claude identificerer vigtige afsnit)
- Bullet points konverteret til pile (→)
- Tabeller med korrekt formatering
- Billeder fra Word inkluderet (base64 embedded)
- A4-sider med automatisk paginering
- Logo og sidetal i sidefod
- PDF-klar (skarp tekst og logo ved print-to-PDF)

## Installation

```bash
# Klon repository
git clone https://github.com/haettemaagen/Backstage-Report-Engine.git
cd Backstage-Report-Engine

# Installer dependencies
pip install -r requirements.txt
```

## Brug med Claude Code

**Nemmeste metode:** Åbn mappen i Claude Code. `CLAUDE.md` indeholder det fulde konverteringsflow.

1. Placer din `.docx` fil i projektmappen
2. Bed Claude konvertere den (se konverteringsflow i CLAUDE.md)
3. Output gemmes i `HTML Exports/` mappen
4. Åbn HTML-filen i en browser

## Brug via Python

```python
from docx import Document
from html_converter import convert_to_html

doc = Document('dit-dokument.docx')

html = convert_to_html(
    doc,
    title="Dokumenttitel",
    cover_caption="RAPPORT",
    cover_description="En kort beskrivelse af dokumentet.",
    cover_date="Februar 2026"
)

# VIGTIGT: Gem altid i HTML Exports/ mappen (fonts virker kun derfra)
with open("HTML Exports/output.html", "w", encoding="utf-8") as f:
    f.write(html)
```

## Mappestruktur

```
Backstage-Report-Engine/
├── html_converter.py      # Hovedfil - konverteringslogik
├── converter.py            # Word → Word formatering
├── styles.py               # Backstage style-definitioner
├── app.py                  # Streamlit web-interface
├── requirements.txt        # Python dependencies
├── CLAUDE.md               # Konverteringsflow og regler
├── README.md               # Denne fil
├── backstage-vi-guide.md   # Visuel identitet guide
├── Backstage Logo/         # Logo-filer (PNG + SVG)
├── Fonts/                  # FH Lecturis + Helvetica Neue
└── HTML Exports/           # ← Output-filer havner her
```

**VIGTIGT:** HTML-filer skal gemmes i `HTML Exports/` mappen. Font-stierne er relative (`../Fonts/`) og virker kun fra denne placering.

## Dokumenttyper (cover_caption)

| Type | Brug |
|------|------|
| `RAPPORT` | Analyser, evalueringer, undersøgelser |
| `ANALYSE` | Dybdegående analyse af specifikt emne |
| `NOTAT` | Kortere, interne dokumenter |
| `ANBEFALING` | Beslutningsoplæg, handlingsforslag |
| `ROADMAP` | Fremtidsplaner, strategier |

## Visuel Identitet

### Farver
- **Primary Blue:** #001270 (tekst, overskrifter)
- **Accent Blue:** #3e5cfe (pile, links, highlight borders)
- **Background Light:** #eef2ff (highlight boxes)

### Fonte
- **Overskrifter:** FH Lecturis
- **Brødtekst:** Helvetica Neue

## Filformat

**Vigtigt:** Konverteren understøtter kun `.docx` filer (ikke det gamle `.doc` format).

Hvis du har en `.doc` fil, konverter den først:
1. **I Word:** Åbn filen → Gem som → Vælg "Word-dokument (.docx)"
2. **Via Google Drive:** Upload → Åbn med Google Docs → Download som .docx

## Krav

- Python 3.9+
- python-docx
- streamlit (for web-app)

---

*Backstage Report Engine v26*
