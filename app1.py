# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 17:42:53 2025

@author: Usuario
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Visor de Ofertas de Empleo Tecnológico")

# Carga de datos
@st.cache_data
def load_data():
    df = pd.read_csv("ruta/a/tu/archivo.csv")  # Reemplaza con la ruta real
    return df

df = load_data()

# Filtros
st.sidebar.header("Filtros")
ubicaciones = df['ubicacion'].dropna().unique()
ubicacion_seleccionada = st.sidebar.multiselect("Ubicación", ubicaciones, default=ubicaciones)

# Aplicar filtros
df_filtrado = df[df['ubicacion'].isin(ubicacion_seleccionada)]

# Mostrar tabla
st.subheader("Ofertas de Empleo")
st.dataframe(df_filtrado)

# Gráfico de tecnologías más demandadas
st.subheader("Tecnologías Más Demandadas")
# Suponiendo que 'tecnologias_aptitudes' es una lista separada por comas
from collections import Counter
import itertools

tecnologias = df_filtrado['tecnologias_aptitudes'].dropna().apply(lambda x: [i.strip() for i in x.split(',')])
tecnologias_lista = list(itertools.chain.from_iterable(tecnologias))
tecnologias_contador = Counter(tecnologias_lista)
tecnologias_df = pd.DataFrame(tecnologias_contador.items(), columns=['Tecnología', 'Cantidad']).sort_values(by='Cantidad', ascending=False)

fig = px.bar(tecnologias_df.head(10), x='Tecnología', y='Cantidad', title='Top 10 Tecnologías Más Demandadas')
st.plotly_chart(fig)
