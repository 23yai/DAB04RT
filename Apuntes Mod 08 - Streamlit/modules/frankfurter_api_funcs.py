import streamlit as st
import requests
import pandas as pd
import numpy as np
from datetime import datetime

@st.cache_data
def get_currency_data(currency, year):

    url = "https://api.frankfurter.app"

    date = f"{year}-01-01"

    if year != datetime.now().year:
            
        date_ = f"{year}-12-31"
        
        endpoint = f"{url}/{date}..{date_}?to={currency}"
        
    else:
        
        endpoint = f"{url}/{date}..?to={currency}"

    data = requests.get(url = endpoint).json()

    fechas = list(data["rates"].keys())
    fechas = [datetime.strptime(fecha, "%Y-%m-%d") for fecha in fechas]

    moneda = [data["rates"][fecha][currency] for fecha in data["rates"].keys()]

    df = pd.DataFrame(data = np.array([fechas, moneda]).T,
                      columns = ["date", "currency"])
    
    return df
