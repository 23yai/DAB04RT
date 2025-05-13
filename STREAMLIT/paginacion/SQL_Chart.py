#pages/04_SQL.py

import streamlit as st
import streamlit.components.v1 as components

def page_SQL():
    st.markdown("<h2 'text-align=left'>SQL Chart", unsafe_allow_html=True)
    st.markdown("Este es el diagrama de datos creado a partir de MySQL. Aquí es donde se almacena y organiza la información que da vida a JobExplorer.\n\n Este conjunto de " \
    "tablas destaca una principal en el centro: Ofertas. Esta tabla se relaciona con otras a través de relaciones normalizadas de muchos" \
    " a muchos. Para precisar aún mas la información, se generan tablas adicionales también relacionadas de muchos a muchos, 'N:M', o también conocidas como 'many-to-many'.\n\n Creando estas relaciones, podemos " \
    "dividir y organizar la información de forma mas precisa y manejable mediante consultas. Por ejemplo, existe una" \
    " relación 'many-to-many' entre ofertas y ubicación, lo que significa que una oferta puede tener varias ubicaciones" \
    " y una ubicación puede asociarse a múltiples ofertas. El mismo caso se da en idiomas, empresas y tecnologías y aptitudes por ejemplo.\n\n Esta distribución de los datos permite realizar" \
    " consultas complejas, como filtrar vacantes por compañía, rol, habilidades o tipo de jornada. Además, la base de datos se mantiene en" \
    " constante actualización para reflejar las demandas mas actuales y proporcionar la información mas precisa a nuestros usuarios.")
    
    with open("../DIAGRAMA SQL/SQL.drawio.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=1200, scrolling=True)


#Pie de página
    st.markdown("---")
    st.markdown(
        "© 2025 JobExplorer · Todos los derechos reservados · "
        "[Política de Privacidad](#) · "
        "[Términos de Uso](#)"
    )

