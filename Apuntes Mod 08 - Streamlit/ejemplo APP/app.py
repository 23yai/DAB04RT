import streamlit as st
import plotly.express as px
import numpy as np

from modules.ml_func import *
from eda import eda_app
from ml import ml_app
from about import about_app

def main():
    st.set_page_config(**PAGE_CONFIG)

    menu = ["Main App", "Exploratory Data Analysis", "Machine Learning Model", "About"]

    choice = st.sidebar.selectbox(label = "Menu", options = menu, index = 0)

    if choice == "Main App":
        st.subheader(body = "Home :house:")

        st.write("Welcome to the **CO2 Emissions Machine Learning Model Website** made with **Streamlit**.")

        st.markdown("""The data for this project comes from the following website: 
                       [Open Canada](https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64).""")

        st.write("""To use this app just go to the `Exploratory Data Analysis` section to know more about the data that we used to build
                    the Machine Learning models.""")
        
        st.write("""To use the `Machine Learning Model` section you can either use the sliders in the sidebar or upload you own CSV file.""")

        st.warning("""Note: If you are using a CSV file you cannot use the sidebar's sliders to use the model.""")

        df = read_data()

        tab1, tab2, tab3 = st.tabs(["Exploratory Data Analysis", "Machine Learning Model", "Data"])

        fig_scatter = px.scatter(data_frame = df,
                            x          = "Fuel Consumption City",
                            y          = "CO2 Emissions",
                            color      = "Fuel Type",
                            opacity    = 0.5)

        tab1.plotly_chart(figure_or_data = fig_scatter, use_container_width = True)

        fuel_type = tab2.radio(label      = "Select Fuel Type:",
                               options    = df["Fuel Type"].unique(),
                               index      = 0,
                               disabled   = False,
                               horizontal = True)
        
        # Filtrar Datos por fuel_type
        df = df[df["Fuel Type"] == fuel_type]

        X_scaler, y_scaler, model = load_model(fuel_type = fuel_type)

        min_model_year, min_engine_size, min_cylinders, min_fuel_consumption_city = X_scaler.data_min_

        max_model_year, max_engine_size, max_cylinders, max_fuel_consumption_city = X_scaler.data_max_

        min_co2_emissions, max_co2_emissions = y_scaler.data_min_, y_scaler.data_max_

        col1, col2 = tab2.columns([1, 1])

        model_year = col1.slider(label     = "Model Year",
                                min_value = int(min_model_year),
                                max_value = int(max_model_year), 
                                step      = 1)
    
        engine_size = col2.slider(label     = "Engine Size",
                                  min_value = float(min_engine_size),
                                  max_value = float(max_engine_size), 
                                  step      = 0.1)
        
        cylinders = col1.slider(label      = "Cylinders",
                                min_value  = int(min_cylinders),
                                max_value  = int(max_cylinders), 
                                step       = 1)

        fuel_cosumption_city = col2.slider(label     = "Fuel Consumption City",
                                           min_value = float(min_fuel_consumption_city),
                                           max_value = float(max_fuel_consumption_city), 
                                           step      = 0.1)
        
        data = np.array([model_year, engine_size, cylinders, fuel_cosumption_city]).reshape(1, -1)

        # Predicción
        data_scaled = X_scaler.transform(data)

        prediction = model.predict(data_scaled)

        prediction_scaled = y_scaler.inverse_transform(prediction)

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
                                opacity    = 0.4,
                                title      = "Fuel Consumption City v CO2 Emissions")

        fig_point1 = px.scatter(data_frame = df_pred,
                                x          = "Fuel Consumption City",
                                y          = "CO2 Emissions", )
        
        fig_point1.update_traces(marker = {"color" : "red", "size" :10, "symbol" : 21})
        fig_scatter1.add_trace(fig_point1.data[0])
        fig_scatter1.update_layout(xaxis_range = [min_fuel_consumption_city - 1, max_fuel_consumption_city + 1],
                                   yaxis_range = [min_co2_emissions - 1, max_co2_emissions + 1])
        
        tab2.plotly_chart(figure_or_data = fig_scatter1, use_container_width = True)

        tab3.dataframe(df)
        tab3.markdown(body = download_file(df = df), unsafe_allow_html = True)

        if st.button(label = "Are you ready?"):
            st.balloons()

    elif choice == "Exploratory Data Analysis":
        eda_app()

    elif choice == "Machine Learning Model":
        ml_app()

    else:
        about_app()




if __name__ == "__main__":
    main()