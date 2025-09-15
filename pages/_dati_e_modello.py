import streamlit as st

st.title("📊 Dati & Modello — Panoramica")
st.write(
    """
    In questa pagina verranno mostrati:
    - il dataset utilizzato (anteprima e descrizione colonne),
    - i passaggi di **pre‑processing** (pulizia, encoding, scaling),
    - il **modello** scelto per la classificazione (baseline).

    """
)

from ui import render_footer
render_footer("Vincenzo Franzone","https://github.com/vincenzofranzonee" , "https://github.com/vincenzofranzonee")