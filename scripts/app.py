import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

# Cargar datos
def load_csv(filename):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 🛠️ 2 niveles hacia arriba
    data_path = os.path.join(base_dir, "data", filename)
    return pd.read_csv(data_path, parse_dates=["date"])

# Función para graficar precios diarios
def plot_daily(df):
    df["sma_7"] = df["price"].rolling(window=7).mean()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_facecolor('#111111')
    fig.patch.set_facecolor('#111111')

    is_bullish = df["price"].iloc[-1] > df["price"].iloc[0]
    line_color = '#00FF7F' if is_bullish else '#FF4C4C'

    ax.plot(df["date"], df["price"], color=line_color, linewidth=2.5, label="Precio BTC")
    ax.plot(df["date"], df["sma_7"], color="#1E90FF", linestyle="--", linewidth=2, label="SMA 7 días")

    ax.tick_params(axis='x', colors='white', labelsize=9)
    ax.tick_params(axis='y', colors='white', labelsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#444444')
    ax.spines['bottom'].set_color('#444444')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
    plt.xticks(rotation=45)
    ax.set_title("Bitcoin - Últimos 30 días", fontsize=14, color='white', pad=15)

    legend = ax.legend(loc="upper left", fontsize=10)
    for text in legend.get_texts():
        text.set_color("white")

    plt.tight_layout()
    st.pyplot(fig)

# Función para graficar precios intradía
def plot_hourly(df):
    df["sma_24h"] = df["price"].rolling(window=24).mean()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_facecolor('#111111')
    fig.patch.set_facecolor('#111111')

    ax.plot(df["date"], df["price"], color="#00FF7F", linewidth=2.0, label="Precio BTC (1H)")
    ax.plot(df["date"], df["sma_24h"], color="#1E90FF", linestyle="--", linewidth=2, label="SMA 24h")

    ax.tick_params(axis='x', colors='white', labelsize=8)
    ax.tick_params(axis='y', colors='white', labelsize=8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#444444')
    ax.spines['bottom'].set_color('#444444')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b %Hh'))
    plt.xticks(rotation=45)
    ax.set_title("Bitcoin - Última semana (1H)", fontsize=14, color='white', pad=15)

    legend = ax.legend(loc="upper left", fontsize=10)
    for text in legend.get_texts():
        text.set_color("white")

    plt.tight_layout()
    st.pyplot(fig)

# Streamlit App
st.set_page_config(page_title="BTC Forecast", layout="wide")

st.title("📈 BTC Forecast Dashboard")
st.markdown("Visualiza la evolución reciente de Bitcoin en dos modos distintos:")

mode = st.selectbox("Selecciona el modo de visualización:", ("Últimos 30 días (diario)", "Última semana (1H)"))

if mode == "Últimos 30 días (diario)":
    df_daily = load_csv("btc_prices.csv")
    plot_daily(df_daily)
else:
    df_hourly = load_csv("btc_hourly.csv")
    plot_hourly(df_hourly)
