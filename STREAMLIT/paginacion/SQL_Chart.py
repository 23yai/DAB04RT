#pages/04_SQL.py

import streamlit as st

def page_SQL():
    st.title("SQL Chart")

    #Muestra la ilustración al ancho de la columna
    st.image(
        "assets/SQL_chart.png",
        caption="My SQL relaciones",
        use_container_width=False,
        width=1500  
    )

    st.markdown("""
    Este gráfico muestra la tabla principal Ofertas (con campos como URL, oferta, empresa, función, jornada, contrato, salario o experiencia) 
                y sus relaciones con tablas normalizadas de Empresas, Funciones, Aptitudes, Idiomas, Ubicaciones, 
                Modalidad (teletrabajo/presencial) y Rango salarial, garantizando la integridad referencial y 
                permitiendo consultas complejas como filtrar vacantes por compañía, rol, skills o tipo de jornada.
    """)

#Pie de página
    st.markdown("---")
    st.markdown(
        "© 2025 JobExplorer · Todos los derechos reservados · "
        "[Política de Privacidad](#) · "
        "[Términos de Uso](#)"
    )

# # paginacion/SQL_Chart.py
# import streamlit as st

# def page_SQL():
#     st.title("Diagrama ER de SQL")
#     flow_chart = """
#     digraph ER {
#       rankdir=LR;
#       node [shape=record, fontname=Helvetica];

#       Ofertas    [label="{Ofertas|id_urls\\lOferta\\lEmpresa\\lFuncion\\lUbicacion\\lContrato\\lSalario\\lExperiencia\\l}"];
#       Ubicacion  [label="{Ubicacion|id_ubicacion\\lubicacion\\l}"];
#       Empresa    [label="{Empresa|id_empresa\\lnombre\\l}"];
#       Funcion    [label="{Funcion|id_funcion\\lfuncion\\l}"];
#       Aptitudes  [label="{Aptitud|id_aptitud\\laptitud\\l}"];

#       Ofertas:Ubicacion -> Ubicacion:id_ubicacion;
#       Ofertas:Empresa   -> Empresa:id_empresa;
#       Ofertas:Funcion   -> Funcion:id_funcion;
#       Ofertas:Aptitudes -> Aptitudes:id_aptitud;
#     }
#     """
#     st.graphviz_chart(flow_chart)
#     st.write(
#       "En este diagrama, **Ofertas** es la tabla central y se relaciona con "
#       "**Ubicacion**, **Empresa**, **Funcion** y **Aptitudes** mediante claves "
#       "foráneas para garantizar integridad referencial."
#     )

