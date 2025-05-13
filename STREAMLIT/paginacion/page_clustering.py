# pages/06_Clustering.py
# YAIZA 

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def page_clustering():
    st.title("📊 Clustering de Ofertas de Empleo")

    # ─── Introducción ─────────────────────────────────────────────────────────
    st.header("Introducción")
    st.markdown("""
    En esta sección aplicamos **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise)  
    para agrupar las ofertas de empleo, descubrir patrones y facilitar la interpretación de los datos.

    **Ventajas de DBSCAN**  
    - No requiere especificar el número de clústers por adelantado.  
    - Detecta automáticamente outliers o puntos de ruido.
    """)

    st.markdown("""
    **Preparación de Datos y Selección de Parámetros**  
    - Se codificaron variables categóricas a formato numérico.  
    - Se normalizaron con `StandardScaler`.  
    - `eps` y `min_samples` se optimizaron usando gráficas de codo.
    """)

    # ─── Carga de datos ────────────────────────────────────────────────────────
    df_final_clustering = pd.read_csv("C:/Users/Usuario/Documents/GitHub/DAB04RT/STREAMLIT/df_final_clustering.csv")
    st.dataframe(df_final_clustering.head())

    # ─── Selección y escalado ─────────────────────────────────────────────────
    cols_num = ["experiencia", "skills", "vacaciones", "salario_medio"]
    X = (
        df_final_clustering[cols_num]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0)
        .values
    )
    scaler = StandardScaler().fit(X)
    X_scaled = scaler.transform(X)

    # ─── Cálculo Silhouette vs eps ────────────────────────────────────────────
    resultados = []
    for eps in np.arange(0.1, 2.6, 0.05):
        db = DBSCAN(eps=eps, min_samples=14)
        clusters = db.fit_predict(X_scaled)
        n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
        n_noise = list(clusters).count(-1)
        mask = clusters != -1
        if n_clusters > 1 and np.sum(mask) > 1:
            score = silhouette_score(X_scaled[mask], clusters[mask])
        else:
            score = np.nan
        resultados.append([eps, n_clusters, n_noise, score])

    resultados_df = pd.DataFrame(
        resultados,
        columns=["eps", "numero_clusters", "total_outliers", "silhouette"]
    )

    # ─── Gráfica Matplotlib ────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(resultados_df["eps"], resultados_df["silhouette"], marker="o")
    ax.set_xlabel("eps")
    ax.set_ylabel("Silhouette Score")
    ax.set_title("Silhouette Score vs eps")
    st.pyplot(fig)

    # ─── Plotly: Silhouette vs eps ────────────────────────────────────────────
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=resultados_df["eps"],
        y=resultados_df["silhouette"],
        mode="lines+markers",
        name="Silhouette"
    ))
    fig1.update_layout(
        title="Silhouette Score vs eps",
        xaxis_title="eps",
        yaxis_title="Silhouette Score",
        height=400
    )
    st.plotly_chart(fig1, use_container_width=True)

    # ─── Plotly: Número de clusters vs eps ───────────────────────────────────
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=resultados_df["eps"],
        y=resultados_df["numero_clusters"],
        mode="lines+markers",
        name="Clusters"
    ))
    fig2.update_layout(
        title="Número de clusters vs eps",
        xaxis_title="eps",
        yaxis_title="Número de clusters",
        height=400
    )
    st.plotly_chart(fig2, use_container_width=True)

    # ─── Validación Visual ────────────────────────────────────────────────────
    st.header("Validación Visual")
    st.image("assets/imagen2_numclusters.jpg",
             caption="Número de clusters vs eps",
             use_container_width=False,
             width=1000)
    st.image("assets/imagen3_clusters.jpg",
             caption="Clusters identificados por DBSCAN",
             use_container_width=False,
             width=1000)

    # ─── Selección del mejor eps ───────────────────────────────────────────────
    mejor = resultados_df.loc[resultados_df["silhouette"].idxmax()]
    st.markdown(f"""
    **Mejor eps**: {mejor['eps']:.2f}  
    **Silhouette**: {mejor['silhouette']:.3f}  
    **Clusters**: {int(mejor['numero_clusters'])}  
    **Outliers**: {int(mejor['total_outliers'])}
    """)

    # ─── PCA 2D y scatter───────────────────────────────────────────────────────
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    clusters_opt = DBSCAN(eps=mejor['eps'], min_samples=14).fit_predict(X_scaled)
    labels = np.where(clusters_opt == -1, "Outlier",
                      np.where(clusters_opt == 0, "Cluster 1", "Cluster 2"))

    fig3 = px.scatter(
        x=X_pca[:, 0],
        y=X_pca[:, 1],
        color=labels,
        title="Proyección PCA 2D con Clústers",
        labels={"x":"Componente 1", "y":"Componente 2", "color":"Grupo"},
        width=800,
        height=600
    )
    st.plotly_chart(fig3, use_container_width=True)

    # ─── Interpretación ───────────────────────────────────────────────────────
    st.header("Interpretación de Clústers")
    st.markdown("""
    **Distribución de Clústers**  
    - **Cluster 1**: ~25% de las ofertas.  
    - **Cluster 2**: ~75% de las ofertas.  
    - **Outliers**: puntos atípicos.

    **Cluster 1**: formación y experiencia elevadas; más días de vacaciones.  
    **Cluster 2**: énfasis en habilidades; contratos indefinidos y flexibilidad.

    Esta segmentación orienta la estrategia de selección por perfil.
    """)


