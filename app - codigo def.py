# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""


#EN OTRO NOTEBOOK PROGRAMAR PAG PRINCIPAL Y LA SECUNDARIA.




import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Visor de Ofertas de Empleo Tecnológico")

# Carga de datos
def load_data():
    df = pd.read_csv("df_final.csv")
    return df

df = load_data()


# 


# ofetas de empleo distribuidas geograficamente


#Filtrar las ofertas por ubicación, salario, tipo de contrato, tecnologías requeridas y experiencia
# Filtros en la barra lateral
ubicaciones = st.sidebar.multiselect('Ubicacion', df['Ubicacion'].unique())
salario_min = st.sidebar.slider('Salario mínimo', int(df['Salario'].min()), int(df['Salario'].max()))
contratos = st.sidebar.multiselect('Tipo de contrato', df['Contrato'].unique())
tecnologias = st.sidebar.multiselect('Tecnologías', df['Aptitudes'].unique())
experiencia = st.sidebar.selectbox('Experiencia', df['Experiencia'].unique())

# ESTE PUNTO SIN HACER. Geograficamente columnas 'lat' y 'lon'
#st.map(df[['lat', 'lon']])

# Aplicar filtros
df_filtrado = df[
    (df['Ubicacion'].isin(ubicaciones)) &
    (df['Salario'] >= salario_min) &
    (df['Contrato'].isin(contratos)) &
    (df['Aptitudes'].isin(tecnologias)) &
    (df['Experiencia'] == experiencia)
]

# Filtros
st.sidebar.header("Filtros")
ubicaciones = df['Ubicacion'].dropna().unique()
ubicacion_seleccionada = st.sidebar.multiselect("Ubicacion", ubicaciones, default=ubicaciones)

# Aplicar filtros
df_filtrado = df[df['Ubicacion'].isin(ubicacion_seleccionada)]

# Mostrar tabla
st.subheader("Ofertas de Empleo")
st.dataframe(df_filtrado)

#3 Ver una tabla con información detallada de las ofertas de empleo
st.dataframe(df_filtrado)


#4. Visualizar gráficos interactivos sobre tendencias salariales, tecnologías más demandadas y empresas que más contratan
# Tendencias salariales
fig_salario = px.histogram(df_filtrado, x='Salario', nbins=20, title='Distribución Salarial')
st.plotly_chart(fig_salario)

# Tecnologías más demandadas
fig_tecnologias = px.bar(df_filtrado['Aptitudes'].value_counts().head(10), title='Top 10 Tecnologías')
st.plotly_chart(fig_tecnologias)

# Empresas que más contratan
fig_empresas = px.bar(df_filtrado['Empresa'].value_counts().head(10), title='Top 10 Empresas')
st.plotly_chart(fig_empresas)

#5. Acceder a una ficha detallada de cada oferta que incluya la descripción del puesto, requisitos y beneficios
oferta_seleccionada = st.selectbox('Selecciona una oferta', df_filtrado['Oferta'].unique())
detalles = df_filtrado[df_filtrado['Oferta'] == oferta_seleccionada]

st.write(f"**Empresa:** {detalles['Empresa'].values[0]}")
st.write(f"**Descripción:** {detalles['Texto'].values[0]}")
st.write(f"**Requisitos:** {detalles['Requisito'].values[0]}")
st.write(f"**Beneficios:** {detalles['Beneficios'].values[0]}")


#6. Comparar múltiples ofertas de empleo para evaluar cuál se adapta mejor a mi perfil
ofertas_seleccionadas = st.multiselect('Selecciona ofertas para comparar', df_filtrado['Oferta'].unique())
comparacion = df_filtrado[df_filtrado['Oferta'].isin(ofertas_seleccionadas)]

st.dataframe(comparacion[['Oferta', 'Empresa', 'Salario', 'Ubicacion', 'Contrato']])

#7. Acceder a un dashboard en PowerBI con métricas clave sobre el mercado laboral tecnológico
#sin mirar


#8 Visualizar tendencias de demanda de tecnologías y skills a lo largo del tiempo
#foro de programadores
#df['Fecha_de_publicacion'] = pd.to_datetime(df['Fecha_de_publicacion'])
#tendencias = df.groupby([df['Fecha_de_publicacion'].dt.to_period('M'), 'Aptitudes']).size().reset_index(name='Conteo')

#fig_tendencias = px.line(tendencias, x='Fecha_de_publicacion', y='Conteo', color='Aptitudes', title='Tendencias de Tecnologías')
#st.plotly_chart(fig_tendencias)


#9. Ver un esquema visual de la base de datos para comprender mejor la estructura y fuentes de los datos almacenados
st.image('esquema_base_datos.png', caption='Esquema de la Base de Datos')

#10 Filtrar datos por empresa, sector y ubicación para analizar la competencia y mejorar mis estrategias de captación de talento
empresas = st.sidebar.multiselect('Empresa', df['Empresa'].unique())
sectores = st.sidebar.multiselect('Sector', df['Función'].unique())

df_filtrado = df_filtrado[
    (df_filtrado['Empresa'].isin(empresas)) &
    (df_filtrado['Función'].isin(sectores))
]


#11 Utilizar filtros avanzados para encontrar ofertas de empleo o tendencias de manera eficiente. Puesto arriba. 

#12 Realizar búsquedas rápidas dentro de la tabla de datos para acceder a información específica sin perder tiempo
#Agrega un campo de búsqueda para filtrar la tabla en tiempo real.

# Gráfico de tecnologías más demandadas
st.subheader("Tecnologías Más Demandadas")
# Suponiendo que 'tecnologias_aptitudes' es una lista separada por comas
from collections import Counter
import itertools

tecnologias = df_filtrado['tecnologias_aptitudes'].dropna().apply(lambda x: [i.strip() for i in x.split(',')])
tecnologias_lista = list(itertools.chain.from_iterable(tecnologias))
tecnologias_contador = Counter(tecnologias_lista)
tecnologias_df = pd.DataFrame(tecnologias_contador.items(), columns=['Tecnología', 'Cantidad']).sort_values(by='Cantidad', ascending=False)

fig = px.bar(tecnologias_df.head(10), x='Tecnología', y='Cantidad', title='Top 10 Tecnologías Más Demandadas')
st.plotly_chart(fig)



