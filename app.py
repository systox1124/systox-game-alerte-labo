import streamlit as st

accueil = st.Page("accueil.py", title="SysTox Game")
resultat = st.Page("resultat.py", title="SysTox Game")
resultat_mobile = st.Page("resultat_mobile.py", title="SysTox Game")

pg = st.navigation([accueil, resultat, resultat_mobile], position="hidden")
pg.run()