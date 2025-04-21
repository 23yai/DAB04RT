# -*- coding: utf-8 -*-

# pages/01_Landing.py
import streamlit as st

def app():
    st.title("Visor de Ofertas - Bienvenido")
    st.markdown("""
    Esta aplicación te permite explorar oportunidades de empleo en tiempo real.
    Usa el menú lateral para filtrar, comparar y visualizar tus ofertas favoritas.
    """)
    # Ejemplo de tarjeta destacada
    col1, col2, col3 = st.columns(3)
    for col, oferta in zip((col1, col2, col3), ["Oferta A", "Oferta B", "Oferta C"]):
        with col:
            st.card(
                title=oferta,
                text="Empresa X · Full‑stack · Salario: 35k€/año",
                image="https://via.placeholder.com/150"
            )