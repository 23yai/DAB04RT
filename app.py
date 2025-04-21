# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import plotly.express as px


# Configuración general de la página
st.set_page_config(
    page_title="Visor Ofertas",
    page_icon="insertar icono",
    layout="wide",
    initial_sidebar_state="expanded"
)
    
# Título de la aplicación
st.title("Visor de Ofertas de Empleo")

# Carga de datos visto cache en la web del programador
@st.cache_data
def load_data():
    return pd.read_csv("df_final.csv")

df = load_data()


# Barra lateral fija con menú de navegación usando solo Streamlit
with st.sidebar:
    choice = st.radio(
        "Navegación",
        ("Inicio", "Presentación"),
        index=0
    )

# Interpretamos la selección para el enrutado
if choice.startswith("Inicio"):
    import pages._01_Landing as page_module
else:
    import pages._02_Analisis as page_module

# Ejecutamos la página correspondiente
page_module.app()
