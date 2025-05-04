# pages/05_about_us.py

#mila 
#https://www.linkedin.com/in/milagros-castellano-barbero?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
#yaiza
#http://www.linkedin.com/in/yaiza-rubio-gil-99b3a0250
#Daniel Labella Raya
#http://linkedin.com/in/digitalanalyticsanddata


import streamlit as st

def page_aboutus():
    st.title("¿Quienes somos?")


 # Encabezamiento con nuestra historia
    st.markdown("""
    **Nuestra Historia**\n\n  
    Nos conocimos durante el Máster en Análisis de Datos de Hack a Boss, donde descubrimos que compartíamos la misma pasión por la tecnología y la innovación.\n\n 
    Fruto de nuestro trabajo conjunto en proyectos de machine learning y visualización de datos, decidimos unir fuerzas para crear JobExplorer, el buscador de empleo tecnológico más completo y avanzado de España.\n\n 
    Nuestra misión es conectar a profesionales tech con oportunidades que potencien sus carreras y transformen el mercado laboral.
    """)

    # Perfil de cada uno
    col1, col2, col3, col4, col5 = st.columns(5, gap="large")

    with col1:
        # Foto y nombre
        st.image("assets/claudio_chiappucci.jpeg", width=180)
        st.subheader("Daniel Labella Raya")
        # Mini reseña
        st.markdown("""
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        """)

        ####prueba para poder descargar

        with open("assets/CV - DANIEL LABELLA RAYA.pdf", "rb") as f:
            pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](http://linkedin.com/in/digitalanalyticsanddata)")

        st.download_button(
            label="📄 Descargar CV",
            data=pdf_bytes,
            file_name="assets/Daniel_Labella_2025.pdf",
            mime="application/pdf",
            key="download_Daniel_cv"
        )

    with col2:
        st.image("assets/marco_pantani.jpeg", width=180)
        st.subheader("Anthony")
        st.markdown("""
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        """)
        
        with open("assets/1. SILVIALORRIO-CV2024-EN.pdf", "rb") as f:
            pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](http://www.linkedin.com/in/yaiza-rubio-gil-99b3a0250)")

        st.download_button(
            label="📄 Descargar CV",
            data=pdf_bytes,
            file_name="assets/1. SILVIALORRIO-CV2024-EN.pdf",
            mime="application/pdf",
            key="download_Anthony_cv"
        )


    with col3:
        st.image("assets/gino_bartali.jpeg", width=180)
        st.subheader("Mila")
        st.markdown("""
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        """)

        with open("assets/1. SILVIALORRIO-CV2024-EN.pdf", "rb") as f:
            pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/milagros-castellano-barbero?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app0)")

        st.download_button(
            label="📄 Descargar CV",
            data=pdf_bytes,
            file_name="assets/1. SILVIALORRIO-CV2024-EN.pdf",
            mime="application/pdf",
            key="download_Mila_cv"
        )


    with col4:
        st.image("assets/eddy_merckx.jpeg", width=180)
        st.subheader("Yaiza")
        st.markdown("""
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        """)

        with open("assets/1. SILVIALORRIO-CV2024-EN.pdf", "rb") as f:
                pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](http://www.linkedin.com/in/yaiza-rubio-gil-99b3a025)")

        st.download_button(
            label="📄 Descargar CV",
            data=pdf_bytes,
            file_name="assets/1. SILVIALORRIO-CV2024-EN.pdf",
            mime="application/pdf",
            key="download_Yaiza_cv"
        )


    with col5:
        st.image("assets/miguel_indurain.jpeg", width=180)
        st.subheader("Silvia Lorrio")
        st.markdown("""
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        """)

        with open("assets/1. SILVIALORRIO-CV2024-EN.pdf", "rb") as f:
                pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](falta)")

        st.download_button(
            label="📄 Descargar CV",
            data=pdf_bytes,
            file_name="assets/1. SILVIALORRIO-CV2024-EN.pdf",
            mime="application/pdf",
            key="download_Silvia_cv"
        )
  

    #Pie de página
    st.markdown("---")
    st.markdown(
        "© 2025 JobExplorer · Todos los derechos reservados · "
        "[Política de Privacidad](#) · "
        "[Términos de Uso](#)"
    )


    # #Muestra la ilustración al ancho de la columna
    # st.image(
    #     "assets/claudio_chiappucci.jpeg",
    #     caption="Daniel Labella",
    #     use_container_width=False,
    #     width=200  
    # )


    # #Muestra la ilustración al ancho de la columna
    # st.image(
    #     "assets/marco_pantani.jpeg",
    #     caption="Anthony",
    #     use_container_width=False,
    #     width=200  
    # )

    # #Muestra la ilustración al ancho de la columna
    # st.image(
    #     "assets/gino_bartali.jpeg",
    #     caption="Mila",
    #     use_container_width=False,
    #     width=200  
    # )
    
    # #Muestra la ilustración al ancho de la columna
    # st.image(
    #     "assets/eddy_merckx.jpeg",
    #     caption="Yaiza",
    #     use_container_width=False,
    #     width=200  
    # )
    
    #Muestra la ilustración al ancho de la columna
    # st.image(
    #     "assets/miguel_indurain.jpeg",
    #     caption="Silvia",
    #     use_container_width=False,
    #     width=200  
    # )
    


    #######################################################




