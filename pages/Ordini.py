import streamlit as st
from repo.repo import Ordine

st.set_page_config(
    page_title="Inserimento Ordini",  
    page_icon="📝",                
    layout="wide",             
)

Ordine.registra()


col1, col2 = st.columns(2)
with col1:
    on = st.toggle("Mostra tabella ordini")
    if on == True:
        Ordine.visulaizza()
with col2:
    mod = st.toggle("Modifica Csv")
    if mod == True:
        Ordine.modifica()


 