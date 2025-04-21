# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 17:16:13 2025

@author: Usuario
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.write("### Probando! Aquí está el visor del máster. Dios, dame paciencia 🙏😅")

df = pd.read_csv(r"C:\Users\Usuario\Documents\GitHub\DAB04RT\df_final.csv")


st.dataframe(df.head())


Contratos = pd.DataFrame(df["Contrato"].value_counts())
Contratos["Contrato"] = Contratos.index
st.dataframe(Contratos)

fig, ax = plt.subplots()
Contratos.plot(kind='bar', ax=ax)

st.pyplot(fig)

