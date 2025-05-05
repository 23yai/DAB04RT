# pages/06_Clustering.py
# YAIZA 

import streamlit as st
import pandas as pd
import plotly.express as px

def page_clustering():
    st.title("📊 Clustering de Ofertas de Empleo")

    st.title("Introducción")
    st.markdown(
        "En esta sección se aplicó el algoritmo **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) para agrupar las vacantes y extraer patrones de comportamiento y relaciones entre características similares.\n\n" \
        "El objetivo es identificar segmentos de ofertas con atributos comunes, lo que facilita la interpretación de los datos y la toma de decisiones, por ejemplo, mediante:\n\n"
        "- Descubrimiento de tendencias o patrones ocultos.\n\n"
        "- Segmentación eficaz del mercado laboral para orientar estrategias de reclutamiento.\n\n"

        "Se eligió DBSCAN por sus ventajas:\n\n"
        "- No requiere definir de antemano el número de clusters.\n\n"  
        "- Detecta automáticamente outliers o puntos de ruido.\n\n"

        "Para su correcta aplicación, primero se prepararon los datos:\n\n"
        "- Se codificaron variables categóricas a formato numérico, requisito del algoritmo.\n\n"
        "- Se ajustaron los parámetros `eps` y `min_samples`, apoyándose en gráficas de codo para determinar los valores óptimos.\n\n"

        "**Preparación de Datos y Selección de Parámetros**\n\n"
        "En primer lugar se realizó el preprocesamiento del conjunto de datos: todas las variables categóricas se codificaron a formato numérico para cumplir con los requisitos de entrada de DBSCAN.\n\n" \
        "A continuación, se ajustaron los hiperparámetros clave (`eps` y `min_samples`) apoyándose en gráficas de codo, las cuales aportaron la información necesaria para elegir los valores que optimizan la calidad del clustering.\n\n"

    )

    st.title("Silhouette Score vs Eps")
    st.image(
            "assets/imagen1_silhouette.jpg",
            use_container_width = False,
            width=1200  
        )
    # Añadimos nuestro “caption” como HTML con estilo
    st.markdown(
        """
        <p style="font-size:18px; font-weight:bold; margin: 0;">
        Puntos claves
        </p>
        <p style="font-size:18px; margin-top:8px; color:gray;">
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        </p>
        """,
        unsafe_allow_html=True
    )



    st.title("Número de clusters vs eps")
    st.image(
            "assets/imagen2_numclusters.jpg",
            use_container_width = False,
            width=1200  
        )
    st.markdown(
        """
        <p style="font-size:18px; font-weight:bold; margin: 0;">
        Puntos claves
        </p>
        <p style="font-size:18px; margin-top:8px; color:gray;">
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "Finalmente se ha aplicado DBSCAN.\n\n"
        "Nos muestra mediante un gráfica PCA de 2 dimensiones, como los gráficos se agrupan en 2 clusters o densidades:\n\n"
    )


    st.title("Clusters DBSCAN")
    st.image(
            "assets/imagen3_clusters.jpg",
            use_container_width = False,
            width=1200  
        )
    st.markdown(
        """
        <p style="font-size:18px; font-weight:bold; margin: 0;">
        Puntos claves
        </p>
        <p style="font-size:18px; margin-top:8px; color:gray;">
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "Al ver que claramente los datos están bien diferenciados, se confirma la validez del análisis"
    )

    st.markdown(
        "**Interpretación de los clusters**\n\n" 
        "Tamaño y la proporción de cada cluster:\n\n"
            "- Cluster 0: 25,3% de las ofertas (1.356 ofertas)\n\n"
            "- Cluster 1: 74,7% de las ofertas (4.003 ofertas)\n\n"
    )


    st.title("Dataframe")
    st.image(
            "assets/imagen4_dataframe.jpg",
            use_container_width = False,
            width=1200  
        )
    st.markdown(
        """
        <p style="font-size:18px; font-weight:bold; margin: 0;">
        Puntos claves
        </p>
        <p style="font-size:18px; margin-top:8px; color:gray;">
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "**Cluster 0 (Ofertas más tradicionales/académicas)**\n\n" 
            "- Requieren estudios formales y más experiencia.\n\n" 
            "- Ofrecen más días de vacaciones.\n\n" 
            "- Tambien piden ciertas tecnologías y aptitudes.\n\n" 
            "- Por lo general no ofrecen beneficios adicionales.\n\n" 
            "- Menor porcentaje de contratos indefinidos.\n\n"  
            "- Hay jornadas de todo tipo, pero la mayoría completa.\n\n" 
            "- Todas las ofertas de este cluster pertenecen a tecnoempleo.\n\n"   
    )


    st.markdown(
        "**Cluster 1 (Ofertas más orientadas a habilidades o tecnologías que experiencia y con mayor flexibilidad)**\n\n" 
            "- No requieren estudios formales específicos.\n\n" 
            "- No piden tanta experiencia si no más skills técnicas y tecnologías.\n\n" 
            "- Ofrecen más beneficios.\n\n" 
            "- Son todas a jornada completa.\n\n" 
            "- Un 99% de contratos indefinidos.\n\n"  
            "- Más trabajo en remoto.\n\n" 
            "- Estas ofertas pertenecen a ambos portales de empleo (Manfred y Tecnoempleo).\n\n"   
    )


    st.markdown(
        "**Interpretación del Mercado Laboral**\n\n" 
        "La visualización PCA muestra dos grupos claramente separados:\n\n" 
            "- Cluster 0: Representa ofertas más tradicionales/académicas que valoran la formación formal y la experiencia por encima de aptitudes o skills específicas.\n\n" 
            "- Cluster 1: Representa ofertas más orientadas a habilidades que no necesitan estudios formales pero buscan competencias específicas, y ofrecen mejores condiciones como un contrato indefinido o jornada completa, en resumen mayor estabilidad, beneficios o mayor flexibilidad (remoto).\n\n" 
        "Esta segmentación puede ser muy útil para orientar la búsqueda de empleo según el perfil del candidato."   
    )


