# pages/03_DetalleComparacion.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def page_comparativa():
    st.title("Comparativa de Ofertas de Empleo")

    # Mostramos la ilustración de job cards
    st.image(
        "assets/data_job_cards_search.png",
        caption="Filtra y compara empleos de datos rápidamente",
        use_container_width=False,
        width=700  
    )
    
    df = pd.read_csv("df_final.csv")

    df_filtrado = buscador_ofertas(df)
    comparador_ofertas(df_filtrado)

    comparador_puestos_genericos(df)

    # Ilustración al final: mujer buscando empleos de datos
    st.image(
        "assets/data_search_woman.png",
        caption="Encuentra tu próximo empleo en datos",
        use_container_width=False,
        width=700
    )


def buscador_ofertas(df):
    # Buscador en oferta y empresa
    query = st.text_input(
        "🔎 Filtra por palabra clave (Oferta o Empresa)",
        placeholder="Ej. Data Analyst, Remoto, Python, Ops Tools, Linux..."
    )
    if query:
        mask = (
            df["oferta"].str.contains(query, case=False, na=False) |
            df["empresa"].str.contains(query, case=False, na=False)
        )
        df_f = df[mask].copy()
    else:
        df_f = df.copy()

    st.write(f"Ofertas encontradas: **{len(df_f)}**")
    st.dataframe(
        df_f[["oferta", "empresa", "funcion", "salario_min", "ubicacion", "jornada", "contrato"]],
        use_container_width=True
    )

    return df_f


def comparador_ofertas(df_filtrado):
    if df_filtrado.shape[0] < 2:
        st.warning("Con el filtro actual no hay suficientes ofertas para comparar.")
        return

    # Crear columna auxiliar para etiquetas únicas
    df_filtrado = df_filtrado.copy()
    df_filtrado["etiqueta"] = df_filtrado["oferta"] + " — " + df_filtrado["empresa"]

    seleccion = st.multiselect(
        "✅ Busca y selecciona hasta dos ofertas para comparar",
        options=df_filtrado["etiqueta"].tolist(),
        max_selections=2
    )

    if len(seleccion) == 2:
        # Filtrar usando la columna auxiliar 'etiqueta'
        df_comparativa = df_filtrado[df_filtrado["etiqueta"].isin(seleccion)].copy()

        # Debug para asegurar lo correcto
        # st.code(df_comparativa[["etiqueta", "salario_min", "salario_max", "experiencia", "vacaciones"]].to_string(index=False))

        st.markdown("### Comparador de ofertas")
        mostrar_comparativa_radar(df_comparativa, df_total=df_filtrado)

    elif seleccion:
        st.info("Busca dos ofertas para ver la comparación.")
    else:
        st.info("🛈 Selecciona alguna oferta arriba para compararla.")


def mostrar_comparativa_radar(df_comparativa, df_total, mostrar_info=True):
    """
    Muestra un gráfico radar comparando 2 ofertas, normalizando con base en todo el dataframe.
    """
    if df_comparativa.shape[0] != 2:
        st.warning("Selecciona exactamente 2 ofertas para ver la comparación.")
        return

    # Columnas a usar y sus etiquetas legibles
    columnas_usadas = ["salario_min", "salario_max", "experiencia", "vacaciones"]
    columnas_legibles = {
        "salario_min": "Salario mínimo (€)",
        "salario_max": "Salario máximo (€)",
        "experiencia": "Experiencia (años)",
        "vacaciones": "Vacaciones (días)"
    }
    categorias = [columnas_legibles[col] for col in columnas_usadas]

    # Asegurar numéricos + relleno de NaN con 0
    df = df_comparativa.copy()
    df_total = df_total.copy()

    # Si quieres debuggear puedes usar st.code para mostrar los valores de ambos
    # st.code(df_comparativa[["oferta", "salario_min", "salario_max", "experiencia", "vacaciones"]].to_string(index=False))

    for col in columnas_usadas:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
        df_total[col] = pd.to_numeric(df_total[col], errors="coerce").fillna(0)

    # Radar: normalizamos con base en todo el df_total
    fig = go.Figure()

    for i, (_, fila) in enumerate(df.iterrows()):
        r_norm = []
        hover_vals = []

        for col in columnas_usadas:
            val_real = fila[col]
            val_min = df_total[col].min()
            val_max = df_total[col].max()

            # Normalización a escala 0-10
            if val_max != val_min:
                val_norm = (val_real - val_min) / (val_max - val_min) * 10
            else:
                val_norm = 0

            r_norm.append(round(val_norm, 2))
            hover_vals.append(f"{columnas_legibles[col]}: {val_real:.2f}")

        fig.add_trace(go.Scatterpolar(
            r=r_norm,
            theta=categorias,
            fill='toself',
            name=fila["oferta"],
            hovertext=hover_vals,
            hoverinfo="text"
        ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
        showlegend=True
    )

    # Mostrar solo el radar si no hay info adicional
    if not mostrar_info:
        st.plotly_chart(fig, use_container_width=True)
        return

    # Visual + texto lateral
    col1, col2 = st.columns([1, 2])
    with col1:
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown("### Información básica de las ofertas comparadas")
        cols = st.columns(2)
        for col, (_, row) in zip(cols, df.iterrows()):
            with col:
                experiencia = f"{int(row['experiencia'])} años" if pd.notna(row['experiencia']) else "No especificada"
                vacaciones = f"{int(row['vacaciones'])} días" if pd.notna(row['vacaciones']) else "No especificadas"
                st.markdown(f"""
                **🧠 Oferta:** {row['oferta']}  
                **🏢 Empresa:** {row['empresa']}  
                **📍 Ubicación:** {row['ubicacion']}  
                **💼 Modalidad:** {row['modalidad']}  
                **🕒 Jornada:** {row['jornada']}  
                **📜 Contrato:** {row['contrato']}  
                **🌐 Idiomas:** {row['idiomas']}  
                **🎯 Experiencia:** {experiencia}  
                **🛫 Vacaciones:** {vacaciones} 
                """)


def comparador_puestos_genericos(df):
    st.markdown("### 🔁 Comparativa por puestos genéricos")

    opciones_puestos = [
        "Frontend", "Backend", "Fullstack", "Data Analyst", "DevOps", "QA", "Product Manager"
    ]
    opciones_nivel = [
        "Cualquiera", "Junior", "Senior"
    ]

    col1, col2 = st.columns(2)
    with col1:
        puesto_1 = st.selectbox("🔹 Primer puesto", opciones_puestos)
        nivel_1 = st.selectbox("Nivel", opciones_nivel, key="nivel_1")
    with col2:
        puesto_2 = st.selectbox("🔸 Segundo puesto", opciones_puestos, index=1)
        nivel_2 = st.selectbox("Nivel", opciones_nivel, key="nivel_2")

    # Selector de tipo de comparación
    modo = st.radio("🔍 ¿Qué comparar?", ["Media", "Valor máximo", "Percentil 75"], horizontal=True)

    def filtrar(df, puesto, nivel):
        # Filtro base por puesto
        mask = df["oferta"].str.contains(puesto, case=False, na=False)
        # Filtro adicional por nivel si no es "Cualquiera"
        if nivel != "Cualquiera":
            mask &= df["oferta"].str.contains(nivel, case=False, na=False)
        return df[mask]

    grupo_1 = filtrar(df, puesto_1, nivel_1)
    grupo_2 = filtrar(df, puesto_2, nivel_2)

    if grupo_1.empty or grupo_2.empty:
        st.warning("Uno de los grupos no tiene resultados. Intenta con otros filtros.")
        return

    columnas = ["salario_min", "salario_max", "experiencia", "vacaciones"]

    if modo == "Media":
        resumen_1 = grupo_1[columnas].mean(numeric_only=True)
        resumen_2 = grupo_2[columnas].mean(numeric_only=True)
    elif modo == "Valor máximo":
        resumen_1 = grupo_1[columnas].max(numeric_only=True)
        resumen_2 = grupo_2[columnas].max(numeric_only=True)
    else:  # Percentil 75
        resumen_1 = grupo_1[columnas].quantile(0.75)
        resumen_2 = grupo_2[columnas].quantile(0.75)

    comparativa = pd.DataFrame([resumen_1, resumen_2])
    etiqueta_1 = f"{puesto_1} ({nivel_1})" if nivel_1 != "Cualquiera" else puesto_1
    etiqueta_2 = f"{puesto_2} ({nivel_2})" if nivel_2 != "Cualquiera" else puesto_2
    comparativa["oferta"] = [etiqueta_1, etiqueta_2]
    comparativa.set_index("oferta", inplace=True)

    st.markdown(f"🔍 Ofertas encontradas: **{len(grupo_1)}** vs **{len(grupo_2)}**")

    mostrar_comparativa_radar(comparativa.reset_index(), df_total=df, mostrar_info=False)

    with st.expander("📊 Ver resumen medio por grupo"):
        st.dataframe(comparativa)