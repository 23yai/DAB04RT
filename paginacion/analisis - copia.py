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

    # Mapa con Folium (GEO JASON - DATAFRAME)
    st.subheader("Mapa de ubicaciones. latitud y longitud")
    m = folium.Map(location=[40.4, -3.7], zoom_start=5)
    # for _, row in df_f.iterrows():
    #     folium.Marker(
    #         location=[row["lat"], row["lon"]],
    #         popup=row["Empresa"]
    #     ).add_to(m)
    st_folium(m, width="100%", height=400)

#Skills más solicitadas por funcion
# query = '''SELECT 
#           o.oferta,
#           s.skills        AS skill,
#           COUNT(*)        AS veces
#         FROM ofertas o
#         JOIN oferta_skill os  ON o.id_urls    = os.id_urls
#         JOIN skills        s  ON os.id_skills = s.id_skills
#         GROUP BY o.oferta, s.skills
#         ORDER BY o.oferta, veces DESC;'''

#     db_conectada = conectar_db()
#     df_skills_por_oferta = ejecutar_query(query, db_conectada)
#     db_conectada.close()

    # st.subheader("📋 Conteo de Skills por Oferta")
    # st.dataframe(df_skills_por_oferta, use_container_width=True)

    # st.subheader("🔄 Matriz Oferta vs Skill")
    # pivot_df = (
    #     df_skills_por_oferta
    #     .pivot(index="oferta", columns="skill", values="veces")
    #     .fillna(0)
    #     .astype(int)
    # )
    # st.dataframe(pivot_df, use_container_width=True)

    # # ── 3) Crear la figura agrupada ──
    #     fig_skills = px.bar(
    #         data_frame=df_skills_por_oferta,
    #         x="skill",
    #         y="veces",
    #         color="oferta",
    #         barmode="group",
    #         title="📊 Conteo de Skills por Oferta",
    #         labels={
    #             "skill": "Skill",
    #             "veces": "Veces solicitada",
    #             "oferta": "Oferta"
    #         }
    #     )

    #     # ── 4) Mostrar en Streamlit ──
    #     st.plotly_chart(fig_skills, use_container_width=True)
    #     st.write(
    #         "Esta gráfica muestra cuántas veces aparece cada skill en las distintas ofertas, "
    #         "con barras agrupadas por oferta para facilitar la comparación."
    #     )

##############################################################################################

# De la 224 en adelante, del notebook de gráficas 

    ## Mapa Coroplético: Ofertas de empleo por provincia y salario promedio.

    # fig = px.choropleth(
    #     df_x,
    #     geojson = geojson_data,
    #     locations='ubicacion',  
    #     featureidkey = "properties.name", 
    #     color='cantidad_ofertas',
    #     color_continuous_scale='Tealgrn',
    #     range_color = (0,200),
    #     title='Ofertas de empleo por provincia y su salario promedio',
    #     hover_name = "ubicacion",
    #     hover_data = {"ubicacion":False, "cantidad_ofertas" : True, "salario_promedio": ":.0f"},
    #     labels = {"cantidad_ofertas" : "Ofertas", "salario_promedio": "Salario €"}

    # )
    # fig.update_geos(fitbounds="locations", visible=True)
    # fig.show()


##############################################################################

#Repetir el mismo mapa pero mostrando la media de salario, segmentado por puesto de trabajo

# fig = px.choropleth(
#     df_c,
#     geojson = geojson_data,
#     locations="ubicacion",
#     featureidkey = "properties.name",
#     color='funcion',
#     color_continuous_scale='Viridis',
#     hover_name = "ubicacion",
#     hover_data = ["salario_promedio"],
#     labels = {"ubicacion" : "Ubicacion", "salario_promedio": "Salario €"},
#     title=f'Salario promedio de ocupacion segun la provincia'
    
# )
# fig.update_geos(fitbounds="locations", visible=True)
# fig.show()

#####################################################################

#falta insertar grafica
# # Recreamos la columna ubicación y cambiamos los valores, por unos generales para poder agruparlos


#Pie de página
    st.markdown("---")
    st.markdown(
        "© 2025 JobExplorer · Todos los derechos reservados · "
        "[Política de Privacidad](#) · "
        "[Términos de Uso](#)"
    )