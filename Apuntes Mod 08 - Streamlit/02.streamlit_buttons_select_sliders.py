import streamlit as st
import numpy as np
import pandas as pd

def main():
    
    # # Buttons
    # name = "Daniel"

    # if st.button(label = "Submit", key = "submit1"):
    #     st.write(f"{name.upper()}")

    # if st.button(label = "Submit", key = "submit2", type = "primary"):
    #     st.write(f"First Name: {name.title()}")

    # # Radio Buttons
    # status = st.radio(label = "What is your status?",
    #                   options = ("None", "Active", "Inactive"),
    #                   index = 0,
    #                   disabled = False,
    #                   horizontal = True,
    #                   )
    # if status == "Active":
    #     st.success("You are Active.")
    # elif status == "Inactive":
    #     st.warning("You are Inactive.")


    # # CheckBox
    # if st.checkbox(label = "Show/Hide"):
    #     st.text("Showing Something")

    # # Expander
    # with st.expander(label = "DataFrame", expanded = False):
    #     st.dataframe(pd.read_csv("sources/AccidentesBicicletas_2021.csv", sep = ";"))

    # # SelectBox
    # modulos = ["Python", "Matemáticas", "Data Science", "SQL", "ML", "Big Data", "Streamlit"]
    # choice = st.selectbox(label = "Modulo", options = modulos)
    # st.write(f"Modulo: {choice}")

    # # Multiple Selection
    # librerias = ["numpy", "pandas", "random", "datetime", "sklearn"]
    # libreria = st.multiselect(label = "Librerias",
    #                           options = librerias, 
    #                           default = librerias,
    #                           placeholder = "Placeholder",
    #                          )
    # st.write(libreria)

    # # Slider Int, Float, Date
    # age = st.slider(label     = "Age",
    #                 min_value = 1,
    #                 max_value = 100,
    #                 value     = 50,
    #                 step      = 2)
    
    # age = st.slider(label     = "Age",
    #                 min_value = 1.0,
    #                 max_value = 100.0,
    #                 value     = 50.0,
    #                 step      = 0.01)

    # # Select Slider
    # colores = ["Amarillo", "Azul", "Rojo", "Morado", "Verde"]
    # color = st.select_slider(label  = "Choose Color",
    #                          options = colores,
    #                          value = "Morado")

    pass

if __name__ == "__main__":
    main()

