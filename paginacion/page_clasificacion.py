# pages/06_Clasificacion.py
# DANIEL 

import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

modelo = joblib.load('modelo.pkl')
escalador = joblib.load('escalador.pkl')

def page_clasificacion():
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


    estudios = st.sidebar.slider("Estudios", min_value=0, max_value=1, value=1)
    experiencia = st.sidebar.slider("Años de experiencia", min_value=0, max_value=10, value=3)
    skills = st.sidebar.slider("Skills", min_value=0, max_value=19, value=5)
    tecnologias = st.sidebar.slider("Tecnologías/Aptitudes", min_value=0, max_value=25, value=4)
    vacaciones = st.sidebar.slider("Vacaciones (días)", min_value=10, max_value=40, value=22)
    beneficios = st.sidebar.slider("Beneficios", min_value=0, max_value=17, value=2)
    salario = st.sidebar.slider("Salario (€)", min_value=850, max_value=150000, value=25000)

    nueva_fila = pd.DataFrame([[
        estudios,
        experiencia,
        skills,
        tecnologias,
        vacaciones,
        beneficios,
        salario
    ]], columns=[
        'estudios', 'experiencia', 'skills', 'tecnologias_aptitudes',
        'vacaciones', 'beneficios', 'salario_medio'
    ])

    fila_escalada = escalador.transform(nueva_fila)
    pred = modelo.predict(fila_escalada)[0]
    proba = modelo.predict_proba(fila_escalada)


    st.subheader("Oferta introducida")
    st.dataframe(nueva_fila)

    st.subheader("Resultado de la Clasificación")
    st.markdown(f"**Grupo (cluster) asignado:** {pred}")

    st.subheader("Probabilidades por Grupo")
    proba_df = pd.DataFrame(proba, columns=[f'Grupo {i}' for i in range(proba.shape[1])])
    st.dataframe(proba_df.T.rename(columns={0: 'Probabilidad'}).style.format({'Probabilidad': '{:.2%}'}))

    if pred == 0:
        st.markdown(
            "**Cluster 0 (Ofertas más tradicionales/académicas)**\n\n" 
            "- Requieren estudios formales y más experiencia.\n\n" 
            "- Ofrecen más días de vacaciones.\n\n" 
            "- También piden ciertas tecnologías y aptitudes.\n\n" 
            "- Por lo general no ofrecen beneficios adicionales.\n\n" 
            "- Menor porcentaje de contratos indefinidos.\n\n"  
            "- Hay jornadas de todo tipo, pero la mayoría completa.\n\n" 
            "- Todas las ofertas de este cluster pertenecen a Tecnoempleo.\n\n"
        )
    elif pred == 1:
        st.markdown(
            "**Cluster 1 (Ofertas más orientadas a habilidades o tecnologías que experiencia y con mayor flexibilidad)**\n\n" 
            "- No requieren estudios formales específicos.\n\n" 
            "- No piden tanta experiencia, sino más skills técnicas y tecnologías.\n\n" 
            "- Ofrecen más beneficios.\n\n" 
            "- Son todas a jornada completa.\n\n" 
            "- Un 99% de contratos indefinidos.\n\n"  
            "- Más trabajo en remoto.\n\n" 
            "- Estas ofertas pertenecen a ambos portales de empleo (Manfred y Tecnoempleo).\n\n"
        )





