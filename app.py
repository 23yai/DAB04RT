
import streamlit as st
import pandas as pd
import plotly.express as px
from paginacion.landing import page_landing
from paginacion.analisis import page_analisis
from paginacion.comparativa import page_comparativa
from paginacion.SQL_Chart import page_SQL

# Configuración general de la página
# st.set_page_config(  
#     page_title="Visor Ofertas", 
#     page_icon="insertar icono",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )
    
def main():

    # Título de la aplicación
    st.title("JobExplorer: el buscador de Ofertas de Empleo Tecnologico")

    # Carga de datos visto "cache" en la web del programador
    @st.cache_data
    def load_data():
        return pd.read_csv("df_final.csv")

    df = load_data()


    # Barra lateral fija con menú de navegación usando solo Streamlit
    with st.sidebar:
        choice = st.radio(
            "Navegación",
            ("Bienvenidos", "Ofertas de empleo", "Comparador", "SQL Chart"),
            index=0
        )

    # Interpretamos la selección para el enrutado (codigo previo, cuando solo habia 2 paginas)
    if choice.startswith("Bienvenidos"):
        page_landing()
    elif choice == "Ofertas de empleo":
        page_analisis()
    elif choice == "Comparador":
        page_comparativa()
    elif choice == "SQL Chart":
        page_SQL()

# Ejecutamos la página correspondiente
if __name__ == "__main__":
    main()

    