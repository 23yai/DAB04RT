# pages/07_powerbi.py


import streamlit as st
import pandas as pd
import plotly.express as px

def page_powerbi():

    powerbi_width = 1500
    powerbi_height = 1000
    st.markdown(body = f'<iframe title="proyecto power bi inmobiliario." width="{powerbi_width}" height="{powerbi_height}" src="https://app.powerbi.com/view?r=eyJrIjoiZTExYmMyMzAtYmY0Ni00NGIxLWE1MGEtMDAyMjc0ZTkzMDAzIiwidCI6IjVlNzNkZTM1LWU4MjUtNGVkNS1iZTIyLTg4NTYzNTI3MDkxZSIsImMiOjl9&pageName=6f77bdd5799feaa9c9e0" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)