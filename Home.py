import streamlit as st
from repo.repo import Dashboard

st.set_page_config(
    page_title="Home Page",  
    page_icon="📝",                
    layout="wide",             
)

st.write("Home Page")



col1, col2 = st.columns(2)
with col1:
    Dashboard.d_ordini()
with col2:
    Dashboard.d_vendite()

Dashboard.df_ordini()

Dashboard.note()