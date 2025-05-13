# -*- coding: utf-8 -*-

# pages/02_Analisis.py
import streamlit as st
import pandas as pd
import folium
import plotly.express as px
from streamlit_folium import st_folium
import mysql
import mysql.connector
from PIL import Image
import datetime
from datetime import date
import json
import requests
from shapely.geometry import shape
import matplotlib.cm as cm
import matplotlib.colors as colors

url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/spain-provinces.geojson"
geojson_data = requests.get(url).json()
geojson_data

def conectar_db(host = "localhost", user = "root", password = "roronoa273", database = "ofertas_empleo"):
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
    st.markdown("<h2 style='text-align: center;'>🔍 Tu próximo empleo empieza aquí", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1,2])
    # Mostramos la ilustración de job cards
    with col1:
        img00 = Image.open("assets/couple_searching_job.png")
        img00 = img00.resize((1500,1100))
        st.image(img00)
    with col2:
        st.subheader("📝 La clave del éxito en tu búsqueda")
        st.markdown(
            "- Utiliza palabras clave relevantes para tu perfil.\n\n"
            "- Selecciona adecuadamente los filtros disponibles.\n\n"
            "- Explora los resultados con atención. \n\n"
            "- Mantén tu CV, o perfil de LinkedIn actualizado y adaptado a cada oferta. \n\n"
            "- Constancia y presencia, revisa ofertas diariamente. \n\n"
            "- Prepara una presentación y simula entrevistas con preguntas comunes del sector. \n\n"
            "- Analiza el resultado obtenido e inscríbete en la oferta de trabajo.\n"
        )
    sustituciones = {
        'A Coruña': 'A Coruña','La Coruña': 'A Coruña','Baleares': 'Illes Balears','Palma': 'Illes Balears','Barcelona': 'Barcelona','Bilbao': 'Bizkaia/Vizcaya','Vizcaya': 'Bizkaia/Vizcaya',
        'Guipúzcoa': 'Gipuzkoa/Guipúzcoa','Álava': 'Araba/Álava','Girona': 'Girona','Madrid': 'Madrid','Valencia': 'València/Valencia','Sevilla': 'Sevilla','Zaragoza': 'Zaragoza','Toledo': 'Toledo',
        'Córdoba': 'Córdoba','Murcia': 'Murcia','Granada': 'Granada','Málaga': 'Málaga','Alicante': 'Alacant/Alicante','Castellón': 'Castelló/Castellón','Lleida': 'Lleida','Cantabria': 'Cantabria',
        'Valladolid': 'Valladolid','Lugo': 'Lugo','Navarra': 'Navarra','Albacete': 'Albacete','Ciudad Real': 'Ciudad Real','Palencia': 'Palencia','Burgos': 'Burgos','Santander': 'Cantabria',
        'Oviedo': 'Asturias','Gijón': 'Asturias','Logroño': 'La Rioja','Vigo': 'Pontevedra','San Sebastián': 'Gipuzkoa/Guipúzcoa','Alcobendas': 'Madrid','Segovia': 'Segovia','Bergondo': 'A Coruña'}

    # Carga de CSV
    df = pd.read_csv("df_final_limpio.csv")
    sal_min = int(df["salario_min"].min())
    sal_max = int((df["salario_max"].max()))
    salario_f = st.sidebar.slider('Filtrar por salario', min_value=sal_min,max_value=sal_max, value=(int((sal_max*0.15)), int((sal_max)*0.35)), step=500) 
    contratos = st.sidebar.multiselect('Tipo de contrato', df['contrato'].unique(), default = ["Indefinido"])
    jornada = st.sidebar.selectbox('Jornada', df['jornada'].unique())

    df["ubicacion"] = df["ubicacion"].apply(lambda x: x if pd.isna(x) else x.split(","))
    df = df.explode("ubicacion").reset_index(drop=True)
    df["ubicacion"] = df["ubicacion"].str.strip()
    df["ubicacion"] = df["ubicacion"].replace(sustituciones)

    ubicaciones = st.sidebar.multiselect('Ubicacion', df['ubicacion'].unique(), default = ["Madrid"])
    mod_teletrabajo = st.sidebar.checkbox("Incluir ofertas en teletrabajo")
    funciones = df["funcion"].unique().tolist()
    sel_fun = st.sidebar.selectbox("Filtra por función", funciones)


    df_f = df[(df["ubicacion"].isin(ubicaciones)) &\
            (df["salario_min"] >= salario_f[0]) &\
            (df["salario_max"] <= salario_f[1]) &\
            (df["contrato"].isin(contratos)) &\
            (df["funcion"] == sel_fun) &\
            (df["jornada"] == jornada)]
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("Una vez adaptados los intereses y capacidades del usuario, JobExplorer presenta una visualización general con las ofertas filtradas. Además, ofrece acceso, con un sencillo click, a las direcciones"
        " URL donde se encuentran publicadas las ofertas, permitiendo al usuario inscribirse fácilmente. Al explorar la página, también puede obtener información relevante sobre dichas ofertas, como el salario por región, "
        " habilidades mas demandadas en el sector, o incluso las empresas mejor remuneradas.")
    if mod_teletrabajo:
        df_f2 = df[(df["ubicacion"] == "Teletrabajo") &\
            (df["salario_min"] >= salario_f[0]) &\
            (df["salario_max"] <= salario_f[1]) &\
            (df["contrato"].isin(contratos)) &\
            (df["funcion"] == sel_fun) &\
            (df["jornada"] == jornada)]
        df_f3 = pd.concat([df_f, df_f2]).drop_duplicates()
        st.dataframe(
                df_f3[["oferta", "empresa", "funcion", "ubicacion", "salario_min", "salario_max"]].reset_index(drop = True),
                use_container_width=True
        )
    else:
        st.dataframe(
                df_f[["oferta", "empresa", "funcion", "ubicacion", "salario_min", "salario_max"]].reset_index(drop = True),
                use_container_width=True
        )
    st.write(f"Total ofertas: {len(df_f3) if mod_teletrabajo else len(df_f)}\n")
        # CheckBox
    if st.checkbox(label = "Pulse para acceder a los enlaces"):
        [st.markdown(f'<a href="{row["id_urls"]}" target="_blank">{row["oferta"]}', unsafe_allow_html=True) for _,row in df_f.iterrows()]


    #######################################################################
    #cantidad de ofertas por ubicacion
    query = '''SELECT 
            u.ubicacion,
            count(o.oferta) AS cantidad_ofertas,
            AVG((o.salario_min + o.salario_max) / 2) AS salario_promedio
        FROM ofertas o
        JOIN ubicacion u ON o.id_ubicacion = u.id_ubicacion
        GROUP BY u.ubicacion
        ORDER BY salario_promedio DESC;'''
    db_conectada = conectar_db()
    df_ubicacion = ejecutar_query(query, db_conectada)
    db_conectada.close()

    sustituciones = {
        'A Coruña': 'A Coruña','La Coruña': 'A Coruña','Baleares': 'Illes Balears','Palma': 'Illes Balears','Barcelona': 'Barcelona','Bilbao': 'Bizkaia/Vizcaya','Vizcaya': 'Bizkaia/Vizcaya',
        'Guipúzcoa': 'Gipuzkoa/Guipúzcoa','Álava': 'Araba/Álava','Girona': 'Girona','Madrid': 'Madrid','Valencia': 'València/Valencia','Sevilla': 'Sevilla','Zaragoza': 'Zaragoza','Toledo': 'Toledo',
        'Córdoba': 'Córdoba','Murcia': 'Murcia','Granada': 'Granada','Málaga': 'Málaga','Alicante': 'Alacant/Alicante','Castellón': 'Castelló/Castellón','Lleida': 'Lleida','Cantabria': 'Cantabria',
        'Valladolid': 'Valladolid','Lugo': 'Lugo','Navarra': 'Navarra','Albacete': 'Albacete','Ciudad Real': 'Ciudad Real','Palencia': 'Palencia','Burgos': 'Burgos','Santander': 'Cantabria',
        'Oviedo': 'Asturias','Gijón': 'Asturias','Logroño': 'La Rioja','Vigo': 'Pontevedra','San Sebastián': 'Gipuzkoa/Guipúzcoa','Alcobendas': 'Madrid','Segovia': 'Segovia','Bergondo': 'A Coruña',}
    
    df_x = df_ubicacion.copy()
    df_x["ubicacion"] = df_x["ubicacion"].apply(lambda x: x.split(","))
    df_x = df_x.explode("ubicacion").reset_index(drop=True)
    df_x["ubicacion"] = df_x["ubicacion"].str.strip()
    df_x["ubicacion"] = df_x["ubicacion"].replace(sustituciones)

    df_ubicacion_1 = df_x.copy()
    df_ubicacion_1 = df_ubicacion_1[df_ubicacion_1["ubicacion"]!= "Teletrabajo"]
    df_ubicacion_1= df_ubicacion_1.groupby("ubicacion", as_index =False).agg({"cantidad_ofertas":"sum"}).nlargest(15, "cantidad_ofertas")

    fig1 = px.bar(
        data_frame = df_ubicacion_1,
        x = "ubicacion",
        y = "cantidad_ofertas",
        labels={"ubicacion": "Ubicación","cantidad_ofertas": "Total ofertas"})
    st.subheader("Ubicaciones con mas ofertas de empleo")
    st.write("El gráfico de barras muestra las diez ubicaciones que concentran el mayor número de ofertas de empleo de nuestro conjunto de datos. En el eje horizontal aparecen las ubicaciones (ciudades o regiones), ordenadas de mayor a menor número de vacantes, y en el eje vertical se indica la cantidad de ofertas publicadas en cada una. " \
    "Gracias a esta visualización se puede identificar rápidamente los mercados laborales más activos y focalizar tu búsqueda en aquellas zonas donde la oferta es más abundante.")
    st.plotly_chart(fig1)

    
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

    df_salario_por_funcion_ubicacion_2 = df_salario_por_funcion_ubicacion.copy()
    df_salario_por_funcion_ubicacion_2 = df_salario_por_funcion_ubicacion_2.groupby(by = "funcion", as_index = False).agg({"salario_promedio" : "mean"})
    df_salario_por_funcion_ubicacion_2 = df_salario_por_funcion_ubicacion_2.sort_values("salario_promedio", ascending = False)
    fig2 = px.bar(data_frame = df_salario_por_funcion_ubicacion_2,
                  x = "funcion",
                  y = "salario_promedio",
                  labels={
                      "funcion":"Ocupación",
                      "salario_promedio":"Salario anual €"})
    st.subheader("Salario en funcion de puesto de trabajo")
    st.write(
        "Este gráfico de barras representa el salario medio anual para cada rol o función disponible, generalizando la ubicación de su demanda. De este modo podemos observar cuál es la ocupación mejor" \
        " remunerada según las ofertas mas actuales y disponibles."
    )
    st.plotly_chart(fig2)

    
    df_x = df_x.groupby("ubicacion", as_index = False).agg({"cantidad_ofertas":"sum", "salario_promedio" : "mean"}).fillna(0)

    prov_coords = []
    for i in geojson_data['features']:
        nombre = i['properties']['name']
        geom = shape(i['geometry'])
        centroid = geom.centroid
        prov_coords.append({"ubicacion": nombre, "lat": centroid.y, "lon": centroid.x})

    df_coords = pd.DataFrame(prov_coords)
    df_mapa = pd.merge(df_x, df_coords, on="ubicacion", how="inner")


    # Mapa con Folium
    st.subheader("Provincias de España")
    st.write("Interactuando con la siguiente visualización podremos observar, pulsando sobre una provincia, el total de ofertas disponibles y, además, la media de salario total.")
    m = folium.Map(location=[40.4, -3.7], zoom_start=5)

    for _, row in df_mapa.iterrows():
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=f"{row["ubicacion"]}: {row["cantidad_ofertas"]} ofertas \n Media salario: {row["salario_promedio"]:.1f} €"
        ).add_to(m)
    st_folium(m, width="100%", height=400)

################################################

    st.subheader(f"Estudio segun cargo de: {sel_fun}")
    st.write("En las siguientes visualizaciones, podremos observar las tecnologías y lenguajes mas solicitados y ademas la media salarial\nen funcion del puesto de trabajo seleccionado.")
    query = '''SELECT
            o.funcion,
            t.tecnologias_aptitudes AS habilidad_tecnica,
            COUNT(*) AS cantidad_ofertas
        FROM
            ofertas o
        JOIN
            oferta_tecnologia ot ON o.id_urls = ot.id_urls
        JOIN
            tecnologias_aptitudes t ON ot.id_tecnologias = t.id_tecnologias
        WHERE o.funcion IS NOT NULL
        GROUP BY
            o.funcion, t.tecnologias_aptitudes
        ORDER BY
            o.funcion, cantidad_ofertas DESC;'''

    db_conectada = conectar_db()
    df_tecnologias_funcion = ejecutar_query(query, db_conectada)
    db_conectada.close()
    df_filtrada = df_tecnologias_funcion[df_tecnologias_funcion["funcion"] == sel_fun]
    st.write(f"Empezando por el próximo gráfico. Para el cargo de {sel_fun}, observamos que las tecnologías mas solicitadas en relación a su demanda son: {", ".join([i for i in df_filtrada.nlargest(3,"cantidad_ofertas")["habilidad_tecnica"]])}.")

    fig4 = px.bar(
        df_filtrada.nlargest(10,"cantidad_ofertas"),
        x="cantidad_ofertas",
        y="habilidad_tecnica",
        orientation="h",
        title=f"Habilidades técnicas mas solicitadas para {sel_fun}",
        labels={
            "cantidad_ofertas": "Número de veces solicitada",
            "habilidad_tecnica": "Tecnología"
        }
    )
    st.plotly_chart(fig4, use_container_width=True)

    st.write(f"Ahora veremos un mapa interactivo de las provincias de España, filtrado por la ocupación seleccionada. Podremos observar dónde hay demanda de {sel_fun}")
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
    df_c = df_salario_por_funcion_ubicacion.copy()
    df_c["ubicacion"] = df_c["ubicacion"].apply(lambda x: x.split(","))
    df_c = df_c.explode("ubicacion").reset_index(drop=True)
    df_c["ubicacion"] = df_c["ubicacion"].str.strip()
    df_c["ubicacion"] = df_c["ubicacion"].replace(sustituciones)
    df_mapa1= pd.merge(df_c, df_coords, on="ubicacion", how="inner")

    pe= folium.Map(location=[40.4, -3.7], zoom_start=5)
    for _, row in df_mapa1[df_mapa1["funcion"] == sel_fun].iterrows():
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=f"{row["ubicacion"]} \n Salario promedio: {row["salario_promedio"]:.1f} €"
        ).add_to(pe)
    st_folium(pe, width="100%", height=400)
    st.write(f"En el cargo de un {sel_fun}, la provincia mejor remunerada es {" ".join(df_mapa1[df_mapa1["funcion"]== sel_fun].nlargest(1,"salario_promedio")["ubicacion"])}, lo deducimos del siguiente gráfico de barras.")
    
    # Vamos a visualizar top 10 ubicaciones mejores pagadas en funcion de su salario promedio por ocupacion
    query =  '''SELECT
            o.funcion,
            u.ubicacion,
            avg((o.salario_min + o.salario_max)/2) AS salario_promedio,
            COUNT(*) AS cantidad_ofertas
        FROM
            ofertas o
        JOIN
            oferta_tecnologia ot ON o.id_urls = ot.id_urls
		JOIN
			ubicacion u ON o.id_ubicacion = u.id_ubicacion
        WHERE funcion IS NOT NULL
        GROUP BY
            o.funcion, u.ubicacion
        ORDER BY
            o.funcion, u.ubicacion, cantidad_ofertas DESC;'''
    db_conectada = conectar_db()
    df_salario_ubicacion_func = ejecutar_query(query, db_conectada)
    db_conectada.close()


    df_f1= df_salario_ubicacion_func.copy()
    df_f1["ubicacion"] = df_f1["ubicacion"].apply(lambda x:x.split(","))
    df_f1 = df_f1.explode("ubicacion").reset_index(drop=True)
    df_f1["ubicacion"] = df_f1["ubicacion"].str.strip()
    df_f1["ubicacion"] = df_f1["ubicacion"].replace(sustituciones)    
    # A partir de ahora, reorganizaremos y reordenaremos los datos, para el siguiente paso, Top 10
    df_f1 = df_f1.groupby(["ubicacion","funcion"],as_index=False).agg({"salario_promedio":"mean", "cantidad_ofertas":"sum"})
    # Barras – Salario promedio por ubicación
    # Mostramos solo el top 10 de ubicaciones con mayor salario y ofertas totales
    df_top10 = df_f1[df_f1["funcion"] == sel_fun].fillna(0)
    df_top10 = df_top10[df_top10["salario_promedio"] > 0]
    df_top10 = df_top10.nlargest(10,"salario_promedio")

    fig7 = px.bar(
        df_top10,
        x = "salario_promedio",
        y = "ubicacion",
        orientation = "h",
        text = "salario_promedio",
        title =f"Ubicaciones mejor remuneradas para un {sel_fun}",
        labels = {"salario_promedio":"Salario €", "ubicacion" : "Ubicacion","cantidad_ofertas": "Ofertas totales"},
        hover_data = {"salario_promedio" : False, "cantidad_ofertas":True, "ubicacion":False})
    fig7.update_traces(texttemplate='%{text:.0f} €')
    fig7.update_layout(
        yaxis={'categoryorder':'total ascending'},
        xaxis_title="Salario €",
        yaxis_title="",
        bargap = 0.2,
        height = 700)
    
    st.plotly_chart(fig7,use_container_width=True)

    query = '''SELECT
			o.funcion,
            t.tecnologias_aptitudes AS habilidad_tecnica,
            COUNT(*) AS cantidad_ofertas
        FROM oferta_tecnologia ot
        JOIN ofertas o ON ot.id_urls = o.id_urls
        JOIN tecnologias_aptitudes t ON ot.id_tecnologias = t.id_tecnologias
        WHERE o.funcion IS NOT NULL AND o.id_ubicacion = 5
        GROUP BY o.funcion, t.tecnologias_aptitudes
        ORDER BY cantidad_ofertas DESC;'''
    db_conectada = conectar_db()
    df_tele  = ejecutar_query(query, db_conectada)
    db_conectada.close()

   # Pivot para la matriz
    heatmap_df1= (
        df_tele[df_tele["funcion"]== sel_fun]
        .pivot(index="funcion", columns="habilidad_tecnica", values="cantidad_ofertas")
        .fillna(0)
        .astype(int)
    )
    heatmap_df1 = heatmap_df1.loc[:, heatmap_df1.loc[sel_fun].sort_values(ascending=False).index]

    fig8=px.imshow(
        heatmap_df1.loc[:, heatmap_df1.loc[sel_fun] > 1],
        title=f"Tecnologías mas solicitadas en Teletrabajo para {sel_fun}",
        labels={"x": "Tecnología", "y": "Función", "color": "Veces solicitada"},
        text_auto=False,
        aspect="auto",
        color_continuous_scale="blues"
    )
    st.plotly_chart(fig8, use_container_width=True)
    
    st.write(f"Podemos observar con este mapa de calor cuál es la habilidad mas demandada en teletrabajo para el puesto de {sel_fun}.")


    st.subheader("Mapa de calor Función-Tecnología")
# ── 2) Heatmap de Top 20 combinación Función–Tecnología ──
    query = """SELECT
            o.funcion,
            t.tecnologias_aptitudes AS habilidad_tecnica,
            COUNT(*) AS cantidad_ofertas
        FROM oferta_tecnologia ot
        JOIN ofertas o ON ot.id_urls = o.id_urls
        JOIN tecnologias_aptitudes t ON ot.id_tecnologias = t.id_tecnologias
        WHERE o.funcion IS NOT NULL
        GROUP BY o.funcion, t.tecnologias_aptitudes
        ORDER BY cantidad_ofertas DESC
        LIMIT 20;
    """

    db_conectada = conectar_db()
    df_heat = ejecutar_query(query, db_conectada)
    db_conectada.close()
    df_heat["habilidad_tecnica"] = df_heat["habilidad_tecnica"].apply(lambda x:x.lower())
    df_heat = df_heat.groupby(["funcion", "habilidad_tecnica"], as_index=False).agg({"cantidad_ofertas":"sum"})
                                    

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
# ── 3) Habilidades solicitadas por año
    st.subheader("Habilidades técnicas y Ocupaciones demandadas según intervalos de tiempo")
    st.write("Con las siguientes visualizaciones podremos apreciar una relación entre los cargos demandados y las habilidades técnicas mas demandadas según un intervalo de tiempo determinado.")
    query = '''SELECT
            o.fecha,
            t.tecnologias_aptitudes AS habilidad_tecnica,
            COUNT(*) AS cantidad_ofertas
        FROM
            ofertas o
        JOIN
            oferta_tecnologia ot ON o.id_urls = ot.id_urls
        JOIN
            tecnologias_aptitudes t ON ot.id_tecnologias = t.id_tecnologias
        GROUP BY
            o.fecha, t.tecnologias_aptitudes
        ORDER BY
            o.fecha, cantidad_ofertas DESC;'''
    db_conectada = conectar_db()
    df_habilidad_fecha = ejecutar_query(query, db_conectada)
    db_conectada.close()
    df_habilidad_fecha["año_mes_dia"] = df_habilidad_fecha["fecha"].dt.strftime("%Y-%m-%d")
    df_habilidad_fecha["habilidad_tecnica"] = df_habilidad_fecha["habilidad_tecnica"].apply(lambda x:x.lower())
    df_habilidad_fecha = df_habilidad_fecha.groupby(["año_mes_dia", "habilidad_tecnica"], as_index = False).agg({"cantidad_ofertas":"sum"})
    rango_fechas = st.date_input("Selecciona un rango de fechas", value=(df_habilidad_fecha["año_mes_dia"].min(), datetime.date.today()))
    fecha_inicio, fecha_fin = rango_fechas
    df_fecha = df_habilidad_fecha[(df_habilidad_fecha["año_mes_dia"] >= str(fecha_inicio)) & (df_habilidad_fecha["año_mes_dia"] <= str(fecha_fin))]
    df_fecha = df_fecha.groupby(["habilidad_tecnica"], as_index = False).agg({"cantidad_ofertas":"sum"})
    fig_bar = px.bar(
        data_frame=df_fecha.nlargest(10,"cantidad_ofertas"),
        x = "cantidad_ofertas",
        y = "habilidad_tecnica",
        orientation = "h",
        title = f"Tecnologías mas solicitadas durante {fecha_inicio} y {fecha_fin}",
        labels = {"habilidad_tecnica":"Tecnología","cantidad_ofertas": "Ofertas totales"},
        hover_data = {"habilidad_tecnica" : False, "cantidad_ofertas":True})
    st.plotly_chart(figure_or_data=fig_bar, use_container_width=True)

    query = '''SELECT
            o.funcion,
            o.fecha,
            u.ubicacion,
            COUNT(*) AS cantidad_ofertas
        FROM
            ofertas o
        JOIN
            ubicacion u ON o.id_ubicacion = u.id_ubicacion
        GROUP BY
            o.funcion, u.ubicacion, o.fecha
        ORDER BY
            o.fecha DESC;'''
    db_conectada = conectar_db()
    df_fechas_ofertas = ejecutar_query(query, db_conectada)
    db_conectada.close()
    df_fechas_ofertas["año_mes_dia"] = df_fechas_ofertas["fecha"].dt.strftime("%Y-%m-%d")
    df_fechas_ofertas["ubicacion"] = df_fechas_ofertas["ubicacion"].apply(lambda x: x.split(","))
    df_fechas_ofertas = df_fechas_ofertas.explode("ubicacion").reset_index(drop=True)
    df_fechas_ofertas = df_fechas_ofertas.groupby(["año_mes_dia", "funcion"], as_index = False).agg({"cantidad_ofertas":"sum"})
    df_fechas_ofertas = df_fechas_ofertas[(df_fechas_ofertas["año_mes_dia"] >= str(fecha_inicio)) & (df_fechas_ofertas["año_mes_dia"] <= str(fecha_fin))]
    df_fechas_ofertas = df_fechas_ofertas.groupby(["funcion"], as_index = False).agg({"cantidad_ofertas":"sum"})
    fig_bar = px.bar(
        data_frame=df_fechas_ofertas.nlargest(10,"cantidad_ofertas"),
        x = "cantidad_ofertas",
        y = "funcion",
        orientation = "h",
        title = f"Cargos mas solicitados durante {fecha_inicio} y {fecha_fin}",
        labels = {"funcion":"Ocupación","cantidad_ofertas": "Ofertas totales"},
        hover_data = {"funcion" : False, "cantidad_ofertas":True})
    st.plotly_chart(figure_or_data=fig_bar, use_container_width=True)
    
################################################

    st.subheader("Visualizaciones de outliers y rangos intercuartílicos")
    #Obtener la media y la desviación estándar de los salarios

    query = '''SELECT
                o.funcion,
                AVG((salario_min + salario_max)/2) AS media_salario,
                STDDEV((salario_min + salario_max)/2) AS std_salario
            FROM ofertas o
            WHERE salario_min IS NOT NULL AND salario_max IS NOT NULL AND funcion IS NOT NULL
            GROUP BY o.funcion;'''

    db_conectada = conectar_db()
    df_media_desviacionstd_salarios = ejecutar_query(query, db_conectada)
    db_conectada.close()

    #obtener los salarios medios de las ofertas
    query = '''SELECT
                funcion,
                (salario_min + salario_max) / 2 AS salario_medio
            FROM ofertas
            WHERE salario_min IS NOT NULL AND salario_max IS NOT NULL AND funcion IS NOT NULL;'''
    db_conectada = conectar_db()
    df_salarios_ofertas = ejecutar_query(query, db_conectada)
    db_conectada.close()
    #Calcular Z-Score por funcion
    df_fin = df_salarios_ofertas.merge(df_media_desviacionstd_salarios, on="funcion", how="left")
    df_fin["z_score"] = (df_fin["salario_medio"]-df_fin["media_salario"]) / df_fin["std_salario"]

    # Marcar como outlier si z_score > 3 o < -3
    df_fin["outlier"] = df_fin["z_score"].abs() > 3
    df_fin["outlier_str"] = df_fin["outlier"].map({True:"Si", False:"No"})


    #Graficar histograma diferenciando outliers
    fig2 = px.histogram(
        df_fin[df_fin["funcion"] == sel_fun],
        x="salario_medio",
        color = "outlier_str",
        nbins = 40,
        barmode = "overlay",
        color_discrete_map = {"No": "skyblue", "Si" : "red"},
        title = f"Distribucion de salarios con deteccion de outliers (Z-Score) para {sel_fun}",
        hover_data = {"salario_medio":True, "outlier_str":False}
    )

    fig2.update_layout(
        xaxis_title = "Salario aprox",
        yaxis_title = "Número de ofertas",
        legend_title = "Outlier")
    st.write(f"En esta representación hemos aplicado un filtro de función interactivo para averiguar outliers por ofertas en función del cargo. Para la \
             función {sel_fun} existen salarios entre {int(df_fin[df_fin["funcion"] == sel_fun]["salario_medio"].quantile(0.25))} € y \
             {int(df_fin[df_fin["funcion"] == sel_fun]["salario_medio"].quantile(0.75))} €. En caso de tener outliers, filtrando en la gráfica podríamos resaltarlos.")
    st.plotly_chart(fig2, use_container_width=True)

################################################
    query = '''SELECT 
                u.ubicacion,
                (o.salario_min + o.salario_max) / 2 AS salario_medio
            FROM ofertas o
            JOIN ubicacion u ON o.id_ubicacion = u.id_ubicacion
            WHERE o.salario_min IS NOT NULL AND o.salario_max IS NOT NULL;'''
    db_conectada = conectar_db()
    df_salario_medio_por_oferta_ubicacion = ejecutar_query(query, db_conectada)
    db_conectada.close()

    df_filt = df_salario_medio_por_oferta_ubicacion.copy()
    df_filt["ubicacion"] = df_filt["ubicacion"].apply(lambda x:x.split(","))
    df_filt = df_filt.explode("ubicacion").reset_index(drop=True)
    df_filt["ubicacion"] = df_filt["ubicacion"].str.strip()
    df_filt["ubicacion"] = df_filt["ubicacion"].replace(sustituciones)
    ubicaciones_disponibles = df_filt["ubicacion"].unique()
    # Aqui creamos un filtro para recoger las ubicaciones que mas registros tengan
    # De esta manera el gráfico quedará mucho mas claro
    top_ubi = df_filt['ubicacion'].value_counts().nlargest(15).index
    df_filt = df_filt[df_filt['ubicacion'].isin(top_ubi)]
    sel_ubicaciones = st.multiselect("Selecciona ubicaciones", ubicaciones_disponibles, default=top_ubi)
    df_filtrat = df_filt[df_filt["ubicacion"].isin(sel_ubicaciones)]
    # Relación Salario/Ubicación: Mostrar la relación entre el salario y la ubicación de la oferta de empleo
    fig3 = px.box(
        df_filtrat[(df_filtrat["salario_medio"] >= salario_f[0]) & (df_filtrat["salario_medio"] <= salario_f[1])],
        x = "ubicacion",
        y = "salario_medio",
        title = "Distribución del salario medio por ubicación",
        labels = {"ubicacion": "Ubicación", "salario_medio":"Salario €"},
        hover_data = df_filt.columns)
    fig3.update_layout(
        xaxis_title = "Ubicación",
        yaxis_title = "Salario €",
        xaxis_tickangle = -45)
    st.plotly_chart(fig3, use_container_width=True)
    st.write("En este gráfico comprendemos al interactuar con las cajas que se muestran por ubicación la siguiente informacion." \
    "Con el Q1 interpretamos cuál es el salario anual mas bajo y habitual, si ademas nos fijamos en el mínimo,"
    " podemos señalar que el 25% de las ofertas de la ubicación observada tienen un salario desde el valor min, hasta el Q1. El Q3 representaría el salario" \
    " habitual mas alto, si observamos también el valor máximo, podemos señalar que el salario anual mas alto puede variar desde el Q3 hasta el valor máximo y" \
    " la mediana sería el anual mas típico de la región señalada.")


################################################
    query = '''SELECT 
        e.empresa,
        salario_medio,
        cantidad_ofertas
    FROM (
        SELECT 
            o.id_empresa,
            AVG((salario_min + salario_max) / 2) AS salario_medio
        FROM ofertas o
        WHERE salario_min IS NOT NULL AND salario_max IS NOT NULL
        GROUP BY o.id_empresa
    ) AS salarios
    JOIN (
        SELECT 
            id_empresa,
            COUNT(id_urls) AS cantidad_ofertas
        FROM ofertas
        GROUP BY id_empresa
    ) AS ofertas_count ON salarios.id_empresa = ofertas_count.id_empresa
    JOIN empresa e ON e.id_empresa = salarios.id_empresa
    ORDER BY cantidad_ofertas DESC;'''
    db_conectada = conectar_db()
    df_salario_medio_por_empresa = ejecutar_query(query, db_conectada)
    db_conectada.close()
    df_empresas_top = df_salario_medio_por_empresa.copy()
    df_empresas_top = df_empresas_top[df_empresas_top["cantidad_ofertas"]>= 30]

    fig9 = px.pie(df_empresas_top, names='empresa', values='cantidad_ofertas', 
             title='Distribución de Ofertas por Empresa')

    # Mostrar gráfico en Streamlit
    st.subheader("Empresas")
    st.write("Con el siguiente gráfico podemos evaluar rápidamente la empresa que mas ofertas de trabajo crea.")
    st.plotly_chart(fig9)
    st.write("Una vez observada la aparición de las empresas en las ofertas de trabajo existentes en nuestra base de datos, puede seleccionar entre las empresas existentes para averiguar el salario" \
    " medio que ofrece a sus trabajadores en base a la ocupación de su total interés.")
    empresa_seleccionada = st.multiselect("Selecciona una empresa", df_salario_medio_por_empresa['empresa'].unique().tolist(), default=df_empresas_top["empresa"].unique().tolist())
    query = '''SELECT 
        salarios.funcion,
        e.empresa,
        salarios.salario_medio,
        ofertas_count.cantidad_ofertas
    FROM (
        SELECT 
            o.funcion,
            o.id_empresa,
            AVG((salario_min + salario_max) / 2) AS salario_medio
        FROM ofertas o
        WHERE salario_min IS NOT NULL AND salario_max IS NOT NULL
        GROUP BY o.id_empresa, o.funcion
    ) AS salarios
    JOIN (
        SELECT 
            id_empresa,
            COUNT(id_urls) AS cantidad_ofertas
        FROM ofertas
        GROUP BY id_empresa
    ) AS ofertas_count ON salarios.id_empresa = ofertas_count.id_empresa
    JOIN empresa e ON e.id_empresa = salarios.id_empresa
    ORDER BY ofertas_count.cantidad_ofertas DESC;'''
    db_conectada = conectar_db()
    df_salario_empresa_funcion = ejecutar_query(query, db_conectada)
    db_conectada.close()
    df_salario_medio_por_empresa1 = df_salario_empresa_funcion.copy()
    func_sel = st.multiselect("Seleccione su ocupación", df_salario_medio_por_empresa1["funcion"].unique().tolist(), default=df_salario_medio_por_empresa1["funcion"].unique().tolist()[:3])
    df_salario_medio_por_empresa1 = df_salario_medio_por_empresa1[(df_salario_medio_por_empresa1["empresa"].isin(empresa_seleccionada)) &
                                                                  (df_salario_medio_por_empresa1["funcion"].isin(func_sel))]
    df_salario_medio_por_empresa1["salario_medio"] = df_salario_medio_por_empresa1["salario_medio"].round(0)
    fig10 = px.bar(df_salario_medio_por_empresa1, x='empresa', y='salario_medio', color='funcion', 
             labels={'salario_medio': 'Salario Medio', 'empresa': 'Empresa', 'cantidad_ofertas':'Ofertas'},
             hover_data={"salario_medio":":.0f", "empresa":True, "cantidad_ofertas":False},
             title='Salario Medio por Empresa y Función')
    # Mostrar gráfico en Streamlit
    st.write("Seleccionados los parámetros, podemos estimar en qué empresa el salario anual de la ocupación escogida es mas elevado")
    st.plotly_chart(fig10)
