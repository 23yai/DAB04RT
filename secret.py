# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 18:06:27 2025

@author: Usuario
"""

import streamlit as st

# Leer valores desde st.secrets
db_user = st.secrets["database"]["user"]
db_password = st.secrets["database"]["password"]
db_host = st.secrets["database"]["host"]
db_name = st.secrets["database"]["name"]

# Mostrar datos (sólo para pruebas, quita esto luego)
st.write("Usuario:", db_user)
st.write("Host:", db_host)

# Aquí podrías usar los valores para conectar a la base de datos
# por ejemplo con SQLAlchemy, psycopg2, pymysql, etc.
