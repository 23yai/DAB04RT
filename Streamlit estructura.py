
# Estructura carpetas (imagenes etc)

# Estructurar la mutilpágina: 
# /mi_proyecto
# ├─ .streamlit/
# │   └─ config.toml
# ├─ app.py
#    assets 
#       imagenes dentro
# └─ paginacion/
#    ├─ landing.py
#    └─ analisis.py
#       comparativa
#       sql_chart



# SPRINT 1 (Mejoras pendientes para el lunes 28 abril)

# 1. Página del comparador. Tiene mucha mejora.
#     1.1 Grafico de radar. Nos proponen este grafico para comparar 2 ofertas, con 2 colores según la oferta.
#     1.2 Comparar puestos genericos. Poder comparar 2 puestos muy similares, por ejemplo "desarrollador back end o full stack" data analitics etc... 
#     MARTES - Ver resumen medio por grupo (las 10 kills que mas se piden de cada grupo, no de las ofertas, sino  aplicar y con un filtro)

# 2. Gráficas (ojo cambiar la contraseña de MySQL para que funcione)
#     2.1 Corregir las gráficas en el notebook llamado "Gráficas_Queries_Def" (hay bastante eje de mejora)
#     2.2 Insertarlas en la pagina stremlit sin errores

# 3. SQL página
#     3.1 Insertamos una imagen de las relaciones de SQL. Nos proponen hacerlo con LowChart o algun grafico mas interactivo desde internet 
#     en sprint 2 hay un doc de pag web para poder hacer los graficos
#     https://app.diagrams.net/

# 4. Visualización
#     Botoneras más atractivas




# MAS ADELANTE:
# SPRINT 2 (presentamos el 6 de mayo)


# Parte 5 - Streamlit
# ● Página Principal: Descripción general del proyecto, breve introducción a las secciones de la app.
# ● Exploratory Data Analysis: En estas páginas se mostrarán las visualizaciones y funcionalidades de las gráficas propuestas en el SPRINT I.
# ● Dashboard en PowerBI: Integrar el dashboard en Streamlit.
# ● Clustering y Clasificación: En estas páginas se expondrán ambos modelos, elmodelo de clustering que agrupa las ofertas de empleo según sus características y
# el modelo de clasificación que clasifica una oferta de empleo a un grupo definido por el modelo de clustering. El usuario puede interactuar con el modelo de clasificación a
# través de inputs en Streamlit. Añadir conclusiones para cada modelo y explicar su funcionalidad.
# ● Base de Datos: Mostrar en esta página la arquitectura de la base de datos implementada en el proyecto, explicando la utilidad de cada tabla y del significado de
# cada columna. Sugerencia: https://app.diagrams.net/
# ● About Us: Información de los integrantes del proyecto, enlaces a LinkedIn y Github.
# ● Definir funciones para cada página y funcionalidad de Streamlit.