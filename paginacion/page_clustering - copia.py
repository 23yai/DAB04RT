# pages/06_Clustering.py
import streamlit as st
import pandas as pd
import plotly.express as px

def page_clustering():
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

    # ──────────────────────────────────────────────────────────────
    # 1️⃣ Carga de datos
    @st.cache_data
    def load_data():
        df = pd.read_csv("df_subconjunto_cluster.csv")
        # Aseguramos nombres sencillos
        df.columns = df.columns.str.lower().str.replace(" ", "_")
        return df

    df = load_data()

    # ──────────────────────────────────────────────────────────────
    # 2️⃣ Panel de Filtros en la barra lateral
    st.sidebar.header("🔎 Filtros de Clustering")


    estudios_opt = st.sidebar.selectbox(
        "Requiere estudios:",
        options=["Ambos", "Sí", "No"]
    )

    exp_min, exp_max = st.sidebar.slider(
        "Experiencia (años):",
        int(df.experiencia.min()), int(df.experiencia.max()),
        (int(df.experiencia.min()), int(df.experiencia.max()))
    )

    skills_min, skills_max = st.sidebar.slider(
        "Número de skills:",
        int(df.skills.min()), int(df.skills.max()),
        (int(df.skills.min()), int(df.skills.max()))
    )

    tech_min, tech_max = st.sidebar.slider(
        "Tecnologías/Aptitudes:",
        int(df.tecnologias_aptitudes.min()), int(df.tecnologias_aptitudes.max()),
        (int(df.tecnologias_aptitudes.min()), int(df.tecnologias_aptitudes.max()))
    )

    vac_min, vac_max = st.sidebar.slider(
        "Vacaciones (días):",
        int(df.vacaciones.min()), int(df.vacaciones.max()),
        (int(df.vacaciones.min()), int(df.vacaciones.max()))
    )

    ben_min, ben_max = st.sidebar.slider(
        "Beneficios (#):",
        int(df.beneficios.min()), int(df.beneficios.max()),
        (int(df.beneficios.min()), int(df.beneficios.max()))
    )

    sal_min, sal_max = st.sidebar.slider(
        "Salario medio (€):",
        float(df.salario_medio.min()), float(df.salario_medio.max()),
        (float(df.salario_medio.min()), float(df.salario_medio.max()
        ))
    )

    # ──────────────────────────────────────────────────────────────
    # 3️⃣ Aplicación de filtros
    dff = df.copy()
    if estudios_opt != "Ambos":
        dff = dff[dff.estudios == (1 if estudios_opt == "Sí" else 0)]

    dff = dff[
        (dff.experiencia.between(exp_min, exp_max)) &
        (dff.skills.between(skills_min, skills_max)) &
        (dff.tecnologias_aptitudes.between(tech_min, tech_max)) &
        (dff.vacaciones.between(vac_min, vac_max)) &
        (dff.beneficios.between(ben_min, ben_max)) &
        (dff.salario_medio.between(sal_min, sal_max))
    ]

    st.sidebar.markdown(f"**Ofertas tras filtro:** {len(dff)} registros")

    # ──────────────────────────────────────────────────────────────
    # 4️⃣ Distribución de Clusters
    st.subheader("📈 Distribución de Clusters")
    fig_count = px.histogram(
        dff,
        x="cluster",
        color="cluster",
        title="Número de Ofertas por Cluster",
        labels={"cluster": "Cluster", "count": "Ofertas"}
    )
    st.plotly_chart(fig_count, use_container_width=True)
    st.markdown(
        "Se presenta un histograma que muestra cuántas ofertas pertenecen a cada cluster. El eje X representa los distintos grupos generados por el modelo de clustering y el eje Y indica el recuento de ofertas en cada uno. Esta visualización permite: Evaluar la tamaño relativo de cada cluster, detectar desequilibrios (clusters con muy pocas o muchas ofertas) e identificar si es necesario ajustar el número de clusters o revisar las variables de entrada para lograr una segmentación más equilibrada."
    )

    # ──────────────────────────────────────────────────────────────
    # 5️⃣ Parallel Coordinates para todas las variables
    st.subheader("🔀 Parallel Coordinates")
    vars_para = [
        "experiencia", "skills", "tecnologias_aptitudes",
        "vacaciones", "beneficios", "salario_medio"
    ]
    fig_par = px.parallel_coordinates(
        dff,
        color="cluster",
        dimensions=vars_para,
        color_continuous_scale=px.colors.diverging.Tealrose,
        color_continuous_midpoint=dff.cluster.mean(),
        labels={
            "experiencia": "Años Exp.",
            "skills": "Skills",
            "tecnologias_aptitudes": "Tec/Apt",
            "vacaciones": "Vacaciones",
            "beneficios": "Beneficios",
            "salario_medio": "Salario (€)"
        },
        title="Visualización multidimensional de variables por Cluster"
    )
    st.plotly_chart(fig_par, use_container_width=True, height=600)
    st.markdown(
        "Se trazan líneas paralelas, una por cada oferta, que interceptan un eje para cada variable.Al colorearlas según el cluster, se observa cómo los grupos tienden a ocupar regiones específicas en cada dimensión. Esta vista multivariada resulta idónea para detectar patrones conjuntos —por ejemplo, la combinación de salarios altos con bajas exigencias de experiencia."
    )

    # ──────────────────────────────────────────────────────────────
    # 6️⃣ Scatter Matrix (muestra muestra)
    st.subheader("🔍 Matriz de Dispersión (muestra aleatoria)")
    # para rendimiento, muestreamos 500 puntos
    sample = dff.sample(500, random_state=42) if len(dff) > 500 else dff
    fig_smat = px.scatter_matrix(
        sample,
        dimensions=vars_para,
        color="cluster",
        title="Scatter Matrix de Variables Clustering",
        labels={var: var.title() for var in vars_para}
    )
    st.plotly_chart(fig_smat, use_container_width=True, height=800)
    st.markdown(
        "Se construye una cuadrícula de gráficos de dispersión que compara cada par de variables, coloreando los puntos por cluster. Para optimizar el rendimiento, se muestra una muestra aleatoria de hasta 500 ofertas. Este análisis bivariado permite identificar correlaciones directas o inversas y zonas de solapamiento entre grupos."
    )

########nuevas visualizaciones
#Análisis de Centroides (Heatmap)
#Muestra la media de cada variable por cluster como un mapa de calor, para ver de un vistazo qué distingue a cada grupo.

    with st.expander("🗺️ Heatmap de Centroides"):
        centroids = (
            dff
            .groupby("cluster")[vars_para]
            .mean()
            .round(2)
        )
        fig = px.imshow(
            centroids,
            text_auto=True,
            color_continuous_scale="Viridis",
            title="Centroides promedio por Cluster",
            labels={"x":"Variable", "y":"Cluster", "color":"Valor medio"}
        )
        st.plotly_chart(fig, use_container_width=True, height=400)
        st.markdown(
        "Se emplea un mapa de calor para representar el valor medio de cada variable en cada cluster. Cada fila corresponde a un cluster y cada columna a una variable de entrada (estudios, experiencia, skills, tecnologías/apts, vacaciones, beneficios, salario medio). Los colores indican la magnitud promedio, de modo que resulta inmediato identificar qué características distinguen un cluster de otro."
    )



########nuevas visualizaciones
#Box & Violin Plots por Variable
#Para cada variable, un boxplot o violin que compare su distribución entre clusters.
#Puedes copiar ese patrón para todas las variables (experiencia, skills, …).

    tab1, tab2 = st.tabs(["🎨 Boxplot", "🎻 Violin"])
    for name, func in zip(["Boxplot", "Violin"], [px.box, px.violin]):
        with st.container():
            st.subheader(name + " de Salario Medio")
            fig = func(
                dff,
                x="cluster",
                y="salario_medio",
                color="cluster",
                points="all" if name=="Violin" else False,
                title=f"{name} de Salario Medio por Cluster",
                labels={"cluster":"Cluster","salario_medio":"Salario (€)"}
            )
            st.plotly_chart(fig, use_container_width=True)
            st.markdown(
            "Se utilizan diagramas de caja (boxplot) y de violín (violin plot) para comparar la distribución de cada variable entre clusters. En el boxplot se muestran mediana, cuartiles y posibles valores atípicos; en el violin plot, además, se visualiza la densidad de puntos. Estas gráficas permiten determinar si existen diferencias significativas en, por ejemplo, salario o experiencia entre los grupos."
         )

########nuevas visualizaciones
#PCA 2D / t-SNE
#Proyecta tu espacio 7-D en 2-D para ver la separación real de clusters. Requiere sklearn.

    from sklearn.decomposition import PCA
    from sklearn.manifold import TSNE

    X = dff[vars_para]

    # ▶ PCA
    pca2 = PCA(n_components=2).fit_transform(X)
    df_pca = pd.DataFrame(pca2, columns=["PC1","PC2"])
    df_pca["cluster"] = dff["cluster"].astype(str)

    # ▶ Plot
    st.subheader("🔍 PCA 2D")
    fig = px.scatter(
        df_pca, x="PC1", y="PC2", color="cluster",
        title="PCA 2D de Variables de Clustering",
        labels={"PC1":"Componente 1","PC2":"Componente 2"}
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
            "Se aplica Análisis de Componentes Principales (PCA) para proyectar las siete dimensiones originales en dos componentes ortogonales que retienen la mayor varianza. El diagrama de dispersión resultante coloreado por cluster facilita la evaluación de la separación o solapamiento de los grupos en un espacio bidimensional reducido."
         )

########nuevas visualizaciones
    #Radar Chart de Un Cluster
    #Para analizar un solo cluster en detalle, un radar chart de sus medias:
    import plotly.graph_objects as go

    with st.expander("📡 Radar Chart por Cluster"):
        sel = st.selectbox("Escoge Cluster", sorted(dff.cluster.unique()))
        cent = centroids.loc[sel, :]
        fig = go.Figure(data=go.Scatterpolar(
            r=cent.values,
            theta=vars_para,
            fill='toself',
            name=f"Cluster {sel}"
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True)),
            title=f"Perfil Radar del Cluster {sel}"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(
            "Se genera un gráfico polar (radar) para un cluster seleccionado, en el que cada “brazo” representa una de las variables continuas. La forma resultante ilustra el perfil promedio del grupo, mostrando de manera sintética en qué dimensiones destaca o queda rezagado."
         )



########nuevas visualizaciones
#silhouette Plot
#Para medir la calidad de tu clustering, un silhouette plot:

    from sklearn.metrics import silhouette_samples
    import numpy as np

    with st.expander("📏 Silhouette Score"):
        sil_vals = silhouette_samples(X, dff["cluster"])
        df_sil = dff.copy()
        df_sil["silhouette"] = sil_vals
        fig = px.box(
            df_sil, x="cluster", y="silhouette", color="cluster",
            title="Silhouette Score por Cluster",
            labels={"silhouette":"Silhouette","cluster":"Cluster"}
        )
        st.plotly_chart(fig, use_container_width=True)
        st.write(f"Silhouette medio: {sil_vals.mean():.2f}")
        st.markdown(
            "Se calcula el coeficiente de silueta para cada punto y se visualiza en un boxplot por cluster. Este indicador cuantifica la coherencia interna de los grupos (valores cercanos a 1 indican buena asignación). La silueta media global se muestra como referencia de calidad del clustering."
         )







    
