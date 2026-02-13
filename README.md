# Backstage Word Dokument Converter

Konverterer Word-dokumenter (.docx) til Backstage's visuelle identitet som HTML med A4-sider.

## Features

- Automatisk forside med titel, dokumenttype og beskrivelse
- Auto-genereret indholdsfortegnelse med sidetal
- Backstage fonte (FH Lecturis + Helvetica Neue)
- Backstage farver (#001270, #3e5cfe)
- Bullet points konverteret til pile (→)
- Highlight boxes for vigtige afsnit
- Tabeller med korrekt formatering
- Billeder fra Word inkluderet
- A4-sider med automatisk paginering
- Logo og sidetal i sidefod

## Installation

```bash
# Klon repository
git clone <repo-url>
cd word-dokument-converter

# Installer dependencies
pip install -r requirements.txt
```

## Brug

### Via Web-app (Streamlit)

```bash
streamlit run app.py
```

Åbn http://localhost:8501 i din browser.

### Via Python

```python
from docx import Document
from html_converter import convert_to_html

# Indlæs Word-dokument
doc = Document('dit-dokument.docx')

# Konverter til HTML
html = convert_to_html(
    doc,
    title="Dokumenttitel",
    cover_caption="RAPPORT",
    cover_description="En kort beskrivelse af dokumentet."
)

# Gem HTML
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html)
```

## Filer

| Fil | Beskrivelse |
|-----|-------------|
| `app.py` | Streamlit web-interface |
| `html_converter.py` | Konverteringslogik (Word → HTML) |
| `converter.py` | Word → Word formatering |
| `styles.py` | Backstage style-definitioner |
| `Fonts/` | FH Lecturis og Helvetica Neue fonte |
| `Backstage Logo/` | Logo-filer |

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

Hvis du har en `.doc` fil, kan du konvertere den til `.docx` på følgende måder:

1. **I Word:** Åbn filen → Gem som → Vælg "Word-dokument (.docx)"
2. **Via Google Drive:** Upload filen → Højreklik → "Åbn med" → Google Docs → Fil → Download → Microsoft Word (.docx)

## Krav

- Python 3.9+
- python-docx
- streamlit (for web-app)

---

*Backstage Word Converter v1.0*
