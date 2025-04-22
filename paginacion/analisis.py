# -*- coding: utf-8 -*-

# pages/02_Analisis.py
import streamlit as st
import pandas as pd
import folium
import plotly.express as px
from streamlit_folium import st_folium
import mysql
import mysql.connector


def conectar_db(host = "localhost", user = "root", password = "Nica100!", database = "ofertas_empleo"):
    return mysql.connector.connect(host = host,
                                    user = user,
                                    password = password,
                                    database = database
                                )
def ejecutar_query(query, db_conectada):
    cursor = db_conectada.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    columnas = [col[0] for col in cursor.description]
    df = pd.DataFrame(data, columns=columnas)
    cursor.close()
    return df


def page_analisis():
    st.title("¡Encuentra tu puesto!")

    # Mostramos la ilustración de job cards
    st.image(
        "assets/couple_searching_job.png",
        caption="Filtra y busca empleos de datos rápidamente",
        use_container_width=False,
        width=1200  
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



    #######################################################################
    #cantidad de ofertas por ubicacion
    query = '''SELECT 
                u.ubicacion,
                COUNT(o.id_urls) AS cantidad_ofertas
            FROM ofertas o
            JOIN ubicacion u ON o.id_ubicacion = u.id_ubicacion
            GROUP BY u.ubicacion
            ORDER BY cantidad_ofertas DESC;'''

    db_conectada = conectar_db()

    df_ofertas_por_ubicacion = ejecutar_query(query, db_conectada)

    db_conectada.close()

    fig1 = px.bar(data_frame = df_ofertas_por_ubicacion.iloc[:10, :], x = "ubicacion", y = "cantidad_ofertas", title = "Cantidad de ofertas por ubicacion")
    st.plotly_chart(fig1)
    st.write("El gráfico de barras muestra las diez ubicaciones que concentran el mayor número de ofertas de empleo de nuestro conjunto de datos. En el eje horizontal aparecen las ubicaciones (ciudades o regiones), ordenadas de mayor a menor número de vacantes, y en el eje vertical se indica la cantidad de ofertas publicadas en cada una. " \
    "Gracias a esta visualización se puede identificar rápidamente los mercados laborales más activos y focalizar tu búsqueda en aquellas zonas donde la oferta es más abundante. ")

#######################################################################

    #media salarial por función en cada ubicacion
    query = '''SELECT 
                u.ubicacion,
                o.funcion,
                AVG((o.salario_min + o.salario_max)/2) AS salario_promedio
            FROM ofertas o
            JOIN ubicacion u ON o.id_ubicacion = u.id_ubicacion
            WHERE o.salario_min IS NOT NULL AND o.salario_max IS NOT NULL
            GROUP BY u.ubicacion, o.funcion
            ORDER BY salario_promedio DESC;'''

    db_conectada = conectar_db()

    df_salario_por_funcion_ubicacion = ejecutar_query(query, db_conectada)

    db_conectada.close()

    df_salario_por_funcion_ubicacion_2 = df_salario_por_funcion_ubicacion.groupby(by = "funcion", as_index = False).agg({"salario_promedio" : "mean"})
    df_salario_por_funcion_ubicacion_2 = df_salario_por_funcion_ubicacion_2.sort_values("salario_promedio", ascending = False)
    fig2 = px.bar(data_frame = df_salario_por_funcion_ubicacion_2, x = "funcion", y = "salario_promedio")
    st.subheader("Salario en funcion de puesto de trabajo")
    st.plotly_chart(fig2)
    st.write(
        "Esta barra representa el salario medio anual para cada rol o función, "
        "calculado como la media de los extremos salarial mínimo y máximo de todas "
        "las ofertas"
    )
#######################################################################

# Promedio salarial por experiencia y función
    query = '''
        SELECT 
            o.funcion,
            o.experiencia,
            AVG((o.salario_min + o.salario_max) / 2) AS salario_promedio
        FROM ofertas o
        WHERE o.salario_min IS NOT NULL 
        AND o.salario_max IS NOT NULL
        AND o.experiencia IS NOT NULL
        GROUP BY o.funcion, o.experiencia
        ORDER BY o.funcion, o.experiencia;
    '''

    # Abrimos y cerramos la conexión DB
    db_conectada = conectar_db()
    df_salario_promedio_exp_func = ejecutar_query(query, db_conectada)
    db_conectada.close()

    fig3 = px.bar(
        data_frame=df_salario_promedio_exp_func,
        x="experiencia",
        y="salario_promedio",
        color="funcion",
        barmode="group",
        title="Salario Promedio por Experiencia y Función",
        labels={
            "experiencia": "Años de Experiencia",
            "salario_promedio": "Salario Medio (€)",
            "funcion": "Función / Rol"
        }
    )

    # Mostramos en Streamlit
    st.plotly_chart(fig3, use_container_width=True)
    st.write(
        "Esta gráfica compara el salario medio para cada combinación de rol y nivel de "
        "experiencia, lo que nos ayuda a ver cómo varía la retribución según los años de carrera "
        "y la función desempeñada."
    )


#####################################################

    # Mapa con Folium
    st.subheader("Mapa de ubicaciones. latitud y longitud")
    m = folium.Map(location=[40.4, -3.7], zoom_start=5)
    # for _, row in df_f.iterrows():
    #     folium.Marker(
    #         location=[row["lat"], row["lon"]],
    #         popup=row["Empresa"]
    #     ).add_to(m)
    st_folium(m, width="100%", height=400)



################################################
    
    query = """
    SELECT 
        ot.habilidad_tecnica,
        COUNT(*) AS cantidad_ofertas
    FROM oferta_tecnologia ot
    JOIN ofertas o ON ot.id_urls = o.id_urls
    WHERE o.funcion = 'Data Analyst'
    GROUP BY ot.habilidad_tecnica
    ORDER BY cantidad_ofertas DESC
    LIMIT 10;
"""

    db_conectada = conectar_db()
    df_tecnologias_funcion = ejecutar_query(query, db_conectada)
    db_conectada.close()

    fig4 = px.bar(
        df_tecnologias_funcion,
        x="cantidad_ofertas",
        y="habilidad_tecnica",
        orientation="h",
        title="Top 10 tecnologías solicitadas para Data Analyst",
        labels={
            "cantidad_ofertas": "Veces solicitada",
            "habilidad_tecnica": "Tecnología"
        }
    )
    st.plotly_chart(fig4, use_container_width=True)
    st.write(
        "Este gráfico muestra las diez tecnologías más demandadas en las ofertas "
        "etiquetadas como **Data Analyst**, ordenadas de mayor a menor frecuencia."
    )

# ── 2) Heatmap de Top 20 combinación Función–Tecnología ──
    query = """
        SELECT
            o.funcion,
            ot.habilidad_tecnica,
            COUNT(*) AS cantidad_ofertas
        FROM oferta_tecnologia ot
        JOIN ofertas o ON ot.id_urls = o.id_urls
        GROUP BY o.funcion, ot.habilidad_tecnica
        ORDER BY cantidad_ofertas DESC
        LIMIT 20;
    """

    db_conectada = conectar_db()
    df_heat = ejecutar_query(query, db_conectada)
    db_conectada.close()

    # Pivot para la matriz
    heatmap_df = (
        df_heat
        .pivot(index="funcion", columns="habilidad_tecnica", values="cantidad_ofertas")
        .fillna(0)
        .astype(int)
    )

    fig5 = px.imshow(
        heatmap_df,
        title="Top 20 Combinaciones Función–Tecnología",
        labels={"x": "Tecnología", "y": "Función", "color": "Veces solicitada"},
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig5, use_container_width=True)
    st.write(
        "El mapa de calor refleja las 20 combinaciones más frecuentes de rol y tecnología, "
        "permitiéndote identificar rápidamente los pares función‑skill más populares."
    )



################################################




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

