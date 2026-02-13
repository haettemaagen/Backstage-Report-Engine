"""
Backstage Word Dokument Converter
=================================
Web-app til konvertering af Word-dokumenter til Backstage's visuelle identitet.

Kør med: streamlit run app.py
"""

import streamlit as st
from docx import Document
from io import BytesIO
import os

from converter import convert_document

# =============================================================================
# PAGE CONFIG
# =============================================================================

st.set_page_config(
    page_title="Backstage Dokument Converter",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# CUSTOM CSS
# =============================================================================

st.markdown("""
<style>
    /* Backstage farver */
    :root {
        --primary-blue: #001270;
        --accent-blue: #3e5cfe;
        --bg-light: #eef2ff;
    }

    /* Header */
    .main-header {
        color: #001270;
        font-size: 2.5rem;
        font-weight: 400;
        margin-bottom: 0.5rem;
    }

    .sub-header {
        color: #001270;
        font-size: 1.1rem;
        font-weight: 300;
        margin-bottom: 2rem;
        opacity: 0.8;
    }

    /* Upload area */
    .stFileUploader > div > div {
        border: 2px dashed #3e5cfe;
        border-radius: 12px;
        padding: 2rem;
    }

    /* Buttons */
    .stDownloadButton > button {
        background-color: #3e5cfe;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-size: 1rem;
        font-weight: 500;
    }

    .stDownloadButton > button:hover {
        background-color: #001270;
    }

    /* Info boxes */
    .info-box {
        background-color: #eef2ff;
        border-left: 3px solid #3e5cfe;
        padding: 1rem 1.5rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #666;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #eee;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# HEADER
# =============================================================================

st.markdown('<h1 class="main-header">Backstage</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Word Dokument Converter</p>', unsafe_allow_html=True)

# =============================================================================
# MAIN CONTENT
# =============================================================================

st.markdown("""
Upload dit Word-dokument, og få det konverteret til Backstage's visuelle identitet.
""")

# Info box
st.markdown("""
<div class="info-box">
    <strong>Hvad konverteren gør:</strong>
    <ul style="margin-top: 0.5rem; margin-bottom: 0;">
        <li>Skifter overskrifter til FH Lecturis font</li>
        <li>Skifter brødtekst til Helvetica Neue</li>
        <li>Anvender Backstage's blå farver</li>
        <li>Konverterer bullet points til pile (→)</li>
        <li>Formaterer tabeller korrekt</li>
        <li>Tilføjer highlight boxes til vigtige afsnit</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# File uploader
uploaded_file = st.file_uploader(
    "Vælg et Word-dokument (.docx)",
    type=["docx"],
    help="Upload det dokument du vil konvertere"
)

if uploaded_file is not None:
    # Show file info
    st.success(f"✓ Fil uploadet: **{uploaded_file.name}** ({uploaded_file.size / 1024:.1f} KB)")

    # Convert button
    if st.button("🔄 Konverter dokument", type="primary", use_container_width=True):
        with st.spinner("Konverterer dokument..."):
            try:
                # Load document
                doc = Document(BytesIO(uploaded_file.read()))

                # Convert
                converted_doc = convert_document(doc)

                # Save to buffer
                output_buffer = BytesIO()
                converted_doc.save(output_buffer)
                output_buffer.seek(0)

                # Generate output filename
                original_name = uploaded_file.name.rsplit('.', 1)[0]
                output_filename = f"{original_name}_backstage.docx"

                st.success("✓ Dokument konverteret!")

                # Download button
                st.download_button(
                    label="⬇️ Download konverteret dokument",
                    data=output_buffer,
                    file_name=output_filename,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )

            except Exception as e:
                st.error(f"Der opstod en fejl under konvertering: {str(e)}")
                st.info("Tip: Sørg for at filen er et gyldigt .docx dokument")

else:
    # Placeholder when no file is uploaded
    st.info("👆 Upload et Word-dokument for at komme i gang")

# =============================================================================
# SIDEBAR - Avancerede indstillinger (til senere)
# =============================================================================

with st.sidebar:
    st.markdown("### ⚙️ Indstillinger")
    st.markdown("*Kommer snart*")

    st.markdown("---")

    st.markdown("""
    **Konverteringsregler:**
    - Heading 1 → 32pt
    - Heading 2 → 20pt
    - Heading 3 → 14pt
    - Brødtekst → 10pt
    """)

# =============================================================================
# FOOTER
# =============================================================================

st.markdown("""
<div class="footer">
    Backstage Word Converter v1.0<br>
    Kontakt support hvis du oplever problemer
</div>
""", unsafe_allow_html=True)
