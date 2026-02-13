# Projekt: Backstage Word Dokument Converter

## Formål
En web-app der konverterer Word-dokumenter til Backstage's visuelle identitet.

**Primært output:** HTML med A4-sider, auto-paginering, sidefod med logo+sidetal

**Sekundært output:** Word-til-Word formatering (via Streamlit app)

---

## 🚀 TL;DR - Hvad er dette projekt?

En Word-til-HTML konverter der:
1. Læser `.docx` filer med `python-docx`
2. Anvender Backstage's visuelle identitet (FH Lecturis fonte, blå farver)
3. **Claude analyserer indholdet semantisk** og identificerer vigtige afsnit → call-out boxes
4. Genererer A4-formateret HTML med auto-paginering via JavaScript
5. Inkluderer QC-funktion der sammenligner Word og HTML

**Nøglefil:** `html_converter.py` - indeholder al konverteringslogik (~2200 linjer)

---

## Status: CHECKPOINT 2026-02-13 (v27)

### Hvad er færdigt
- [x] Visuel identitet guide opdateret (`backstage-vi-guide.md`)
- [x] Python converter kode (`converter.py`, `styles.py`, `app.py`, `html_converter.py`)
- [x] Alle fonts tilgængelige i `fonts/` mappen
- [x] Logo i sidefod (ikke header)
- [x] Korrekt label-afstand (10px mellem tekst og streg)
- [x] Øget afstande mellem elementer (H2, H3, list items, highlight boxes, tabeller)
- [x] Billede-ekstraktion fra Word-dokumenter (base64 embedded)
- [x] Auto-genererede labels ved H1 kapitler (med intelligent mønstergenkendelse)
- [x] Tabeller placeres korrekt i dokumentrækkefølge (ikke i bunden)
- [x] PDF export fix: Logo som PNG (ikke SVG) for skarp print
- [x] PDF export fix: Sidetal med `text-stroke: 0` for at undgå pixelering
- [x] Logo størrelse: 17px højde
- [x] Sidetal størrelse: 9pt (Arial font for print-kompatibilitet)
- [x] **Caption-undtagelser** - Bilag, Ordliste, Appendix får INGEN label/caption
- [x] **Brødtekst formatering** - `format_long_text_block()` splitter ved blank lines, konverterer `## Header` til H4
- [x] **Side overflow fix** - maxContentHeight reduceret til 235mm for sikkerhedsmargin
- [x] **QC-funktion** - `quality_check()` og `print_qc_report()` sammenligner Word og HTML
- [x] **Bilag-formatering** - Source Code stil → `.code-block`, data-labels for "Datakilder:" etc.
- [x] **Hyperlink-support** - Links fra Word ekstraheres og formateres som `<a>` tags
- [x] **Element-splitting** - Tabeller, kodeblokke og highlight boxes splittes automatisk over flere sider (v12)
- [x] **splitCodeBlock() lineHeight fix (v13)** - Rettet beregning: lineHeight 12→16px + blockOverhead 64px
- [x] **Forbedret QC** - Ordantal-sammenligning mellem Word og HTML for at fange manglende tekst
- [x] **Instruction-section splitting (v14)** - Code blocks med `## headers` splittes til separate DOM elementer for bedre paginering
- [x] **Orphan prevention (v15)** - `preventOrphanedHeadings()` flytter "flyvende" overskrifter til næste side
- [x] **Forside-beskyttelse** - Første side røres aldrig af orphan prevention (titlen skal stå alene)
- [x] **Table minimum rows** - `MIN_ROWS_WITH_HEADER = 2` - tabeller splittes ikke hvis kun header + 0-1 rækker passer
- [x] **Subheading detection** - Korte paragraffer der ender med ":" behandles som heading-lignende elementer
- [x] **Automatisk indholdsfortegnelse (v16)** - TOC genereres automatisk fra H1/H2/H3 overskrifter
- [x] **Forbedret pagination (v16)** - Fixed edge case hvor overflowIndex=0 stoppede pagination
- [x] **Semantisk call-out analyse (v17)** - Claude identificerer call-outs baseret på betydning, ikke keywords
- [x] **callout_paragraphs parameter** - `convert_to_html()` accepterer nu liste af call-out tekster
- [x] **extract_paragraphs_for_analysis()** - Ny hjælpefunktion til at ekstrahere paragraffer for analyse
- [x] **Ingen konsekutive call-outs (v17)** - `_last_was_callout` forhindrer to highlight boxes i træk
- [x] **Forside design (v18)** - Automatisk genereret forside med titel, caption og beskrivelse
- [x] **LLM-genereret forside-indhold** - Claude analyserer dokument og genererer caption/beskrivelse
- [x] **cover_caption parameter** - Dokumenttype (RAPPORT, ANALYSE, NOTAT, etc.)
- [x] **cover_description parameter** - Kort beskrivelse til forsiden (maks ~200 tegn)
- [x] **Bagside fjernet (v19)** - Kun forside, ingen bagside
- [x] **TOC sidetal fix (v19)** - Ekskluderer cover-page fra sidetalsberegning
- [x] **Sidefod sidetal fix (v19)** - Samme fix for sidefod page numbers
- [x] **TOC matching fix (v19)** - Eksakt match først, derefter bedste match (længste fælles tekst)
- [x] **Heading søgning fix (v19)** - Kun i `.page-content` (ekskluderer logo i sidefod)
- [x] **Forside kvadrater fix (v20)** - Alle kvadrater samme størrelse (80x80px) og farve
- [x] **Zigzag-mønster (v20)** - 3 kvadrater i zigzag nederst til højre: højre-venstre-højre
- [x] **2 kvadrater øverst venstre (v20)** - Diagonal mønster i øverste venstre hjørne
- [x] **Større kvadrater (v21)** - 120x120px (op fra 80px), lavere opacity (0.10)
- [x] **Større logo (v21)** - 30px højde på forside (op fra 20px)
- [x] **GitHub-ready (v21)** - README.md, .gitignore, oprydning af test-filer
- [x] **Callout regel (v22)** - Bullet points/list items er ALDRIG callouts (de er allerede struktureret)
- [x] **Font-smoothing fix (v22)** - Tilføjet antialiasing til forside-tekster (løser pixelering på hvid tekst)
- [x] **Auto-skip Word TOC (v23)** - Manuel indholdsfortegnelse fra Word springes automatisk over
- [x] **cover_date parameter (v23)** - Valgfri dato vises til højre for logo på forsiden
- [x] **Smart H1 title matching (v23)** - Spring kun H1 over hvis den matcher titel-parameteren (ikke bare "første H1")
- [x] **Filformat dokumentation (v23)** - README opdateret: kun .docx understøttes, Google Drive konvertering beskrevet
- [x] **Backward compatibility verificeret (v24)** - Rapport CW TEST.docx fungerer korrekt med v23-ændringer
- [x] **FINAL output med dato (v24)** - `Rapport_CW_TEST_FINAL.html` inkluderer "Februar 2026" på forsiden
- [x] **Pseudo-heading detection (v25)** - `is_pseudo_heading()` auto-detekterer sektionsoverskrifter i ustrukturerede dokumenter
- [x] **Pseudo-heading patterns (v25)** - Genkender: "Tekst:", "How often...?", "Summary: ...", "Topic – Description:"
- [x] **Image extraction fix (v25)** - Billeder i title block-paragraffer inkluderes nu (før blev de sprunget over)
- [x] **Bike.docx stresstest (v25)** - Testet med ustruktureret dokument: 4 billeder, 4 pseudo-headings, 4 callouts
- [x] **PDF print fix (v26)** - Inline hvid SVG logo (ingen CSS filter), løser manglende logo i PDF
- [x] **rgba() farver (v26)** - Erstattet `opacity` med `rgba()` for cover-tekst, løser pixelering i PDF
- [x] **text-stroke: 0 (v26)** - Tilføjet til alle cover-elementer for skarp PDF-rendering
- [x] **fax-rapport stresstest (v26)** - Testet PDF print med korrekt logo og skarp tekst
- [x] **HTML Exports output-mappe (v27)** - HTML-filer gemmes i `HTML Exports/` med relative font-stier (`../Fonts/`)
- [x] **Font-stier fix (v27)** - Rettet `fonts/` → `../Fonts/` og logo `../Backstage Logo/` for korrekt visning fra undermappe
- [x] **GitHub repo (v27)** - Offentligt repo: `haettemaagen/Backstage-Report-Engine`
- [x] **Mappestruktur oprydning (v27)** - Test-filer i `File Exports/`, output i `HTML Exports/`, kun kode i rod
- [x] **Engelsk stresstest (v27)** - `fax-report-english.docx` oprettet og konverteret med engelsk indhold
- [x] **Nina PhD thesis stresstest (v27)** - 519 paragraffer, 76 billeder, 12 tabeller - konverteret succesfuldt
- [x] **README.md opdateret (v27)** - Mappestruktur, klon-URL, output-instruktioner, Claude Code workflow

### Kendte issues (til senere)
- [x] **Indholdsfortegnelse** - Implementeret! Auto-genereret fra dokumentets overskrifter (ikke fra Word TOC)
- [x] **Tal-læsbarhed i overskrifter** - Løst med `format_heading_numbers()` - 1x tyndt mellemrum FØR punktum (ens for alle tal)
- [ ] **Callout max-længde** - Overvej max ~500 tegn grænse (forhindrer alt for lange highlight boxes)
- [ ] **Billede-ekstraktion i store docs** - Nina thesis: kun 14/76 billeder ekstraheret (forbedring nødvendig)

### Næste skridt
- [ ] Test web-appen med `streamlit run app.py`
- [ ] Deploy til intern server
- [ ] Implementér callout max-længde regel (~500 tegn)

---

## Projektfiler

### Konfiguration & Dokumentation
| Fil | Beskrivelse |
|-----|-------------|
| `CLAUDE.md` | Denne fil - projekt checkpoint |
| `backstage-vi-guide.md` | **Master** visuel identitet guide |

### Konverteringsmotor
| Fil | Beskrivelse |
|-----|-------------|
| `html_converter.py` | **HOVEDFIL** - Word→HTML konvertering (~2200 linjer) |
| `converter.py` | Word→Word konvertering (sekundær) |
| `styles.py` | Backstage style-definitioner |

### Web-app
| Fil | Beskrivelse |
|-----|-------------|
| `app.py` | Streamlit web-interface |
| `requirements.txt` | Python dependencies |

### Test & Preview
| Fil | Beskrivelse |
|-----|-------------|
| `Rapport CW TEST.docx` | **Hoved test-dokument** (Word input) |
| `backstage-preview with editor.html` | Interaktiv style editor (hvis tilgængelig) |

### Assets
| Fil | Beskrivelse |
|-----|-------------|
| `Backstage Logo SVG - Dark On White.svg` | Logo |
| `fonts/FHLecturis_BSCustom_*.otf` | FH Lecturis fonte |
| `fonts/HelveticaNeue/*.ttf` | Helvetica Neue fonte |

---

## Sådan kører du appen

```bash
# 1. Gå til projektmappen
cd "Word Dokument Converter Projekt"

# 2. Installer dependencies
pip install -r requirements.txt

# 3. Start web-appen
streamlit run app.py

# 4. Åbn i browser
# http://localhost:8501
```

---

## ⚠️ VIGTIG FILOSOFI: Ekstraher kun det du finder

**Alle parametre er VALGFRIE.** Konverteren virker med kun `title`.

| Parameter | Påkrævet? | Hvis ikke fundet i Word... |
|-----------|-----------|---------------------------|
| `title` | Ja | Brug filnavn eller første H1 |
| `cover_caption` | Nej | Default: "RAPPORT" |
| `cover_description` | Nej | Vises ikke på forsiden |
| `cover_date` | Nej | Vises ikke på forsiden |
| `callout_paragraphs` | Nej | Kun keyword-matching bruges |

**Reglen:** Ekstraher kun det du faktisk kan finde i dokumentet. **Gæt ikke.**

**Minimalt kald der altid virker:**
```python
html = convert_to_html(doc, title="Dokumenttitel")
```

**Med alt metadata (kun hvis det findes):**
```python
html = convert_to_html(
    doc,
    title="...",                    # Påkrævet
    cover_caption="RAPPORT",        # Valgfrit
    cover_description="...",        # Valgfrit - kun hvis intro-tekst findes
    cover_date="Februar 2026",      # Valgfrit - kun hvis dato findes
    callout_paragraphs=[...]        # Valgfrit
)
```

---

## 🔄 KONVERTERINGSFLOW (til Claude)

Når en bruger beder dig konvertere et Word-dokument, følg dette flow:

### Trin 1: Læs dokumentet
```python
from docx import Document
from html_converter import extract_paragraphs_for_analysis, convert_to_html

doc = Document("brugerens-dokument.docx")
paragraphs = extract_paragraphs_for_analysis(doc)
```

### Trin 2: Semantisk analyse af call-outs
Gennemgå alle paragraffer og identificer dem der bør være **call-out boxes** (highlight boxes).

**Call-out kategorier:**

| Kategori | Beskrivelse | Eksempler |
|----------|-------------|-----------|
| ⚠️ Vigtig info | Advarsler, forbehold, kritiske pointer | "Det er afgørende at...", "Bemærk at..." |
| 📊 Konklusioner | Opsummeringer, hovedpointer, bundlinjen | "Samlet set viser...", "Den overordnede konklusion..." |
| 💡 Anbefalinger | Næste skridt, forslag, handlingsplaner | "Vi anbefaler at...", "Som næste skridt bør..." |
| 🎯 Nøgleindsigter | Centrale findings, overraskende resultater | "Et centralt fund er...", "Særligt bemærkelsesværdigt..." |

**Regler for call-outs:**
- Minimum 80 tegn (ikke korte sætninger)
- Skal have substantielt indhold (ikke bare en overskrift)
- Skal være en selvstændig pointe (ikke midt i et argument)
- Overskrifter (H1, H2, H3) er ALDRIG call-outs
- **INGEN konsekutive call-outs** - Hvis én paragraf er call-out, kan den næste IKKE være det (automatisk håndhævet af koden)

### Trin 3: Lav liste af call-out tekster
```python
callout_paragraphs = [
    "Samlet set viser evalueringen at...",  # Konklusion
    "Det er vigtigt at bemærke at...",       # Vigtig info
    "Vi anbefaler at organisationen...",     # Anbefaling
]
```

### Trin 4: Forside-analyse (ekstraher KUN hvis det findes)
Kig efter metadata i dokumentets første paragraffer. **Kun inkluder det du finder:**

**Dokumenttype (cover_caption) - VALGFRIT:**
| Type | Bruges når... |
|------|---------------|
| `RAPPORT` | Analyser, evalueringer, undersøgelser (default) |
| `ANALYSE` | Dybdegående analyse af et specifikt emne |
| `NOTAT` | Kortere, interne dokumenter |
| `ANBEFALING` | Beslutningsoplæg, handlingsforslag |
| `ROADMAP` | Fremtidsplaner, strategier |

**Beskrivelse (cover_description) - VALGFRIT:**
- Kun hvis dokumentet har intro-tekst/undertitel
- 1-2 sætninger, maks ~200 tegn
- Hvis ikke fundet → udelad parameteren

**Dato (cover_date) - VALGFRIT:**
- Kun hvis dokumentet har en dato (f.eks. "Februar 2026", "Dato: Januar 2025")
- Vises til højre for logoet på forsiden
- Hvis ikke fundet → udelad parameteren

### Trin 5: Kør konverteringen
```python
# MINIMALT (altid påkrævet):
html_output = convert_to_html(doc, title="Dokumenttitel")

# MED METADATA (kun hvis fundet i dokumentet):
html_output = convert_to_html(
    doc,
    title="Dokumenttitel",                    # Påkrævet
    callout_paragraphs=callout_paragraphs,   # Valgfrit
    cover_caption="RAPPORT",                  # Valgfrit (default: RAPPORT)
    cover_description="Kort beskrivelse...", # Valgfrit (kun hvis fundet)
    cover_date="Februar 2026"                 # Valgfrit (kun hvis fundet)
)

# VIGTIGT: Gem ALTID i HTML Exports/ mappen (fonts virker kun derfra)
with open("HTML Exports/output_backstage.html", "w", encoding="utf-8") as f:
    f.write(html_output)
```

### Trin 6: QC-tjek
```python
from html_converter import quality_check, print_qc_report

report = quality_check(doc, html_output)
print_qc_report(report)
```

---

## Call-out eksempler (til semantisk genkendelse)

**SKAL være call-out:**
```
"Samlet set viser evalueringen, at Claude-modellerne leverer markant bedre
resultater end GPT-4 på tværs af alle fire evalueringskriterier. Den gennemsnitlige
score for Claude er 4.2 sammenlignet med GPT-4's 3.1."
```
→ Konklusion med konkrete tal og sammenligning

**SKAL være call-out:**
```
"Det er afgørende at bemærke, at disse resultater er baseret på et begrænset
datasæt og bør valideres med yderligere tests før implementering i produktion."
```
→ Vigtig begrænsning/forbehold

**SKAL IKKE være call-out:**
```
"I det følgende afsnit gennemgår vi metodikken."
```
→ For kort, ingen substantiel pointe

**SKAL IKKE være call-out:**
```
"Tabel 3 viser resultaterne."
```
→ Bare en reference, ikke en indsigt

---

## Beslutninger taget

| Beslutning | Valg |
|------------|------|
| Output format | Word-til-Word (ikke HTML) |
| Interface | Streamlit web-app |
| Hosting | Intern server hos Backstage |
| Logo placering | Sidefod (nederst venstre) |
| Sidetal | Nederst højre |
| Highlight boxes | Auto-genkendelse af "Vigtig:", "Konklusion:" etc. |
| Bullet points | Pile (→) i accent blue |
| Label afstand | 10px mellem tekst og blå streg |
| Element-afstande | H2: 36/18px, H3: 28/14px, list: 12px, boxes/tables: 24px |
| Billeder | Ekstraheres fra Word, embedded som base64, centreret |
| Labels ved kapitler | Auto-genereres fra H1-titel med mønstergenkendelse |
| Tabel-placering | I dokumentrækkefølge via `iter_block_items()` |
| Logo format (sidefod) | PNG - bedre print-kvalitet |
| Logo format (forside) | Inline SVG med `fill="white"` - virker i PDF print |
| Logo størrelse | 17px (sidefod), 25px (forside) |
| Sidetal font | Arial 9pt (system font for konsistent PDF) |
| Sidetal styling | `text-stroke: 0` for at undgå pixelering |
| PDF print forside | `rgba()` farver (ikke `opacity`), inline SVG, `text-stroke: 0` |
| **Output-mappe** | **`HTML Exports/`** — HTML-filer SKAL gemmes her (font-stier er relative: `../Fonts/`) |
| Tal-kerning i overskrifter | Tyndt mellemrum FØR punktum (3x ved "1", 1x ved andre) - KUN H1, H2, H3 (IKKE TOC) |
| Indholdsfortegnelse | **Auto-genereret** fra H1/H2/H3, egen side (side 2), INGEN caption/label, border-bottom på hver entry, auto-sidetal via JS |
| Caption-undtagelser | Bilag, Ordliste, Appendix, Glossar, Litteratur, Referencer får INGEN label |
| Lange tekstblokke | Split ved `\n\n`, markdown `## Header` → `<h4 class="instruction-header">` |
| Sidehøjde (overflow fix) | maxContentHeight = 235mm (ned fra 242mm) for sikkerhedsmargin |
| QC-funktion | Sammenligner H1/H2/H3/tabeller/billeder mellem Word og HTML |
| Call-out identifikation | **Semantisk via Claude** + keyword-matching som fallback |
| Call-out regel | Ingen konsekutive call-outs (automatisk håndhævet) |
| **Forside (v18)** | Mørkeblå baggrund, caption + titel + beskrivelse + logo |
| **Bagside (v19)** | FJERNET - kun forside bruges nu |
| Forside sidefod | INGEN sidefod (forsiden har sit eget design) |
| **TOC sidetal (v19)** | Ekskluderer cover-page, eksakt match først |
| Dekorative firkanter | CSS pseudo-elementer + div'er med rgba() farver |
| Cover logo | Hvid (inverteret via CSS filter) |
| Cover titel | FH Lecturis, 48pt, hvid, max 80% bredde |
| Cover beskrivelse | Helvetica 14pt, hvid, 90% opacity, max 70% bredde |

---

## Backstage Visuel Identitet (quick reference)

### Farver
| Navn | Hex | Brug |
|------|-----|------|
| Primary Blue | `#001270` | Al tekst, overskrifter |
| Accent Blue | `#3e5cfe` | Labels, pile, highlight borders |
| Background Light | `#eef2ff` | Highlight box baggrund |

### Fonte
| Element | Font | Vægt | Størrelse |
|---------|------|------|-----------|
| H1 | FH Lecturis | 400 | 32pt |
| H2 | FH Lecturis | 400 | 20pt |
| H3 | FH Lecturis | 400 | 14pt |
| Body | Helvetica Neue | 300 | 10pt |
| Label | Helvetica Neue | 500 | 9pt, UPPERCASE |

### Font-filer
```
fonts/
├── FHLecturis_BSCustom_Regular.otf
├── FHLecturis_BSCustom_Bold.otf
├── FHLecturis_BSCustom_Light.otf
└── HelveticaNeue/
    ├── HelveticaNeue-Light-08.ttf      (300)
    ├── HelveticaNeue-Medium-11.ttf     (500)
    ├── HelveticaNeue-01.ttf            (400)
    └── HelveticaNeue-Bold-02.ttf       (700)
```

---

## Noter til Claude

- `backstage-vi-guide.md` er master-dokumentet for visuel identitet
- Logo skal være i sidefoden, ikke i headeren
- Brug lokale font-referencer (ikke base64) i HTML previews
- **Highlight boxes:** Identificeres semantisk af Claude (se konverteringsflow ovenfor)
- **Keyword fallback:** "Vigtig:", "Konklusion:", "Bemærk:", "Anbefaling:" etc. virker stadig automatisk
- **Test-fil:** `Rapport CW TEST.docx` bruges til at teste konverteringen
- **Output:** Test-filer genereres ved kørsel (ignoreret af .gitignore)

---

---

## Samtale-checkpoint: 6. februar 2025 (session 20) - v25

### Hvad vi lavede i denne session
1. **Pseudo-heading detection** - Auto-detekterer sektionsoverskrifter i ustrukturerede dokumenter

**Nye funktioner:**
```python
def is_pseudo_heading(text: str) -> bool:
    """Genkender pseudo-headings baseret på mønstre:
    - Ender med ":" og er kort (<80 tegn)
    - Starter med spørgeord og ender med "?"
    - Indeholder "–" separator
    - Starter med "Summary:", "Note:", etc.
    """
```

**CSS styling:**
```css
h3.pseudo-heading {
  font-family: 'Helvetica Neue';
  font-weight: 500;
  font-size: 12pt;
  border-bottom: 1px solid #eef2ff;
}
```

2. **Image extraction fix** - Billeder i title block inkluderes nu

**Problemet:**
- Bike.docx havde billede i paragraf 0 (samme som titel)
- `continue` statement sprang HELE paragraffen over inkl. billede

**Løsningen:**
```python
if not seen_first_content_h1 and style_type == 'p':
    if len(text) < 150 or is_title_block_metadata(text):
        # VIGTIGT: Tjek for billede FØR vi springer teksten over
        image_html = get_paragraph_image(para, images)
        if image_html:
            html_parts.append(image_html)
        continue  # Spring kun TEKSTEN over, ikke billedet
```

3. **Bike.docx stresstest** - Testet med ustruktureret dokument

**Resultat:**
- 4/4 billeder ✓
- 4 pseudo-headings auto-detekteret ✓
- 4 semantiske callouts ✓
- Rapport CW TEST.docx uændret ✓

### Filer ændret
- `html_converter.py` - `is_pseudo_heading()`, image extraction fix, CSS
- `CLAUDE.md` - Checkpoint (v25)

### Test-filer
- `Bike_backstage.html` - Stresstest output
- `Rapport_CW_TEST_FINAL.html` - Primær test (uændret)

---

## Samtale-checkpoint: 6. februar 2025 (session 19) - v24

### Hvad vi lavede i denne session
1. **Backward compatibility test** - Verificerede at v23-ændringer fungerer med originalt test-dokument

**Test:**
- Kørte konvertering på `Rapport CW TEST.docx` med v23-koden
- QC passerede: H1 9/9, H2 31/31, H3 15/15, Tabeller 21/21, Billeder 2/2
- Ingen kritiske issues

**Læring:**
- Når `title` parameter matcher første H1 i Word → H1 springes korrekt over
- Forkert `title` parameter → H1 inkluderes (forårsagede blank side + duplikat titel)
- **Regel:** `title` skal matche dokumentets faktiske titel-H1

2. **Dato tilføjet til FINAL output** - "Februar 2026" på forsiden

**Kommando:**
```python
html = convert_to_html(
    doc,
    title="Evaluering af NLQ-teknologi for AKA",
    cover_date="Februar 2026"  # NY
)
```

### Filer ændret
- `CLAUDE.md` - Checkpoint (v24)

### Output
- `Rapport_CW_TEST_FINAL.html` - Komplet output med dato på forsiden
- `fax-rapport_backstage.html` - Sekundær test-fil

---

## Samtale-checkpoint: 6. februar 2025 (session 18) - v23

### Hvad vi lavede i denne session
1. **Auto-skip Word TOC** - Manuel indholdsfortegnelse fra Word springes automatisk over

**Problemet:**
- fax-rapport.docx havde en manuel TOC i starten
- Vores konverter genererer også en TOC automatisk
- Resultat: To indholdsfortegnelser!

**Løsningen:**
```python
def is_manual_toc_entry(text: str) -> bool:
    """Matcher: 'Resumé — 3', '1.1 Noget — 4'"""
    if re.search(r'\s*[—–-]{1,2}\s*\d{1,3}\s*$', text):
        return True

def is_manual_toc_heading(text: str) -> bool:
    """Matcher: 'Indholdsfortegnelse', 'Table of Contents'"""
    toc_headings = ['indholdsfortegnelse', 'indhold', 'table of contents']
    return text.lower().strip() in toc_headings
```

2. **cover_date parameter** - Dato på forsiden

**Ny parameter:**
```python
html = convert_to_html(doc, title="...", cover_date="Februar 2026")
```

**Design:** Dato vises til højre for logoet i forsidebunden (flexbox).

3. **Smart H1 title matching** - Spring kun H1 over hvis den matcher titel

**Problemet:**
- Før: Spring altid første H1 over (antog det var titlen)
- fax-rapport: Første H1 var "Indholdsfortegnelse", ikke titlen
- "Resumé" blev fejlagtigt sprunget over

**Løsningen:**
```python
# Før: if h1_count == 1: continue
# Nu: if text.lower()[:30] == title.lower()[:30]: continue
```

4. **Filosofi-sektion** - "Ekstraher kun det du finder"

- Alle parametre er valgfrie (undtagen title)
- Dokumenteret tydeligt i CLAUDE.md
- Sikrer konverteren virker med alle Word-dokumenter

### Filer ændret
- `html_converter.py` - TOC-skip, cover_date, smart H1 matching, cover-footer CSS
- `README.md` - Filformat dokumentation (.docx krav)
- `CLAUDE.md` - Filosofi-sektion, opdateret konverteringsflow, checkpoint (v23)

---

## Samtale-checkpoint: 6. februar 2025 (session 17) - v22

### Hvad vi lavede i denne session
1. **Callout regel præciseret** - Bullet points skal aldrig være callouts

**Problemet:**
- Side 5 havde 3 callout boxes der visuelt så ud som bullet points i Word
- Disse var del af en sammenhængende liste, men blev til separate highlight boxes

**Løsningen:**
- Fjernede bullet point tekster fra `callout_paragraphs` listen
- Reduceret fra 10 → 6 callouts
- **Ny regel:** Bullet points / list items er ALDRIG callouts

2. **Font-smoothing fix** - Løste pixeleret tekst på forsiden

**Problemet:**
- Hvid tekst på mørk baggrund så fuzzy/pixeleret ud
- Standard subpixel antialiasing virker dårligt på lys-på-mørk

**Løsningen:**
```css
-webkit-font-smoothing: antialiased;
-moz-osx-font-smoothing: grayscale;
text-rendering: optimizeLegibility;
```

Tilføjet til:
- `.cover-caption`
- `.cover-title`
- `.cover-description`

### Filer ændret
- `html_converter.py` - Font-smoothing på forside-elementer
- `CLAUDE.md` - Checkpoint (v22)

### Callout regler (opdateret)
| Kategori | Skal være callout? |
|----------|-------------------|
| Konklusioner, opsummeringer | ✅ Ja |
| Vigtige advarsler, forbehold | ✅ Ja |
| Anbefalinger, næste skridt | ✅ Ja |
| Nøgleindsigter, overraskende fund | ✅ Ja |
| **Bullet points / list items** | ❌ **NEJ** |
| Korte sætninger (<80 tegn) | ❌ Nej |
| Overskrifter (H1, H2, H3) | ❌ Nej |

---

## Samtale-checkpoint: 5. februar 2025 (session 16)

### Hvad vi lavede i denne session
1. **Større dekorative kvadrater (v21)** - 50% større for bedre visuel effekt

**Ændringer:**
- Kvadrat-størrelse: 80×80px → 120×120px (+50%)
- Opacity: 0.15 → 0.10 (mere subtil)
- Logo på forside: 20px → 30px (+50%)
- Positioner opdateret tilsvarende (120, 240, 360)

2. **GitHub-forberedelse** - Projektet er nu klar til deling

**Oprettet:**
- `README.md` - Brugervejledning til kollegaer
- `.gitignore` - Ignorerer test-filer, __pycache__, .DS_Store, .claude/

**Slettet:**
- Alle `Rapport_CW_TEST_*.html` test-filer
- `Rapport CW TEST_backstage.docx` output-fil

### Filer ændret
- `html_converter.py` - Større kvadrater og logo
- `README.md` - NY: Brugervejledning
- `.gitignore` - NY: Ignorer test-output
- `CLAUDE.md` - Checkpoint (v21 FINAL)

### Status: KLAR TIL GITHUB

---

## Samtale-checkpoint: 5. februar 2025 (session 15)

### Hvad vi lavede i denne session
1. **Forside kvadrater fix (v20)** - Alle dekorative kvadrater har nu korrekt design

**Ændringer:**
- Alle 5 kvadrater har samme farve: `rgba(62, 92, 254, 0.2)`
- Alle kvadrater er 80x80px
- Øverst venstre: 2 kvadrater i diagonal (via `::before` og `::after`)
- Nederst højre: 3 kvadrater i **zigzag-mønster**:
  ```
       [1]    ← right: 0 (højre kant)
    [2]       ← right: 80 (forskudt venstre)
       [3]    ← right: 0 (hjørne)
  ```

**CSS positioner (nederst højre):**
- deco-1: `bottom: 160px; right: 0;`
- deco-2: `bottom: 80px; right: 80px;`
- deco-3: `bottom: 0; right: 0;`

### Filer ændret
- `html_converter.py` - Opdateret CSS for zigzag-mønster
- `CLAUDE.md` - Checkpoint (v20)

### Output
- `Rapport_CW_TEST_v19_zigzag.html` - Test-fil med korrekt forside-design

---

## Samtale-checkpoint: 5. februar 2025 (session 14)

### Hvad vi lavede i denne session
1. **Bagside fjernet (v19)** - Kun forside, ingen bagside

**Ændring:**
- `generate_back_page()` kaldes ikke længere
- Dokumentet slutter efter sidste indholdsside

2. **TOC sidetal fix (v19)** - Korrekt sidetalsberegning

**Problemet:**
- TOC-sidetal inkluderede forsiden i tællingen
- "Bilag G" viste side 34 i stedet for side 53
- Alle "Bilag X" entries viste samme sidetal (34)

**Løsningen:**
```javascript
// Ekskluder cover-page fra sidetalsberegning
const contentPages = document.querySelectorAll('.page:not(.cover-page):not(.back-page)');

// Eksakt match først, derefter bedste match (længste fælles tekst)
if (headingPageMap.has(entryText)) {
  pageNumber = headingPageMap.get(entryText);
} else {
  // Find bedste match baseret på længste fælles tekst
}
```

3. **Sidefod sidetal fix (v19)** - Samme fix for sidefod page numbers

4. **Heading søgning fix (v19)** - Kun i `.page-content`
- Ekskluderer "Backstage" logoet fra at blive opfattet som overskrift
- Forhindrer falske TOC-entries

### Filer ændret
- `html_converter.py` - Fjernet back page, rettet TOC/sidefod sidetalslogik
- `CLAUDE.md` - Checkpoint (v19)

### Output
- `Rapport_CW_TEST_v19_final.html` - Test-fil med korrekte TOC-sidetal

---

## Samtale-checkpoint: 5. februar 2025 (session 13)

### Hvad vi lavede i denne session
1. **Automatisk forside og bagside (v18)** - Design baseret på Figma mockup

**Design elementer:**
- Mørkeblå baggrund (#001270)
- Dekorative firkanter (lysere blå, øverst venstre + nederst højre)
- Caption (dokumenttype, uppercase)
- Hvid streg under caption
- Titel (FH Lecturis, 48pt, hvid)
- Beskrivelse (Helvetica 14pt, hvid) - KUN på forside
- Backstage logo (hvid, inverteret) nederst venstre

**Struktur:**
```
Side 0: FORSIDE (cover-page)
Side 1: Indholdsfortegnelse
Side 2+: Dokumentindhold
Sidste side: BAGSIDE (back-page)
```

2. **Nye parametre i `convert_to_html()`:**
```python
html = convert_to_html(
    doc,
    title="...",
    callout_paragraphs=[...],
    cover_caption="RAPPORT",           # NYT: Dokumenttype
    cover_description="Kort beskrivelse..."  # NYT: LLM-genereret
)
```

3. **Nye funktioner:**
- `generate_cover_page(title, caption, description)` - Genererer forside HTML
- `generate_back_page(title, caption)` - Genererer bagside HTML
- `get_html_header_no_page(title)` - Header uden automatisk page åbning

4. **JavaScript opdateret:**
- Pagination ignorerer nu `.cover-page` og `.back-page`
- Nye sider indsættes før bagsiden
- Sidetal beregnes kun for indholdsider (ikke forside/bagside)

### Filer ændret
- `html_converter.py` - CSS for cover/back pages, nye funktioner, opdateret JS
- `CLAUDE.md` - Forside-flow, nye parametre, checkpoint (v18)

### Output
- `Rapport_CW_TEST_v18_cover.html` - Test-fil med forside og bagside

---

## Samtale-checkpoint: 13. februar 2026 (session 14) - v27

### Hvad vi lavede i denne session
1. **PDF print fix (v26)** - Færdiggjort fra forrige session
   - Inline hvid SVG logo (alle paths `fill="white"`) i stedet for CSS filter
   - `rgba()` farver i stedet for `opacity` (løser pixelering i PDF)
   - `text-stroke: 0` + `print-color-adjust: exact` på alle cover-elementer

2. **Engelsk stresstest** - Oprettet `fax-report-english.docx` fra bunden med fuld oversættelse
   - Konverteret til Backstage HTML med 7 tabeller, 4 callouts
   - Verifikation: Converteren håndterer engelsk indhold fint

3. **Nina PhD thesis stresstest** - Stor akademisk afhandling (4.3 MB)
   - 519 paragraffer, 76 billeder, 12 tabeller
   - Resultat: 14/76 billeder ekstraheret (billedekstraktion skal forbedres)
   - Tekst og tabeller konverteret korrekt (19,702 ord bevaret)

4. **Mappestruktur oprydning**
   - Oprettet `File Exports/` til test-dokumenter (docx, pdf)
   - Oprettet `HTML Exports/` til genererede HTML-filer
   - Font-stier ændret: `fonts/` → `../Fonts/` (virker fra undermappe)
   - Logo-sti ændret: `../Backstage Logo/`

5. **GitHub repo oprettet**
   - Public repo: https://github.com/haettemaagen/Backstage-Report-Engine
   - `.gitignore` ekskluderer: `File Exports/`, `HTML Exports/`, `*.docx`, `*.html`, `*.pdf`
   - Kun kode, fonts, logo og dokumentation deles
   - `test_converter.py` slettet (ikke nødvendig i repo)

6. **README.md opdateret** - Mappestruktur, klon-URL, Claude Code workflow

### Filer ændret
- `html_converter.py` - Inline SVG, rgba farver, font-stier, logo-sti
- `CLAUDE.md` - v27 checkpoint, output-mappe regler, beslutninger
- `README.md` - Ny version med mappestruktur og GitHub URL
- `.gitignore` - Tilføjet `File Exports/`, `HTML Exports/`

### Beslutninger taget
| Beslutning | Valg |
|------------|------|
| Output-mappe | `HTML Exports/` (fonts virker via `../Fonts/`) |
| GitHub visibility | Public repo |
| Font-stier | Relative fra undermappe (`../Fonts/`, `../Backstage Logo/`) |
| Callout max-længde | ~500 tegn anbefalet (ikke implementeret endnu) |

---

## Samtale-checkpoint: 6. februar 2025 (session 13)

### Hvad vi lavede i denne session
1. **PDF print fix (v26)** - Løste problemer med print-to-PDF fra browser

**Problem 1: Logo forsvandt i PDF**
- CSS `filter: brightness(0) invert(1)` virker ikke i browser print-to-PDF
- Løsning: Inline hvid SVG logo direkte i HTML (alle paths med `fill="white"`)

**Problem 2: Tekst pixeleret i PDF**
- `opacity: 0.9` og `opacity: 0.7` på cover-tekst gav pixelering
- Løsning: Erstattet med `rgba(255, 255, 255, 0.9)` og `rgba(255, 255, 255, 0.7)`

**Problem 3: Generel PDF-skarphed**
- Tilføjet `text-stroke: 0` og `print-color-adjust: exact` til alle cover-elementer

**Ændrede CSS klasser:**
```css
.cover-title, .cover-caption, .cover-description, .cover-date {
  -webkit-text-stroke: 0;
  text-stroke: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.cover-description { color: rgba(255, 255, 255, 0.9); }
.cover-date { color: rgba(255, 255, 255, 0.7); }

.cover-logo svg { height: 25px; width: auto; }  /* Inline SVG */
```

### Filer ændret
- `html_converter.py` - Inline SVG logo, rgba farver, text-stroke fix
- `CLAUDE.md` - Checkpoint (v26)
- `fax-rapport_backstage.html` - Regenereret med PDF fix

---

## Samtale-checkpoint: 5. februar 2025 (session 12)

### Hvad vi lavede i denne session
1. **Semantisk call-out analyse (v17)** - Claude identificerer call-outs via semantisk forståelse

**Problemet:**
- Tidligere: Kun keyword-matching ("Vigtig:", "Konklusion:", etc.)
- Mange vigtige pointer blev overset fordi de ikke startede med de "rigtige" ord

**Løsningen:**
- `callout_paragraphs` parameter til `convert_to_html()`
- Claude læser dokumentet, identificerer call-outs semantisk
- Matcher via substring-søgning (fleksibel matching)

**Nye funktioner i html_converter.py:**
```python
# Ekstraher paragraffer til analyse
paragraphs = extract_paragraphs_for_analysis(doc)

# Konverter med semantiske call-outs
html = convert_to_html(doc, title="...", callout_paragraphs=["tekst1", "tekst2"])
```

**Call-out kategorier:**
- ⚠️ Vigtig info (advarsler, forbehold)
- 📊 Konklusioner (opsummeringer, hovedpointer)
- 💡 Anbefalinger (næste skridt, forslag)
- 🎯 Nøgleindsigter (centrale findings)

2. **Ingen konsekutive call-outs regel** - Forhindrer at to call-outs står lige efter hinanden

**Problemet:**
- Kapitel 1 havde kun call-out boxes - ingen normal tekst
- Effekten forsvinder hvis alt er fremhævet

**Løsningen:**
- Global variabel `_last_was_callout` tracker forrige element
- Hvis forrige var callout → denne bliver normal paragraf
- Callout → Normal → Callout = OK
- Callout → Callout = Blokeret (anden bliver normal)

### Filer ændret
- `html_converter.py` - Ny `extract_paragraphs_for_analysis()`, opdateret `is_highlight_box()`, `callout_paragraphs` parameter, `_last_was_callout` logik
- `CLAUDE.md` - Konverteringsflow, call-out eksempler, no-consecutive regel, checkpoint (v17)

---

## Samtale-checkpoint: 5. februar 2025 (session 11)

### Hvad vi lavede i denne session
1. **Automatisk indholdsfortegnelse (v16)** - TOC genereres nu automatisk

**Problemet:**
- Word-dokumentet havde ingen TOC (indholdsfortegnelse)
- Tidligere kode understøttede kun TOC hvis Word-filen allerede HAD en

**Løsningen:**
```python
def collect_headings_for_toc(doc: Document) -> list:
    """Saml alle H1/H2/H3 overskrifter (undtagen titlen)"""
    # Skip første H1 (det er titlen)
    # Returner liste af (niveau, tekst) tuples

def generate_toc_html(entries: list) -> str:
    """Generer TOC HTML med korrekt styling"""
```

**Placering:** TOC indsættes automatisk på side 2 (efter titlen, før kapitel 1)

2. **Pagination bug fix** - `overflowIndex === 0` håndteres nu korrekt
   - Tidligere stoppede pagination hvis første element var for stort
   - Nu: prøv at splitte elementet, eller flyt resten til næste side

### Filer ændret
- `html_converter.py` - Nye funktioner: `collect_headings_for_toc()`, `generate_toc_html()`
- `CLAUDE.md` - Checkpoint (v16)

---

## Samtale-checkpoint: 5. februar 2025 (session 10)

### Hvad vi lavede i denne session
1. **Orphan prevention (v15)** - Flyvende overskrifter flyttes til næste side

**Problemet:**
- Overskrifter som "Bilag E" stod alene nederst på en side med ~50% tom plads under
- Indholdet der hørte til overskriften var på næste side

**Løsningen:**
```javascript
function preventOrphanedHeadings() {
  // Find sidste non-heading element (faktisk indhold)
  // Hvis siden ender med headings + >100px tom plads → flyt til næste side
  // REGEL: Første side (forsiden) røres ALDRIG
  for (let i = 1; i < pages.length; i++) { // Start fra side 2
    // ...
  }
}
```

2. **Table minimum rows** - Tabeller splittes ikke med kun header + 0-1 rækker
```javascript
const MIN_ROWS_WITH_HEADER = 2;
if (splitIndex < MIN_ROWS_WITH_HEADER || splitIndex >= bodyRows.length) return false;
```

3. **Subheading detection** - Korte paragraffer med ":" er heading-lignende
```javascript
if (tagName === 'P') {
  const text = element.textContent.trim();
  if (text.endsWith(':') && text.length < 80) {
    return true; // Behandles som heading
  }
}
```

4. **Tal-formatering fix** - Kun 1x tyndt mellemrum (ikke 3x for "1")

### Filer ændret
- `html_converter.py` - Orphan prevention, table min rows, subheading detection
- `CLAUDE.md` - Checkpoint (v15)

---

## Samtale-checkpoint: 5. februar 2025 (session 9)

### Hvad vi lavede i denne session
1. **Instruction-section splitting (v14)** - Løste paginerings-problemer med lange code blocks

**Problemet:**
- Lange instruktionssæt (code blocks med `## headers`) blev renderet som ét stort DOM element
- JavaScript-baseret splitting var upræcis pga. wrapped lines vs. `\n` linjer
- Dense paragraffer med få linjeskift men meget tekst beregnedes forkert

**Løsningen (Option 1 - Python-side splitting):**
I stedet for at splitte i JavaScript, splitter vi nu i Python-converteren ved `## headers`:

```python
def format_instruction_set(text: str) -> str:
    """Splitter ved ## headers så hver sektion bliver et selvstændigt DOM element."""
    sections = re.split(r'(?=^## |\n## )', text.strip())
    # Hver sektion → <div class="instruction-section instruction-first/middle/last">
```

**Nye CSS klasser:**
- `.instruction-section` - Basis styling med blå baggrund og border
- `.instruction-first` / `.instruction-middle` / `.instruction-last` - Positionsafhængig styling
- `page-break-inside: avoid` - Browser kan naturligt bryde mellem sektioner
- Stiplet border mellem tilstødende sektioner for visuel sammenhæng

**Resultat:**
- 17 separate instruction-section elementer i stedet for 1 stor code block
- Bedre paginering da hver sektion er et selvstændigt DOM element
- CSS `page-break-inside: avoid` forhindrer brud midt i en sektion

### Filer ændret
- `html_converter.py` - Ny `format_instruction_set()` funktion + CSS klasser
- `CLAUDE.md` - Checkpoint (v14)

---

## Samtale-checkpoint: 5. februar 2025 (session 8)

### Hvad vi lavede i denne session
1. **KRITISK BUG FUNDET OG RETTET** - `splitCodeBlock()` forårsagede uendelig løkke
   - Browser-freeze i Firefox og Chrome
   - Årsag: `continue;` uden `pageIndex++` efter kodeblok-splitting
   - Løsning: Tilføj `pageIndex++` efter splitting for at undgå uendelig løkke

2. **Rollback og analyse** - Bruger rullede tilbage via OneDrive
   - Sammenlignede fungerende (`Rapport CW TEST_backstage.html`) med ødelagte filer (`_NY.html`, `_SIMPLE.html`)
   - Fungerende fil: 58 TOC entries, 2626 linjer
   - Ødelagte filer: 3 TOC entries, 2659 linjer

### Bug-analyse: splitCodeBlock() uendelig løkke

**Problemet (FEJL-koden):**
```javascript
if (overflowIndex === 0) {
  if (firstChild.classList.contains('code-block')) {
    splitCodeBlock(firstChild, content, remainingHeight);
    pages = document.querySelectorAll('.page');
    continue;  // ← BUG: Gentager samme side uden pageIndex++
  }
}
```

**Løsningen (KORREKT kode):**
```javascript
if (overflowIndex === 0) {
  if (firstChild.classList.contains('code-block') &&
      !firstChild.classList.contains('code-block-split')) {
    // Mark as split to prevent infinite loop
    firstChild.classList.add('code-block-split');
    splitCodeBlock(firstChild, content, remainingHeight);
    pages = document.querySelectorAll('.page');
    continue;  // Recheck - nu med flere children (continuations)
  } else if (children.length > 1) {
    overflowIndex = 1;  // Flyt continuation blocks
  } else {
    pageIndex++;  // Accept overflow for single large element
    continue;
  }
}
```

**Nøglen:** `code-block-split` klassen forhindrer at samme kodeblok splittes flere gange.

### Test-filer efterladt til sammenligning
- `Rapport CW TEST_backstage_NY.html` - Ødelagt (uendelig løkke)
- `Rapport CW TEST_backstage_SIMPLE.html` - Ødelagt (forenklet process_runs)
- `Rapport CW TEST_NO_JS.html` - Ødelagt (uden JS - kun 1 side vist)

### Lærdom
- **Test altid pagination-logik** efter ændringer i autoPaginate()
- **Pas på `continue;` i while-løkker** - sikr at loop-variablen opdateres
- **Browser-freeze = ofte uendelig løkke** i JavaScript

### Vigtige filer ændret
- `html_converter.py` - splitCodeBlock() bug rettet
- `CLAUDE.md` - Deep checkpoint (v11)

### Efterfølgende: Generisk element-splitting (v12)

Implementeret robust løsning for alle oversized elementer:

**Nye funktioner:**
- `splitTable()` - Splitter tabeller mellem rækker, gentager header på ny side
- `splitHighlightBox()` - Splitter highlight boxes ved paragraf-grænser
- `splitElement()` - Generisk dispatcher der vælger korrekt split-funktion

**Split-regler:**
| Element | Split-strategi | Marker |
|---------|----------------|--------|
| Tabeller | Mellem rækker, header gentages | "(tabel fortsat)" |
| Kodeblokke | Mellem linjer | "(fortsat)" |
| Highlight boxes | Mellem paragraffer | "(fortsat)" |

**Nye CSS klasser:**
- `.table-continued` - Fortsat tabel fra forrige side
- `.highlight-box-continued` - Fortsat highlight box
- `.table-split`, `.highlight-box-split` - Guards mod uendelig løkke

**Logik:** Når et element er for stort til at passe på en side:
1. Prøv at splitte det med `splitElement()`
2. Hvis splitting lykkedes → recheck siden
3. Hvis ikke → flyt hele elementet til næste side
4. Hvis kun ét element og kan ikke splittes → accepter overflow

### splitCodeBlock() lineHeight bugfix (v13)

**Problemet:** Side 37 havde stadig overflow fordi `splitCodeBlock()` beregnede forkert antal linjer per side.

**Gammel beregning (FEJL):**
```javascript
const lineHeight = 12; // For lav!
const linesPerPage = Math.floor(maxHeight / lineHeight);
// = 838 / 12 = 69 linjer (for mange!)
```

**Ny beregning (KORREKT):**
```javascript
const lineHeight = 16;  // 8pt font × 1.5 line-height = 16px
const blockOverhead = 64;  // padding (32px) + margin (32px)
const linesPerPage = Math.floor((maxHeight - blockOverhead) / lineHeight);
// = (838 - 64) / 16 = 48 linjer ✓
```

**Filer ændret:**
- `html_converter.py` - splitCodeBlock() lineHeight fix
- `Rapport CW TEST_backstage.html` - Samme fix i JavaScript

---

## Samtale-checkpoint: 5. februar 2025 (session 7)

### Hvad vi lavede i denne session
1. **Syntax fix** - Rettet if/elif fejl i `convert_to_html()` (linje 56-60)
2. **QC-funktion forbedret** - Normalisering af overskrifter før sammenligning
   - `normalize_heading()` fjerner thin spaces og ekstra mellemrum
   - Heading truncation øget fra 50 til 80 tegn
   - Logo ekskluderes fra billedtælling
3. **Test script** - `test_converter.py` oprettet til verificering
   - Kører konvertering og QC-tjek
   - Verificerer hyperlinks er inkluderet

### QC Status
- ✅ INGEN KRITISKE ISSUES
- ✅ 5/5 hyperlinks inkluderet
- ✅ 9 H1, 31 H2, 15 H3 matcher
- ✅ 21 tabeller, 2 billeder matcher
- HTML har 309 ekstra ord (forventet: labels, TOC, sidefod)

### Vigtige filer ændret
- `html_converter.py` - Syntax fix, forbedret QC
- `test_converter.py` - Ny testfil

---

## Samtale-checkpoint: 5. februar 2025 (session 6)

### Hvad vi lavede i denne session
1. **Hyperlink-support** - `process_runs()` opdateret til at ekstrahere og formatere hyperlinks fra Word
   - Links bevares som `<a href="..." class="link">` tags
   - CSS styling for links tilføjet (accent blue, underline)
2. **Kodeblok-splitting** - Lange kodeblokke splittes automatisk over flere sider
   - `splitCodeBlock()` JavaScript-funktion tilføjet
   - `.code-block-continued` CSS klasse for fortsættelses-blokke
3. **Forbedret QC-funktion** - Nu med ordantal-sammenligning
   - Tæller ord i både Word og HTML
   - Advarer hvis >10 ord mangler, kritisk issue hvis >50 ord mangler
   - Viser sample af potentielt manglende ord

### Nye CSS klasser
```css
a, a.link {
  color: #3e5cfe;
  text-decoration: underline;
}

.code-block-continued::before {
  content: '(fortsat)';
  font-style: italic;
}
```

### Vigtige filer ændret
- `html_converter.py` - Hyperlink-support i `process_runs()`, forbedret `quality_check()`
- `Rapport CW TEST_backstage.html` - CSS og JS opdateret

---

## Samtale-checkpoint: 5. februar 2025 (session 5)

### Hvad vi lavede i denne session
1. **Bilag-formatering** - Forbedret formatering til at matche Word
   - **Kodeblokke** for instruktionssæt og prompts (Source Code stil → `.code-block`)
   - **Data-labels** for "Datakilder:" headers (→ `.data-label`)
2. Konverteret alle instruktionssæt og evalueringsprompts til kodeblokke

### Nye CSS klasser (tilføjet)
```css
.code-block {
  background: #eef2ff;
  border-left: 3px solid #3e5cfe;
  margin: 16px 0;
  padding: 16px 20px;
}

.code-block code {
  font-family: 'SF Mono', 'Monaco', monospace;
  font-size: 8pt;
  line-height: 1.5;
}

.data-label {
  font-weight: 500;
  font-size: 10pt;
  margin-top: 24px;
  padding-bottom: 4px;
  border-bottom: 1px solid #eef2ff;
}
```

### Vigtige filer ændret
- `html_converter.py` - Tilføjet: `code` stil-detektion, `.code-block` CSS, `.data-label` CSS
- `Rapport CW TEST_backstage.html` - Bilag C, D, E konverteret til kodeblokke

---

## Samtale-checkpoint: 5. februar 2025 (session 4)

### Hvad vi lavede
1. **Caption-undtagelser** - Labels springes over for: Bilag, Ordliste, Appendix, etc.
2. **Brødtekst formatering** - `format_long_text_block()` funktion
3. **Side overflow fix** - maxContentHeight: 242mm → 235mm
4. **QC-funktion** - `quality_check()` og `print_qc_report()`

---

## Samtale-checkpoint: 5. februar 2025 (session 3)

### Hvad vi lavede i denne session
1. **Indholdsfortegnelse tilføjet til test-fil** - Komplet TOC med alle 50+ overskrifter
2. **TOC på egen side** - Flyttet fra forside til side 2
3. **TOC CSS styling** - Hierarkisk indrykning, border-bottom på hver entry
4. **Thin space regel præciseret** - Gælder IKKE for TOC, kun overskrifter i dokumentet
5. **Ingen label/caption på TOC** - Reglen er at TOC ikke har caption
6. **Automatiske sidetal i TOC** - JavaScript genererer sidetal efter pagination
7. **Slettet converter-preview.html** - Overflødig fil, erstattet af Rapport CW TEST_backstage.html

### TOC CSS (tilføjet)
```css
.toc-heading {
  font-family: 'FH Lecturis', Georgia, serif;
  font-size: 20pt;
  color: #001270;
}

.toc-entry {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 10pt;
  margin-bottom: 8px;
}

.toc-level-1 { font-weight: 500; padding-left: 0; }
.toc-level-2 { font-weight: 300; padding-left: 20px; }
.toc-level-3 { font-weight: 300; padding-left: 40px; font-size: 9pt; }
```

### Tal-kerning regel (præcisering)
- Thin space KUN mellem ciffer og punktum når punktum efterfølges af ciffer
- Eksempel: `1.1` → `1   .1` (3x thin space)
- Eksempel: `2.3` → `2 .3` (1x thin space)
- Standalone tal som `1.` i "1. Hovedresultater" får INGEN thin space
- **VIGTIGT:** Reglen gælder IKKE for indholdsfortegnelsen (TOC)

### TOC regler
- TOC skal være på egen side (IKKE på forsiden)
- **INGEN label/caption** over "Indholdsfortegnelse"
- **INGEN toc-divider** under overskriften
- Tynd linje under HVER entry (`border-bottom: 1px solid #eef2ff`)
- Sidetal genereres automatisk via JavaScript EFTER pagination
- Sidetal vises højrejusteret med flexbox

### Vigtige filer ændret
- `Rapport CW TEST_backstage.html` - Nu med komplet indholdsfortegnelse
- `CLAUDE.md` - Denne fil

---

## Tidligere sessions

### Session 2 (5. februar 2025)
1. PDF export fixes - Logo og sidetal pixelering løst
2. Logo: SVG → PNG for bedre print
3. Sidetal: text-stroke: 0 for skarphed
4. Tal-kerning: `format_heading_numbers()` i html_converter.py
5. TOC støtte i Word-konvertering

### Session 1 (5. februar 2025)
1. Øgede afstande mellem elementer
2. Billede-ekstraktion fra Word
3. Auto-labels ved H1 kapitler
4. Tabel-placering fix

---

*Checkpoint gemt: 13. februar 2026 (v27)*
*Denne fil læses automatisk af Claude Code ved hver session.*

---

## QUICK START (til ny session)

```python
# 1. Indlæs Word-dokument
from docx import Document
from html_converter import extract_paragraphs_for_analysis, convert_to_html, quality_check, print_qc_report

doc = Document('Rapport CW TEST.docx')

# 2. Ekstraher paragraffer og analyser semantisk
paragraphs = extract_paragraphs_for_analysis(doc)
# Gennemgå paragraphs og identificer call-out kandidater

# 3. Definer call-outs (eksempel fra seneste test)
# VIGTIGT: Bullet points / list items er ALDRIG callouts!
callout_paragraphs = [
    "NL2DAX-agenten udviser konsekvent lav nøjagtighed",  # Intro-paragraf
    "LLM-modelversionering: Det er ikke transparent",
    "Analysen afslørede flere strukturelle og indholdsmæssige udfordringer",
    "I en hverdag hvor data skal bearbejdes med kritiske øjne",
    "Baseret på fejlanalysen kan performance forbedres markant",
    "Ud over Microsoft Fabric Data Agent blev Databricks Genie Space også evalueret",
]

# 4. Definer forside-indhold
cover_caption = "RAPPORT"  # Dokumenttype
cover_description = "En teknisk evaluering af Microsoft Fabric Data Agents evne til at besvare forretningsspørgsmål via naturligt sprog (NLQ) – med anbefalinger til forbedring."

# 5. Konverter (med forside)
html_output = convert_to_html(
    doc,
    title="Evaluering af NLQ-teknologi for AKA",  # Fra første H1 i Word
    callout_paragraphs=callout_paragraphs,
    cover_caption=cover_caption,
    cover_description=cover_description,
    cover_date="Februar 2026"  # Valgfrit - kun hvis dato findes i dokumentet
)

# 6. Gem i HTML Exports/ mappen (VIGTIGT: fonts virker kun derfra)
with open("HTML Exports/output.html", "w", encoding="utf-8") as f:
    f.write(html_output)

report = quality_check(doc, html_output)
print_qc_report(report)
```
