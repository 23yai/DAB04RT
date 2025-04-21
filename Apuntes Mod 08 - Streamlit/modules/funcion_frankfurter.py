import requests
import numpy as np
import pandas as pd
from datetime import datetime

def extraer_datos(currency, year):

    url = "https://api.frankfurter.app"

    date_1 = f"{year}-01-01"

    date_2 = f"{year}-12-31"

    endpoint = f"{url}/{date_1}..{date_2}?to={currency}"

    data = requests.get(url = endpoint).json()

    fechas = list(data["rates"].keys())
    fechas = [datetime.strptime(fecha, "%Y-%m-%d") for fecha in fechas]

    moneda = [data["rates"][fecha][currency] for fecha in data["rates"].keys()]

    df = pd.DataFrame(data = np.array([fechas, moneda]).T,
                      columns = ["date", "currency"])
    
    return df