import streamlit as st
import numpy as np
import pandas as pd
from modules.ml_func import *
import plotly.express as px
import statsmodels
# pip install statsmodels



def ml_app():
    
    st.subheader(body = "Machine Learning Model :robot_face:")

    st.markdown(body = """From the `Exploratory Data Analysis` section we conclude that there is a linear relationship
                          between _**Fuel Consumption City**_ and _**CO2 Emissions**_.""")
    st.markdown(body = """Use the sidebar to try our models. We have built a model for each type of `Fuel Type`.""")
    
    df = read_data()

    df_metricas = pd.read_csv("sources/metrics.csv")

    st.sidebar.markdown("*"*10)

    uploaded_file = st.sidebar.file_uploader(label = "Upload your input CSV file", type = ["csv"])

    st.sidebar.markdown("*"*10)

    data_input, fuel_type_input = None, None

    if uploaded_file is not None:

        data = pd.read_csv(filepath_or_buffer = uploaded_file)

        # data.columns = ["Fuel Type", "Model Year", "Engine Size", "Cylinders", "Fuel Consumption City"]

        data_input, fuel_type_input = data.iloc[:, 1:], data.iloc[0, 0]

    
    fuel_type = st.sidebar.selectbox(label = "Select Fuel Type",
                                    options = df_metricas["Fuel Type"],
                                    index = 0)

    st.write(fuel_type_input)

    # Modelo y Escaladores

    if fuel_type_input is not None:
        fuel_type = fuel_type_input

    # Filtrar Datos por fuel_type
    df = df[df["Fuel Type"] == fuel_type]

    X_scaler, y_scaler, model = load_model(fuel_type = fuel_type)

    min_model_year, min_engine_size, min_cylinders, min_fuel_consumption_city = X_scaler.data_min_

    max_model_year, max_engine_size, max_cylinders, max_fuel_consumption_city = X_scaler.data_max_

    min_co2_emissions, max_co2_emissions = y_scaler.data_min_, y_scaler.data_max_

    # Sidebar - model_year, engine_size, cylinders, fuel_consumption_city
    model_year = st.sidebar.slider(label     = "Model Year",
                                   min_value = int(min_model_year),
                                   max_value = int(max_model_year), 
                                   step      = 1)
    
    engine_size = st.sidebar.slider(label     = "Engine Size",
                                    min_value = float(min_engine_size),
                                    max_value = float(max_engine_size), 
                                    step      = 0.1)
    
    cylinders = st.sidebar.slider(label      = "Cylinders",
                                  min_value  = int(min_cylinders),
                                  max_value  = int(max_cylinders), 
                                  step       = 1)
    
    fuel_cosumption_city = st.sidebar.slider(label     = "Fuel Consumption City",
                                             min_value = float(min_fuel_consumption_city),
                                             max_value = float(max_fuel_consumption_city), 
                                             step      = 0.1)

    # User Data Input
    data = np.array([model_year, engine_size, cylinders, fuel_cosumption_city]).reshape(1, -1)

    if data_input is not None:

        data = data_input.copy()

    # Predicción
    data_scaled = X_scaler.transform(data)

    prediction = model.predict(data_scaled)

    prediction_scaled = y_scaler.inverse_transform(prediction)

    col1, col2 = st.columns([1, 1])

    # User Data Input - Display
    df_pred = pd.DataFrame(data = data, columns = X_scaler.get_feature_names_out())
    df_pred["CO2 Emissions"] = prediction_scaled
    col1.markdown(body = "User's Input:")
    col1.dataframe(data = df_pred.iloc[:, :-1])

    col2.markdown(body = "User's Prediction:")
    col2.dataframe(data = df_pred.iloc[:, -1])

    # Scatter Plot - Fuel Consumption
    fig_scatter1 = px.scatter(data_frame = df,
                              x          = "Fuel Consumption City",
                              y          = "CO2 Emissions",
                              color      = "Model Year",
                              marginal_x = "violin",
                              opacity    = 0.4,
                              title      = "Fuel Consumption City v CO2 Emissions")

    fig_point1 = px.scatter(data_frame = df_pred,
                            x          = "Fuel Consumption City",
                            y          = "CO2 Emissions", )
     
    fig_point1.update_traces(marker = {"color" : "red", "size" : 10, "symbol" : 21})
    fig_scatter1.add_trace(fig_point1.data[0])
    fig_scatter1.update_layout(xaxis_range = [min_fuel_consumption_city - 1, max_fuel_consumption_city + 1],
                               yaxis_range = [min_co2_emissions - 1, max_co2_emissions + 1])

    # Scatter Plot - Cylinders
    fig_scatter2 = px.scatter(data_frame = df,
                             x          = "Cylinders",
                             y          = "CO2 Emissions",
                             color      = "Engine Size",
                             marginal_y = "box",
                             opacity    = 0.4)

    fig_point2 = px.scatter(data_frame = df_pred,
                            x          = "Cylinders",
                            y          = "CO2 Emissions")
    
    fig_point2.update_traces(marker = {"color" : "red", "size" :10, "symbol" : 21})
    fig_scatter2.add_trace(fig_point2.data[0])


    # Plots
    col1.plotly_chart(figure_or_data = fig_scatter1, use_container_width = True)
    col2.plotly_chart(figure_or_data = fig_scatter2, use_container_width = True)

    # Metricas
    st.markdown(body = f"Para este modelo tenemos las siguiente métricas:")
    st.dataframe(df_metricas[df_metricas["Fuel Type"] == fuel_type].reset_index(drop = True))
    

    # DataFrame
    with st.expander(label = "DataFrame", expanded = False):
        st.dataframe(df)
        st.markdown(body = download_file(df = df, fuel_type = fuel_type), unsafe_allow_html = True)




