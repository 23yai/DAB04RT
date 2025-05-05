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
        st.image("assets/Daniel_Labella.jpeg", width=180)
        st.subheader("Daniel Labella Raya")
        # Mini reseña
        st.markdown("""
        Ideador en el mundo del Marketing Online, nada se convierte en real sin una idea previa. Intento de emprendedor que no consiguió materializar su "mejor idea" pero que llenó una mochila de aptitudes como son una amplia visión estratégica, creatividad y proactividad.
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

    with col4:
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
        st.image("assets/mila.jpg", width=180)
        st.subheader("Milagros Castellano Barbero")
        st.markdown("""
        Analista de Datos. Gran capacidad para adaptarme a todo tipo de entornos y aportar siempre lo mejor de mí. Me caracterizo por mi facilidad para el trabajo en equipo y mi entusiasmo por aprender y desarrollar mis habilidades. En busca de una oportunidad laboral en la que adquirir más experiencia
        """)

        with open("assets/CV_MilagrosCastellanoBarbero.pdf", "rb") as f:
            pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/milagros-castellano-barbero?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app0)")

        st.download_button(
            label="📄 Descargar CV",
            data=pdf_bytes,
            file_name="assets/1. SILVIALORRIO-CV2024-EN.pdf",
            mime="application/pdf",
            key="download_Mila_cv"
        )


    with col2:
        st.image("assets/yaiza.rubio.png", width=180)
        st.subheader("Yaiza Rubio Gil")
        st.markdown("""
        Apasionada de la creación y el diseño. Me encanta dar forma a las ideas que se me presentan. Me considero una persona creativa y proactiva y me adapto bien a cualquier situación. Buenas dotes comunicativas.
        """)

        with open("assets/CV Yaiza Diseño.pdf", "rb") as f:
                pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/yaiza-rubio-gil-99b3a0250/)")

        st.download_button(
            label="📄 Descargar CV",
            data=pdf_bytes,
            file_name="assets/1. SILVIALORRIO-CV2024-EN.pdf",
            mime="application/pdf",
            key="download_Yaiza_cv"
        )


    with col5:
        st.image("assets/Silvia_Lorrio.jpeg", width=180)
        st.subheader("Silvia Lorrio Olangua")
        st.markdown("""
        Especialista en Supply Chain, con amplia experiencia en operaciones logísticas y negociación de contratos en LATAM, África, Europa y Oriente Medio. Mi objetivo es seguir impulsando la digitalización, perfeccionar procesos logísticos y liderar proyectos internacionales con un enfoque centrado en el análisis de datos.
        """)

        with open("assets/1. SILVIALORRIO-CV2024-EN.pdf", "rb") as f:
                pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/silvialorrio/)")

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




