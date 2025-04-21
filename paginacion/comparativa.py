# pages/03_DetalleComparacion.py

import streamlit as st
import pandas as pd

def page_comparativa():
    st.title("Comparativa de Ofertas de Empleo")

    # Mostramos la ilustración de job cards
    st.image(
        "assets/data_job_cards_search.png",
        caption="Filtra y compara empleos de datos rápidamente",
        use_container_width=False,
        width=700  
    )
    
    # Cargo y normalizo columnas
    df = pd.read_csv("df_final.csv")
    # df.columns = (
    #     df.columns
    #       .str.strip()
    #       .str.lower()
    #       .str.replace(" ", "_")
    #       .str.replace("ó", "o")
    #       .str.replace("í", "i")
    #       .str.replace("á", "a")
    #       .str.replace("é", "e")
    #       .str.replace("ú", "u")
    # )

    # 2Muestro en pantalla las columnas disponibles (opcional, para debug)
    # st.write("Columnas:", df.columns.tolist())

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

    # Selección para comparar (hasta 2)
    etiquetas = df_f["oferta"] + " — " + df_f["empresa"]
    seleccion = st.multiselect(
        "✅ Busca y selecciona hasta dos ofertas para comparar",
        options=etiquetas,
        max_selections=2
    )

    # Render de comparación lado a lado
    if len(seleccion) == 2:
        # obtengo los dos índices
        idxs = [etiquetas[etiquetas == s].index[0] for s in seleccion]
        comparativa = df_f.iloc[idxs]

        cols = st.columns(2)
        for col, (_, row) in zip(cols, comparativa.iterrows()):
            with col:
                st.write(f"Oferta: {row["oferta"]}\n\nEmpresa: {row["empresa"]}\n\nFuncion: {row["funcion"]}\n\nSalario: {row["salario_min"]}\n\nUbicacion: {row["ubicacion"]}\n\nJornada: {row["jornada"]}\n\nContrato: {row["contrato"]}"
                                     
                        # f"**empresa:** {row['empresa']}\n\n"
                        # f"**función:** {row['funcion']}\n\n"
                        # f"**salario:** {row['salario_min']}\n\n"
                        # f"**ubicación:** {row['ubicacion']}\n\n"
                        # f"**jornada:** {row['jornada']}\n\n"
                        # f"**contrato:** {row['contrato']}"
                    )
                
    elif seleccion:
        st.info("Busca dos ofertas para ver la comparación.")
    else:
        st.write("🛈 Selecciona alguna oferta arriba para compararla.")
    



    # Ilustración al final: mujer buscando empleos de datos
    st.image(
        "assets/data_search_woman.png",
        caption="Encuentra tu próximo empleo en datos",
        use_container_width=False,
        width=700
    )



#PRIMER INTENTO DE TODOS....


# import streamlit as st
# import pandas as pd

# def page_comparativa():
#     st.title("Vista Detallada y Comparador")
#     st.markdown(
#         "Busca una oferta concreta y compara hasta dos anuncios seleccionados."
#     )

#     # 1️Cargar datos
#     df = pd.read_csv("df_final.csv")

#     # 2️Buscador de texto libre en la columna 'Oferta' y/o 'Empresa'
#     query = st.text_input(
#         "Escribe palabras clave para buscar",
#         placeholder="Ej. Data Analyst, Remoto, Python, Software"
#     )
#     if query:
#         mask = df["oferta"].str.contains(query, case=False, na=False) | \
#                df["empresa"].str.contains(query, case=False, na=False)
#         df_filtrado = df[mask]
#     else:
#         df_filtrado = df.copy()

#     st.write(f"Ofertas encontradas: **{len(df_filtrado)}**")
#     st.dataframe(df_filtrado[[
#         "oferta","empresa","función","salario_min","ubicacion"
#     ]], use_container_width=True)

#     # Selección para comparar (hasta 2)
#     opciones = df_filtrado["oferta"] + " — " + df_filtrado["empresa"]
#     seleccion = st.multiselect(
#         "Selecciona hasta dos ofertas para comparar",
#         options=opciones,
#         max_selections=2
#     )  # :contentReference[oaicite:0]{index=0}&#8203;:contentReference[oaicite:1]{index=1}

#     # 4️ Mostrar comparación lado a lado
#     if len(seleccion) == 2:
#         idx1 = opciones[opciones == seleccion[0]].index[0]
#         idx2 = opciones[opciones == seleccion[1]].index[0]
#         row1, row2 = df_filtrado.loc[idx1], df_filtrado.loc[idx2]

#         cols = st.columns(2)
#         for col, row in zip(cols, (row1, row2)):
#             with col:
#                 st.card(
#                     title=row["oferta"],
#                     text=(
#                         f"**empresa:** {row['empresa']}\n\n"
#                         f"**función:** {row['función']}\n\n"
#                         f"**salario_min:** {row['salario_min']}\n\n"
#                         f"**ubicación:** {row['ubicacion']}\n\n"
#                         f"**jornada:** {row['jornada']}\n\n"
#                         f"**contrato:** {row['contrato']}"
#                     )
#                 )
#     elif seleccion:
#         st.info("Selecciona dos ofertas para ver la comparación completa.")
#     else:
#         st.write("Selecciona alguna oferta arriba para compararla.")