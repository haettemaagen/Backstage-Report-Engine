"""
Backstage Visuel Identitet - Style Definitioner
================================================
Alle farver, fonte og størrelser til Word-dokumenter.
"""

from docx.shared import Pt, RGBColor, Cm, Twips
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT

# =============================================================================
# FARVER
# =============================================================================

class Colors:
    """Backstage farvepalet"""
    PRIMARY_BLUE = RGBColor(0x00, 0x12, 0x70)      # #001270 - Overskrifter, brødtekst
    ACCENT_BLUE = RGBColor(0x3E, 0x5C, 0xFE)       # #3e5cfe - Labels, links, ikoner
    BACKGROUND_LIGHT = RGBColor(0xEE, 0xF2, 0xFF)  # #eef2ff - Highlight boxes
    WHITE = RGBColor(0xFF, 0xFF, 0xFF)             # #ffffff - Sidebaggrund


# =============================================================================
# FONTE
# =============================================================================

class Fonts:
    """Font-navne"""
    HEADING = "FH Lecturis"           # Overskrifter (H1, H2, H3)
    HEADING_FALLBACK = "Georgia"      # Fallback hvis FH Lecturis mangler
    BODY = "Helvetica Neue"           # Brødtekst
    BODY_FALLBACK = "Arial"           # Fallback


# =============================================================================
# TYPOGRAFI - STØRRELSER OG VÆGTE
# =============================================================================

class Typography:
    """Typografi-specifikationer"""

    # Heading 1
    H1_SIZE = Pt(32)
    H1_LINE_SPACING = 0.95
    H1_LETTER_SPACING = Pt(-1)
    H1_SPACE_BEFORE = Pt(12)
    H1_SPACE_AFTER = Pt(24)

    # Heading 2
    H2_SIZE = Pt(20)
    H2_LINE_SPACING = 0.95
    H2_LETTER_SPACING = Pt(-0.6)
    H2_SPACE_BEFORE = Pt(28)
    H2_SPACE_AFTER = Pt(14)

    # Heading 3
    H3_SIZE = Pt(14)
    H3_LINE_SPACING = 1.0
    H3_LETTER_SPACING = Pt(-0.4)
    H3_SPACE_BEFORE = Pt(20)
    H3_SPACE_AFTER = Pt(10)

    # Subheading
    SUBHEADING_SIZE = Pt(13)
    SUBHEADING_LINE_SPACING = 1.3
    SUBHEADING_LETTER_SPACING = Pt(-0.4)

    # Body / Normal tekst
    BODY_SIZE = Pt(10)
    BODY_LINE_SPACING = 1.5
    BODY_LETTER_SPACING = Pt(-0.3)
    BODY_SPACE_AFTER = Pt(10)

    # Label (kategori med streg)
    LABEL_SIZE = Pt(9)
    LABEL_LINE_SPACING = 1.2
    LABEL_LETTER_SPACING = Pt(0.5)

    # Tabel
    TABLE_HEADER_SIZE = Pt(9)
    TABLE_CELL_SIZE = Pt(9)
    TABLE_LINE_SPACING = 1.4

    # Sidetal
    PAGE_NUMBER_SIZE = Pt(9)


# =============================================================================
# LAYOUT - A4 SIDEFORMAT
# =============================================================================

class Layout:
    """A4 sidelayout"""
    PAGE_WIDTH = Cm(21.0)
    PAGE_HEIGHT = Cm(29.7)

    MARGIN_TOP = Cm(2.0)
    MARGIN_BOTTOM = Cm(2.0)
    MARGIN_LEFT = Cm(2.0)
    MARGIN_RIGHT = Cm(2.0)


# =============================================================================
# HIGHLIGHT KEYWORDS
# =============================================================================

# Tekst der starter med disse ord får highlight box
HIGHLIGHT_KEYWORDS = [
    "Vigtig:",
    "Vigtigt:",
    "Konklusion:",
    "Hovedkonklusion:",
    "Bemærk:",
    "OBS:",
    "Note:",
    "Anbefaling:",
]

# Bullet point symbol
BULLET_SYMBOL = "→"
