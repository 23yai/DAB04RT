# -*- coding: utf-8 -*-



# pages/02_Analisis.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def app():
    st.title("Presentación de Datos")

    # Carga de CSV
    df = pd.read_csv("df_final.csv")  # tu CSV
    # Filtros interactivos
    funciones = df["Función"].unique().tolist()
    sel_fun = st.multiselect("Filtra por función", funciones, default=funciones)
    df_f = df[df["Función"].isin(sel_fun)]
    st.write(f"Total ofertas: {len(df_f)}")
    st.dataframe(df_f, use_container_width=True)

    # Mapa con Folium
    st.subheader("Mapa de ubicaciones")
    m = folium.Map(location=[40.4, -3.7], zoom_start=5)
    for _, row in df_f.iterrows():
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=row["Empresa"]
        ).add_to(m)
    st_folium(m, width="100%", height=400)

    # Dashboard: gráfico de salarios
    st.subheader("Distribución de Salarios")
    salarios = df_f["Salario"].dropna().str.replace("k","",regex=False).astype(float)
    st.bar_chart(salarios)