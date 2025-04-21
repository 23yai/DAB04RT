import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from modules.ml_func import *    


def eda_app():

    st.subheader(body = "Exploratory Data Analysis :chart:")

    st.sidebar.markdown("*"*10)
    st.sidebar.markdown("Select `Year`, `Make` and `Vehicle Class` to explore the data.")

    df = read_data()

    # SIDEBAR
    df_sidebar = df.sort_values(by = "Fuel Type").copy()

    ### Model Year
    model_year_options = ["All"] + list(df["Model Year"].unique())
    model_year = st.sidebar.selectbox(label   = "Select Year:",
                                      options = model_year_options,
                                      index   = 0)
    
    df_sidebar = df_sidebar[df_sidebar["Model Year"] == model_year] if model_year != "All" else df_sidebar

    ### Make
    make_options =[f"{k} ({v})" for k, v in df_sidebar["Make"].value_counts().to_dict().items()]
    make = st.sidebar.multiselect(label   = "Select Make:",
                                  options =  make_options,
                                  default = make_options[:10])

    df_sidebar = df_sidebar[df_sidebar["Make"].isin([m.split()[0] for m in make])]
    
    ### Vehicle Class
    vehicle_class_options = ["All"] + [f"{k} ({v})" for k, v in df_sidebar["Vehicle Class"].value_counts().to_dict().items()]
    vehicle_class = st.sidebar.selectbox(label   = "Select Vehicle Class:",
                                         options = vehicle_class_options,
                                         index   = 0)

    df_sidebar = df_sidebar[df_sidebar["Vehicle Class"] == " ".join(vehicle_class.split()[:-1])] if vehicle_class != "All" else df_sidebar

    df_sidebar.reset_index(drop = True, inplace = True)
    
    with st.expander(label = "DataFrame", expanded = False):
        st.dataframe(df_sidebar)
        st.write(f"DataFrame dimensions: {df_sidebar.shape[0]}x{df_sidebar.shape[1]}")

    col1, col2 = st.columns([1, 1])

    # Scatter Plot
    fig_scatter = px.scatter(data_frame = df_sidebar,
                            x          = "Fuel Consumption City",
                            y          = "CO2 Emissions",
                            color      = "Fuel Type",
                            # size       = "Engine Size",
                            #title      = f"{make} Cars - Year: {model_year}",
                            opacity    = 0.5)
    
    fig_scatter.update_layout()
    

    df_group = df_sidebar.groupby(by = "Fuel Type").agg({"Fuel Type" : ["count"]})
    df_group.columns = ["Fuel Type Count"]
    df_group.reset_index(inplace = True)

    # Bar Chart
    fig_bar = px.bar(data_frame = df_group,
                    x          = "Fuel Type Count",
                    y          = "Fuel Type",
                    color      = "Fuel Type",
                    text_auto  = True)
    fig_bar.update_yaxes(categoryorder = "total ascending")
    fig_bar.update_xaxes(title_text = "Total Cars")
    fig_bar.update_yaxes(title_text = "")

    # Pie Chart
    fig_pie = px.pie(data_frame = df_group,
                    names       = "Fuel Type",
                    values      = "Fuel Type Count",
                    color       = df_group.columns[0])
    
    # Violin Plot
    fig_violin = px.violin(data_frame = df_sidebar,
                            x          = "Fuel Consumption City",
                            color      = "Fuel Type", )
    
    # Line Plot
    df_group_line = df[df["Make"].isin([m.split()[0] for m in make])].groupby(by = ["Model Year", "Make"], as_index = False)\
                                                                     .agg({"CO2 Emissions" : ["min", "mean", "max"]})
    df_group_line.columns = ["Model Year", "Make", "min", "mean", "max"]

    fig_line = px.line(data_frame = df_group_line,
                        y          = "mean",
                        x          = "Model Year",
                        color      = "Make",
                        title      = "CO2 Emissions (Avg) per Year")
    
    fig_line.update_xaxes(title_text = "Year")
    fig_line.update_yaxes(title_text = "CO2 Emissions (Avg)")
    
    # Plots
    col1.plotly_chart(figure_or_data = fig_scatter, use_container_width = True)
    col1.plotly_chart(figure_or_data = fig_bar, use_container_width = True)
    col2.plotly_chart(figure_or_data = fig_pie, use_container_width = True)
    col2.plotly_chart(figure_or_data = fig_violin, use_container_width = True)
    st.plotly_chart(figure_or_data = fig_line, use_container_width = True)

    # Subplots
    # fig_subplot = make_subplots(rows = 2, cols = 2, subplot_titles = ("Scatter Plot", "Pie Chart", "Bar Plot", "Violin Plot"),
    #                             specs = [[{"type": "scatter"}, {"type": "pie"}], [{"type": "bar"}, {"type": "violin"}]])
    
    # fig_subplot.add_trace(fig_scatter.data[0], row = 1, col = 1)
    # fig_subplot.add_trace(fig_pie.data[0], row = 1, col = 2)
    # fig_subplot.add_trace(fig_bar.data[0], row = 2, col = 1)
    # fig_subplot.add_trace(fig_violin.data[0], row = 2, col = 2)

    # st.plotly_chart(figure_or_data = fig_subplot, use_container_width = True)


    
    

if __name__ == "__eda_app__":
    eda_app()