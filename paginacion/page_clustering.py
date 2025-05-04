# pages/06_Clustering.py
# YAIZA 

import streamlit as st
import pandas as pd
import plotly.express as px

def page_clustering():
    st.title("📊 Exploración y Filtrado de Clusters")
    st.markdown(
        "En esta página puedes filtrar las ofertas según las variables usadas "
        "para el clustering y ver cómo se distribuyen los diferentes grupos.\n\n" 
        "Agrupa las ofertas en clusters basados en 7 variables clave:\n\n"
    "• Estudios\n\n"
    "• Experiencia\n\n"
    "• Número de skills\n\n"
    "• Tecnologías/apts\n\n"
    "• Vacaciones\n\n"
    "• Beneficios\n\n"
    "• Salario medio\n\n"
    "Se incorpora un formulario con inputs para las siete variables de una nueva oferta en el lateral izquierdo de la página. Al pulsar “Clasificar”, se escala el vector de entrada y se predice su cluster asociado usando los centroides del modelo de clustering. De esta forma, se demuestra cómo el sistema puede preetiquetar nuevas ofertas en tiempo real."

    )

    