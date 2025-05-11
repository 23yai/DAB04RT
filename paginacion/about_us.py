import streamlit as st
from PIL import Image

def page_aboutus():
    st.markdown("<h2>¿Quiénes somos?", unsafe_allow_html=True)


 # Encabezamiento con nuestra historia
    st.markdown("<h3>Nuestra historia", unsafe_allow_html=True)
    st.markdown("""
    Nos conocimos durante el Máster en Análisis de Datos de Hack a Boss, donde descubrimos que compartíamos la misma pasión por la tecnología y la innovación.
    Fruto de nuestro trabajo conjunto en proyectos de machine learning y visualización de datos, decidimos unir fuerzas para crear JobExplorer, el buscador de empleo tecnológico más completo y avanzado de España. 
    Nuestra misión es conectar a profesionales tech con oportunidades que potencien sus carreras y transformen el mercado laboral.
    """)

    # Perfil de cada uno
    col1, col2, col3, col4, col5 = st.columns(5, gap="large")

    with col1:
        # Foto y nombre
        img1 = Image.open("assets/Daniel_Labella.jpeg")
        img1 = img1.resize((200,240))
        st.image(img1)
        st.subheader("Daniel Labella")
        # Mini reseña
        st.markdown("""
        Ideador en el mundo del Marketing Online, nada se convierte en real sin una idea previa. Intento de emprendedor que no consiguió materializar su "mejor idea" pero que llenó una mochila de aptitudes como son una amplia visión estratégica, creatividad y proactividad.
        """)

        with open("assets/CV - DANIEL LABELLA RAYA.pdf", "rb") as f:
            pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](http://linkedin.com/in/digitalanalyticsanddata)")
        st.markdown("[🐱 GitHub](https://github.com/daninholr?tab=repositories)")

        st.download_button(
            label="📄 Descargar CV",
            data=pdf_bytes,
            file_name="assets/Daniel_Labella_2025.pdf",
            mime="application/pdf",
            key="download_Daniel_cv"
        )

    with col4:
        img2 = Image.open("assets/anthony.jpg")
        img2 = img2.resize((200,240))
        st.image(img2)
        st.subheader("Anthony Díaz")
        st.markdown("""
        Persona comprometida con el trabajo. Me oriento con rapidez e intento ser lo mas efectivo posible. Soy responsable, organizado y disfruto del trabajo en equipo. Me gusta experimentar nuevas experiencias de las que poder aprender y asi ampliar mis recursos y conocimientos.
        """)
        
        with open("assets/CV A.pdf", "rb") as f:
            pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/anthony-d%C3%ADaz-cevallos-bba012339/)")
        st.markdown("[🐱 GitHub](https://github.com/Roronoa273?tab=repositories)")

        st.download_button(
            label="📄 Descargar CV",
            data=pdf_bytes,
            file_name="CVanthony.pdf",
            mime="application/pdf",
            key="download_Anthony_cv"
        )


    with col3:
        img3 = Image.open("assets/mila.jpg")
        img3 = img3.resize((200,240))
        st.image(img3)
        st.subheader("Milagros Castellano")
        st.markdown("""
        Analista de Datos. Gran capacidad para adaptarme a todo tipo de entornos y aportar siempre lo mejor de mí. Me caracterizo por mi facilidad para el trabajo en equipo y mi entusiasmo por aprender y desarrollar mis habilidades. En busca de una oportunidad laboral en la que adquirir más experiencia.
        """)

        with open("assets/CV_MilagrosCastellanoBarbero.pdf", "rb") as f:
            pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/milagros-castellano-barbero/)")
        st.markdown("[🐱 GitHub](https://github.com/Miluette?tab=repositories)")
        st.download_button(
            label="📄 Descargar CV",
            data=pdf_bytes,
            file_name="MilagrosCV.pdf",
            mime="application/pdf",
            key="download_Mila_cv"
        )


    with col2:
        img4 = Image.open("assets/yaiza.rubio.png")
        img4 = img4.resize((200,240))
        st.image(img4)
        st.subheader("Yaiza Rubio Gil")
        st.markdown("""
        Apasionada de la creación y el diseño. Me encanta dar forma a las ideas que se me presentan. Me considero una persona creativa y proactiva y me adapto bien a cualquier situación. Buenas dotes comunicativas.
        """)

        with open("assets/CV Yaiza Diseño.pdf", "rb") as f:
                pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/yaiza-rubio-gil-99b3a0250/)")
        st.markdown("[🐱 GitHub](https://github.com/23yai?tab=repositories)")
        st.download_button(
            label="📄 Descargar CV",
            data=pdf_bytes,
            file_name="YaizaCV.pdf",
            mime="application/pdf",
            key="download_Yaiza_cv"
        )


    with col5:
        img5 = Image.open("assets/Silvia_Lorrio.jpeg")
        img5 = img5.resize((200,240))
        st.image(img5)
        st.subheader("Silvia Lorrio")
        st.markdown("""
        Especialista en Supply Chain, con amplia experiencia en operaciones logísticas y negociación de contratos en LATAM, África, Europa y Oriente Medio. Mi objetivo es seguir impulsando la digitalización, perfeccionar procesos logísticos y liderar proyectos internacionales con un enfoque centrado en el análisis de datos.
        """)

        with open("assets/1. SILVIALORRIO-CV2024-EN.pdf", "rb") as f:
                pdf_bytes = f.read()

        st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/silvialorrio/)")
        st.markdown("[🐱 GitHub](https://github.com/Lorrio-Silvia?tab=repositories)")
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
