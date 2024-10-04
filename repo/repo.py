import streamlit as st
import pandas as pd

class Ordine():
    def registra():
        with st.form(key="my form"):
            nome_clie = st.text_input("Nome Cliente: ")
            cognome_clie = st.text_input("Cognome Cliente: ")
            articolo_ord = st.text_input("Articolo Ordinato: ")
            valore = st.number_input("Valore: ")
            valore = str(valore)
            consegna = st.date_input("Consegna: ")
            consegna = str(consegna)

            import os 
            lista = os.listdir()
            if 'ordini.csv' not in lista:
                with open('ordini.csv','w') as x:
                    x.write('nome,cognome,articolo,valore,consegna' + "\n")
                    x.write(nome_clie + "," + cognome_clie + "," + articolo_ord + "," + valore + "," + consegna + "\n")
                st.success("Dati Registrati! ")
            elif nome_clie and cognome_clie and articolo_ord and valore and consegna != "":
                    with open('ordini.csv','a') as x:
                        x.write(nome_clie + "," + cognome_clie + "," + articolo_ord + "," + valore + "," + consegna + "\n")
                    st.success("Dati Registrati! ")
            else:
                st.warning("Nessun Dato Inserito")
            submit_btn = st.form_submit_button("Registra")

    def visulaizza():
        df = pd.read_csv('ordini.csv',encoding='utf-8')
        st.dataframe(df)

    def modifica():
        df = pd.read_csv('ordini.csv',encoding='utf-8')
        st.data_editor(df, num_rows="dynamic")

class Dashboard():

    def d_ordini():
        st.write("Resoconto Ordini")
        df = pd.read_csv('ordini.csv')
        df['valore'] = df['valore'].astype(int)  # Convert 'valore' to int
        dfok = df[['nome', 'valore']]
        st.bar_chart(dfok.set_index('nome'))
    def d_vendite():
        df = pd.read_csv('ordini.csv')
        st.write("Vendite Data")
        dfok1 = df[['consegna', 'valore']]
        st.line_chart(dfok1.set_index('consegna'))
    def df_ordini():
        df = pd.read_csv('ordini.csv')
        st.table(df)
    def note():
        text_content = st.text_area("Inserisci un appunto personale: ")
        st.download_button("Scarica Il File Txt", text_content)




