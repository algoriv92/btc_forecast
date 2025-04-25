import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("📈 Bitcoin Price Dashboard")

# Función para obtener datos
@st.cache_data
def get_crypto_data(crypto_id="bitcoin", currency="usd", days=90):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"
    params = {"vs_currency": currency, "days": days, "interval": "daily"}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df
    else:
        return None

# Cargar datos
df = get_crypto_data()

if df is not None:
    # Graficar con Plotly
    fig = px.line(df, x="timestamp", y="price", title="Bitcoin Price (USD)")
    st.plotly_chart(fig)
else:
    st.error("Error al obtener los datos.")

# Ejecutar el dashboard con: streamlit run app.py