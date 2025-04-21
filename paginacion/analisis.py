# -*- coding: utf-8 -*-

# pages/02_Analisis.py
import streamlit as st
import pandas as pd
import folium
import plotly.express as px
from streamlit_folium import st_folium

def page_analisis():
    st.title("¡Encuentra tu puesto!")

    # Mostramos la ilustración de job cards
    st.image(
        "assets/couple_searching_job.png",
        caption="Filtra y busca empleos de datos rápidamente",
        use_container_width=False,
        width=900  
    )

    # Carga de CSV
    df = pd.read_csv("df_final.csv")  # tu CSV

    salario_min = st.sidebar.slider('Salario mínimo', int(df['salario_min'].min()), int(df['salario_min'].max()), value = int(df["salario_min"].mean()))
    contratos = st.sidebar.multiselect('Tipo de contrato', df['contrato'].unique(), default = ["Indefinido"])
    #tecnologias = st.sidebar.multiselect('Tecnologías', df['tecnologias_aptitudes'].unique())
    # experiencia = st.sidebar.selectbox('Experiencia', df['experiencia'].unique())
    jornada = st.sidebar.selectbox('jornada', df['jornada'].unique())
    ubicaciones = st.sidebar.multiselect('Ubicacion', df['ubicacion'].unique(), default = ["Madrid"])

    df = df[(df["ubicacion"].isin(ubicaciones)) &\
            (df["salario_min"] <= float(salario_min)) &\
            (df["contrato"].isin(contratos)) &\
            # (df["experiencia"] == experiencia) &\
            (df["jornada"] == jornada)]

    # Filtros interactivos
    funciones = df["funcion"].unique().tolist()
    sel_fun = st.multiselect("Filtra por función", funciones, default=funciones)
    df_f = df[df["funcion"].isin(sel_fun)]
    st.write(f"Total ofertas: {len(df_f)}")
    #st.dataframe(df_f, use_container_width=True)
    st.dataframe(
            df_f[["oferta", "empresa", "funcion", "salario_min", "ubicacion", "jornada", "contrato", "id_urls"]],
            use_container_width=True
    )


    # Mapa con Folium
    st.subheader("Mapa de ubicaciones/Segundo Sprint, se necesita latitud y longitud")
    m = folium.Map(location=[40.4, -3.7], zoom_start=5)
    # for _, row in df_f.iterrows():
    #     folium.Marker(
    #         location=[row["lat"], row["lon"]],
    #         popup=row["Empresa"]
    #     ).add_to(m)
    st_folium(m, width="100%", height=400)

    #Aternativas para ubicacion
    # Normaliza columna
        # df["ubicacion"] = df["ubicacion"].str.strip().fillna("Desconocido")

        # # Cuenta ofertas por ubicación
        # conteo = df["ubicacion"].value_counts().reset_index()
        # conteo.columns = ["ubicacion", "cantidad"]

        # # Gráfico horizontal
        # fig = px.bar(
        #     conteo, 
        #     x="cantidad", 
        #     y="ubicacion", 
        #     orientation="h",
        #     labels={"cantidad":"Ofertas", "ubicacion":"Ubicación"},
        #     title="Ofertas por Ubicación"
        # )
        # st.plotly_chart(fig, use_container_width=True)

    # Dashboard: gráfico de salarios
    # st.subheader("Distribución de Salarios")
    # salarios = df_f["salario_min"].dropna().apply(str).str.replace("k","",regex=False).astype(float)
    # st.bar_chart(salarios)

    # # Empresas con mas ofertas publicadas
    # st.subheader("Empresas con mas ofertas publicadas")
    # ofertas_por_empresa = df["empresa"].value_counts().head(10)
    # st.bar_chart(ofertas_por_empresa)

    #ejemplo como el histograma de tarifas y edades. Pero en experiencia requerida.
    # Extraer valor numérico (ej: '3 años' → 3)
    # no sale lo que quiero. grafico de barras solo con numeros.
    # exp_raw = df["experiencia"].fillna("").astype(str)
    # exp_num = exp_raw.str.extract(r"(\d+)")[0].astype(float)
    # exp_counts = exp_num.value_counts().sort_index()
    # st.subheader("Distribución de Experiencia (años)")
    # st.bar_chart(exp_counts)


    # #Pie Chart tipo de contratos (visto en clase)
    # contratos = df["Contrato"].value_counts()
    # # Con Plotly Express
    # fig = px.pie(
    #     names=contratos.index,
    #     values=contratos.values,
    #     title="Distribución de Tipos de Contrato"
    # )
    # st.plotly_chart(fig, use_container_width=True)

