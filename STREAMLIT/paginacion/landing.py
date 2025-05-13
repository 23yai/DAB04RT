# -*- coding: utf-8 -*-

# pages/01_Landing.py
import streamlit as st
import mysql
import mysql.connector
import pandas as pd
import plotly.express as px
from PIL import Image

def page_landing():
    
    #Muestra la ilustración al ancho de la columna
    col1, col2 = st.columns([1,2])
    
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        img0 = Image.open("assets/landing_illustration.png")
        img0 = img0.resize((1500,1300))
        st.image(img0,caption="Explora ofertas geolocalizadas, tendencias y relaciones.")

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: justify;'>Esta aplicación nos permite explorar y filtrar las oportunidades de empleo mas adecuadas a nuestro perfil. Para ello " \
        "usamos fuentes como tecnoempleo y manfred. El buscador dispone de un menú lateral para acceder a las diferentes opciones de manipulación de datos. Dichas funciones" \
        "permiten al usuario seleccionar la información de su especial interés, comparar y visualizar ofertas de la manera mas interactiva y dinámica. JobExplorer permite:"
        "\n\n-Descubrir oportunidades sobre un mapa interactivo, visualizando la distribución geográfica de las vacantes y encontrando los puestos mas cercanos o estratégicos a su " \
        "ubicación."
        "\n\n-Filtrar al instante por: ciudad, salario anual, tipo de contrato y modalidad (presencial o teletrabajo), experiencia y las tecnologías o aptitudes de su dominio."
        "\n\n-Explorar una tabla detallada donde comparar fácilmente cada oferta: empresa, salario, jornada, requisitos y beneficios."
        "\n\n-Observar tendencias mediante gráficos dinámicos de evolución salarial, tecnologías mas demandadas y ranking de empresas."
        "\n\n-Comparar varias ofertas de forma paralela, para valorar de un vistazo cuál se ajusta mejor a su perfil y preferencias."
        "\n\n-Disfrutar de una experiencia de usuario fluida y atractiva, con menús laterales, botoneras y un diseño que se adapta tanto a escritorio como a móvil.", unsafe_allow_html=True)

    st.markdown("<h2 style= 'text-align:left;'>Funciones y ofertas", unsafe_allow_html=True)
    st.write("A continuación, visualizamos una ilustración gráfica en relación a la cantidad de ofertas de empleo por cargo disponibles en JobExplorer.")

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
    
    query = """SELECT
                    funcion,
                    COUNT(oferta) AS cantidad_ofertas        
                FROM 
                    ofertas
                WHERE funcion IS NOT NULL
                GROUP BY funcion;"""
    db_conectada = conectar_db()
    df_0 = ejecutar_query(query, db_conectada)
    db_conectada.close()
    sele = st.multiselect("Seleccione las funciones de su interés", options= df_0["funcion"].tolist(), default= df_0["funcion"].tolist()[:10])
    df_0_f = df_0[df_0["funcion"].isin(sele)]
    
    fig0 = px.pie(
        data_frame = df_0_f,
        names= "funcion",
        values= "cantidad_ofertas",
        labels={"funcion": "Cargo","cantidad_ofertas": "Total ofertas"},
        hole=0.1)
    st.markdown("<h3 style='text-align: left;'>Ofertas de empleo disponibles", unsafe_allow_html=True)
    st.plotly_chart(fig0)

#Pie de página
    st.markdown("---")
    st.markdown(
        "© 2025 JobExplorer · Todos los derechos reservados · "
        "[Política de Privacidad](#) · "
        "[Términos de Uso](#)"
    )