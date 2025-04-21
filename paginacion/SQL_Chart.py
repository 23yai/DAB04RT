# pages/04_SQL.py

import streamlit as st

def page_SQL():
    st.title("SQL Chart")

    #Muestra la ilustración al ancho de la columna
    st.image(
        "assets/SQL_chart.png",
        caption="My SQL relaciones",
        use_container_width=False,
        width=1500  
    )

    st.markdown("""
    Este gráfico muestra la tabla principal Ofertas (con campos como URL, oferta, empresa, función, jornada, contrato, salario o experiencia) 
                y sus relaciones con tablas normalizadas de Empresas, Funciones, Aptitudes, Idiomas, Ubicaciones, 
                Modalidad (teletrabajo/presencial) y Rango salarial, garantizando la integridad referencial y 
                permitiendo consultas complejas como filtrar vacantes por compañía, rol, skills o tipo de jornada.
    """)

