# Backstage Visuel Identitet Guide for AI

Denne guide indeholder alle specifikationer til at generere dokumenter i Backstage's visuelle identitet.

---

## 1. Farver

| Navn | Hex | Anvendelse |
|------|-----|------------|
| Primary Blue Dark | `#001270` | Overskrifter, brødtekst, logo |
| Accent Blue | `#3e5cfe` | Labels, links, ikoner, fremhævelser |
| Background Light | `#eef2ff` | Highlight boxes, tabel-striber |
| White | `#ffffff` | Sidebaggrund |

---

## 2. Typografi

### Fonte
- **Overskrifter:** FH Lecturis (custom font)
- **Brødtekst:** Helvetica Neue

### Font-filer (lokale)
```
fonts/
├── FHLecturis_BSCustom_Regular.otf   ← Overskrifter (H1, H2, H3)
├── FHLecturis_BSCustom_Bold.otf
├── FHLecturis_BSCustom_Light.otf
└── HelveticaNeue/
    ├── HelveticaNeue-Light-08.ttf    ← Brødtekst (weight 300)
    ├── HelveticaNeue-Medium-11.ttf   ← Labels, tabel headers (weight 500)
    ├── HelveticaNeue-01.ttf          ← Regular (weight 400)
    └── HelveticaNeue-Bold-02.ttf     ← Fed tekst (weight 700)
```

### Skala (til A4 print/Word)

| Element | Font | Vægt | Størrelse | Line Height | Letter Spacing |
|---------|------|------|-----------|-------------|----------------|
| H1 | FH Lecturis | Regular (400) | 32pt | 0.95 | -1pt |
| H2 | FH Lecturis | Regular (400) | 20pt | 0.95 | -0.6pt |
| H3 | FH Lecturis | Regular (400) | 14pt | 1.0 | -0.4pt |
| Subheading | Helvetica Neue | Light (300) | 13pt | 1.3 | -0.4pt |
| Body | Helvetica Neue | Light (300) | 10pt | 1.7 | -0.3pt |
| Label | Helvetica Neue | Medium (500) | 9pt | 1.2 | 0.5px, UPPERCASE |
| Table Header | Helvetica Neue | Medium (500) | 9pt | 1.2 | 0 |
| Table Cell | Helvetica Neue | Light (300) | 9pt | 1.4 | 0 |

### Margins (afstande)

| Element | Margin Top | Margin Bottom |
|---------|------------|---------------|
| H1 | 12px | 24px |
| H2 | 36px | 18px |
| H3 | 28px | 14px |
| Body (p) | 0 | 10px |
| List item | 0 | 12px |
| Highlight box | 24px | 24px |
| Table | 24px | 24px |
| Billede | 24px | 24px |

---

## 3. Komponenter

### Label med streg
```css
.label {
  font-family: 'Helvetica Neue', sans-serif;
  font-weight: 500;
  font-size: 9pt;
  color: #3e5cfe;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding-bottom: 10px;
  border-bottom: 2px solid #3e5cfe;
  display: inline-block;
  margin-bottom: 10px;
}
```

**Auto-generering af labels ved konvertering:**
- Labels tilføjes automatisk før hver H1 (kapitel)
- Mønstergenkendelse: "Resumé", "Konklusion", "Metodik", "Resultater", etc.
- Fallback: Første 2-3 ord fra H1-titlen (max 25 tegn)

### Highlight Box
```css
.highlight-box {
  background: #eef2ff;
  padding: 16px 20px;
  margin: 20px 0;
  border-left: 3px solid #3e5cfe;
}
```

**Trigger keywords:** Tekst der starter med disse ord får automatisk highlight box:
- "Vigtig:" / "Vigtigt:"
- "Konklusion:" / "Hovedkonklusion:"
- "Bemærk:" / "OBS:" / "Note:"
- "Anbefaling:"

### Bullet Points (pile-stil)
```css
ul li::before {
  content: '→';
  color: #3e5cfe;
}
```

### Nummererede faser (cirkler)
```css
.phase-number {
  background: #3e5cfe;
  color: white;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11pt;
  font-weight: 500;
}
```

### Tabel
```css
table { border-collapse: collapse; width: 100%; }
th {
  font-weight: 500;
  text-align: left;
  padding: 10px 8px;
  border-bottom: 2px solid #001270;
  color: #001270;
}
td {
  font-weight: 300;
  padding: 8px;
  border-bottom: 1px solid #eef2ff;
  color: #001270;
}
```

### Billeder
```css
.image-container {
  margin: 24px 0;
  text-align: center;
}

.image-container img {
  max-width: 100%;
  height: auto;
}
```

**Billede-håndtering ved konvertering:**
- Billeder fra Word-dokumenter ekstraheres automatisk
- Konverteres til base64 og indlejres i HTML
- Centreres på siden med 24px margin over/under

---

## 4. Layout (A4)

- **Sidebredde:** 210mm
- **Sidehøjde:** 297mm
- **Marginer:** 20mm alle sider

### Sidefod
- **Logo:** Backstage SVG, position: absolute, bottom: 15mm, left: 20mm
- **Sidetal:** position: absolute, bottom: 15mm, right: 20mm, font-size: 9pt, font-weight: 300

---

## 5. Font Embedding (CSS)

```css
/* FH Lecturis - Backstage custom font */
@font-face {
  font-family: 'FH Lecturis';
  src: url('fonts/FHLecturis_BSCustom_Regular.otf') format('opentype');
  font-weight: 400;
  font-style: normal;
}

@font-face {
  font-family: 'FH Lecturis';
  src: url('fonts/FHLecturis_BSCustom_Bold.otf') format('opentype');
  font-weight: 700;
  font-style: normal;
}

@font-face {
  font-family: 'FH Lecturis';
  src: url('fonts/FHLecturis_BSCustom_Light.otf') format('opentype');
  font-weight: 300;
  font-style: normal;
}

/* Helvetica Neue */
@font-face {
  font-family: 'Helvetica Neue';
  src: url('fonts/HelveticaNeue/HelveticaNeue-Light-08.ttf') format('truetype');
  font-weight: 300;
  font-style: normal;
}

@font-face {
  font-family: 'Helvetica Neue';
  src: url('fonts/HelveticaNeue/HelveticaNeue-Medium-11.ttf') format('truetype');
  font-weight: 500;
  font-style: normal;
}
```

---

## 6. Struktur for rapporter

### Sidehierarki
1. **Forside:** Label → H1 titel → Subheading → Resumé
2. **Indholdssider:** Label → H1 → Indhold → Sidefod (logo + sidetal)

### Teksthierarki
- Label (kategori) med streg
- H1 (hovedtitel)
- H2 (sektioner)
- H3 (undersektioner)
- Body (brødtekst)

---

## 7. Eksempel HTML-struktur

```html
<div class="page">
  <span class="label">Kategori</span>
  <h1>Hovedtitel</h1>

  <div class="subheading">Underoverskrift eller manchet</div>

  <h2>Sektion</h2>
  <p>Brødtekst med <strong>fed tekst</strong> og <span class="accent">accent farve</span>.</p>

  <div class="highlight-box">
    <p><strong>Vigtig pointe:</strong> Fremhævet tekst i boks.</p>
  </div>

  <ul>
    <li>Bullet point med pil</li>
    <li>Endnu et punkt</li>
  </ul>

  <table>
    <thead>
      <tr><th>Kolonne 1</th><th>Kolonne 2</th></tr>
    </thead>
    <tbody>
      <tr><td>Data</td><td>Data</td></tr>
    </tbody>
  </table>

  <!-- Sidefod -->
  <div class="footer-logo">[Backstage SVG Logo]</div>
  <div class="page-number">1</div>
</div>
```

---

## 8. Regler for AI

1. **Brug altid** FH Lecturis til overskrifter (H1, H2, H3) og Helvetica Neue til brødtekst
2. **Labels** skal være uppercase med blå streg under (10px afstand)
3. **Undgå** bullet points i traditionel stil – brug pile (→) eller nummererede cirkler
4. **Highlight boxes** bruges til vigtige konklusioner eller key takeaways (genkend keywords automatisk)
5. **Tabeller** har fed header-linje (2px) og tynde skillelinjer (#eef2ff)
6. **Farver** er kun Primary Blue (#001270) og Accent Blue (#3e5cfe) – ingen andre farver
7. **Sidefod:** Logo nederst venstre, sidetal nederst højre
8. **Alle tekst** skal være i Primary Blue (#001270)

---

## 9. Reference-filer

| Fil | Beskrivelse |
|-----|-------------|
| `Rapport CW TEST_backstage.html` | Hoved test-fil med TOC og alle features |
| `backstage-aka-rapport.html` | Komplet eksempel-rapport |
| `Backstage Logo SVG - Dark On White.svg` | Logo til brug i dokumenter |
