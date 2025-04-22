# -*- coding: utf-8 -*-

# pages/01_Landing.py
import streamlit as st

def page_landing():
    #st.title("Bienvenido a JobExplorer")

    #Muestra la ilustración al ancho de la columna
    st.image(
        "assets/landing_illustration.png",
        caption="Explora ofertas geolocalizadas y sus tendencias",
        use_container_width=False,
        width=700  
    )

    st.markdown("""
    Esta aplicación te permite explorar oportunidades de empleo en tiempo real.
                
    Usa el menú lateral para acceder a las difetentes páginas. Podrás filtrar, comparar y visualizar tus ofertas favoritas.
                
    Con nosotros podrás:
                
    -Descubrir oportunidades sobre un mapa interactivo, visualizando la distribución geográfica de las vacantes y encontrando los puestos más cercanos o estratégicos a tu ubicación.
                
    -Filtrar al instante por ciudad, rango salarial, tipo de contrato, modalidad (presencial o teletrabajo), experiencia y las tecnologías o skills que dominas.
                
    -Explorar una tabla detallada donde comparar fácilmente cada oferta: empresa, salario, jornada, requisitos y beneficios.
                
    -Observar tendencias mediante gráficos dinámicos de evolución salarial, tecnologías más demandadas y ranking de empresas que más contratan.
                
    -Comparar varias ofertas de forma paralela, para valorar de un vistazo cuál se ajusta mejor a tu perfil y preferencias.
                
    -Disfrutar de una experiencia de usuario fluida y atractiva, con menús laterales, botoneras y un diseño que se adapta tanto a escritorio como a móvil.
    """)

    # st.title("Lo dejo para después, Insertar 1 grafica¿? Resto en segunda pagina")

    #Muestra la ilustración al ancho de la columna
    # st.image(
    #     "assets/landing_illustration.png",
    #     caption="Explora ofertas geolocalizadas y sus tendencias",
    #     use_container_width=False,
    #     width=300  
    # )


    #Muestra la ilustración al ancho de la columna
    st.image(
        "assets/data_job_cards_search2.png",
        caption="En nuestro menú Comparador, busca y compara ofertas a la vez.",
        use_container_width=False,
        width=500  
    )
