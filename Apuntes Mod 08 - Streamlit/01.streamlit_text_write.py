import streamlit as st

import numpy as np
import pandas as pd
import requests


def main():

    # Title
    st.title("Hello Streamlit App.")

    # Text
    # st.text("Hello World!")
    # st.text("New Line.")
    # name = "Daniel"
    # st.text("Siu.")
    # st.text(f"Hola soy {name}")
    # print("hola soy daniel")

    # # Header
    # st.header("Header1")

    # # Subheader
    # st.subheader("Subheader1")

    # # Markdown
    # st.markdown("# This is markdown.")

    # # Display Colored Text/Boostraps Alert
    # st.success("Siuuuuu.")
    # st.warning("This is not a Siuuuuuu.")
    # st.info("Info about the Siuuuuuu.")
    # st.error("This is a error Siuuuuuu.")
    # st.exception("This is a Siuuuuu exception.")

    # .write()
    # st.write("Normal Text.")
    # st.write("## This is a markdown text")
    # st.write(1 + 2)
    # st.dataframe(dir(st))

    # # Help
    # st.help(range)

    # Display Data
    # df = pd.read_csv(filepath_or_buffer = "sources/AccidentesBicicletas_2021.csv", sep = ";")
    
    # Dinamic Data
    # st.dataframe(df)
    # st.write(df)

    # Static Table
    # st.table(df)

    # Adding Color
    # st.dataframe(df.select_dtypes(include=np.number).style.highlight_max(axis = 0))

    # Display JSON
    endpoint = "https://api.frankfurter.app/latest"
    response = requests.get(url = endpoint)
    st.json(response.json())

    # # Display Code
    # code = """
    # def func():
    #     return x**2
    # """
    # st.code(body = code, language = "python")

    pass

if __name__ == "__main__":
    main()
    