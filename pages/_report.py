import streamlit as st

st.title("📄 Report")
st.write(
    """
    Qui verrà generato un **riepilogo** scaricabile dei risultati:
    - input inseriti,
    - percentuale ed esito,
    - data/ora e versione del modello.

    
    """
)

from ui import render_footer
render_footer("Vincenzo Franzone","https://github.com/vincenzofranzonee" , "https://github.com/vincenzofranzonee")