"""
Test script til at køre Word-til-HTML konvertering med QC-tjek.
Verificerer at al tekst inkluderes, herunder hyperlinks.
"""

from docx import Document
from html_converter import convert_to_html, quality_check, print_qc_report

# Åbn Word-dokumentet
doc_path = "Rapport CW TEST.docx"
print(f"Åbner: {doc_path}")
doc = Document(doc_path)

# Konverter til HTML
print("Konverterer til HTML...")
html_output = convert_to_html(doc, title="Rapport CW TEST")

# Gem HTML-output
output_path = "Rapport CW TEST_backstage_NY.html"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_output)
print(f"HTML gemt til: {output_path}")

# Kør QC-tjek
print("\nKører QC-tjek...")
qc_report = quality_check(doc, html_output)
print_qc_report(qc_report)

# Ekstra check: find alle hyperlinks i Word og verificer de er i HTML
print("\n" + "=" * 60)
print("HYPERLINK VERIFICERING")
print("=" * 60)

from docx.oxml.ns import qn as oxml_qn
import re

word_links = []
for para in doc.paragraphs:
    for child in para._element:
        if child.tag.endswith('hyperlink'):
            r_id = child.get(oxml_qn('r:id'))
            if r_id:
                try:
                    rel = para.part.rels[r_id]
                    url = rel.target_ref if hasattr(rel, 'target_ref') else str(rel._target)
                    word_links.append(url)
                except:
                    pass

print(f"\nFundet {len(word_links)} hyperlinks i Word-dokument:")
for i, link in enumerate(word_links, 1):
    print(f"  {i}. {link[:60]}{'...' if len(link) > 60 else ''}")

# Check at links er i HTML (alle typer links - http, https, file, etc.)
html_link_count = html_output.count('<a href="')
print(f"\nAntal links i HTML: {html_link_count}")

if len(word_links) > html_link_count:
    print(f"⚠️ ADVARSEL: {len(word_links) - html_link_count} links mangler i HTML!")
elif html_link_count >= len(word_links):
    print("✅ Alle links er inkluderet i HTML")
