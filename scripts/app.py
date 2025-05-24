import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.graph_objects as go
import os

# Cargar datos
def load_csv(filename):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "data", filename)
    return pd.read_csv(data_path, parse_dates=["date"])

# Función para graficar precios diarios
def plot_daily(df):
    df["sma_7"] = df["price"].rolling(window=7).mean()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["date"], y=df["price"],
        mode='lines',
        name='Precio BTC',
        line=dict(color='#00FF7F', width=2)
    ))

    fig.add_trace(go.Scatter(
        x=df["date"], y=df["sma_7"],
        mode='lines',
        name='SMA 7 días',
        line=dict(color='#1E90FF', width=2, dash='dash')
    ))

    fig.update_layout(
        plot_bgcolor='#111111',
        paper_bgcolor='#111111',
        font_color='white',
        title='Bitcoin - Últimos 30 días',
        xaxis_title='Fecha',
        yaxis_title='Precio (€)',
        hovermode='x unified',
    )

    st.plotly_chart(fig, use_container_width=True)

# Función para graficar precios intradía
def plot_hourly(df):
    df["sma_24h"] = df["price"].rolling(window=24).mean()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["date"], y=df["price"],
        mode='lines',
        name='Precio BTC (1H)',
        line=dict(color='#00FF7F', width=2)
    ))

    fig.add_trace(go.Scatter(
        x=df["date"], y=df["sma_24h"],
        mode='lines',
        name='SMA 24h',
        line=dict(color='#1E90FF', width=2, dash='dash')
    ))

    fig.update_layout(
        plot_bgcolor='#111111',
        paper_bgcolor='#111111',
        font_color='white',
        title='Bitcoin - Última semana (1H)',
        xaxis_title='Fecha y Hora',
        yaxis_title='Precio (€)',
        hovermode='x unified',
    )

    st.plotly_chart(fig, use_container_width=True)

# Función para calcular métricas principales
def show_metrics(df):
    # Precio actual
    current_price = df["price"].iloc[-1]

    # Cambio en 24h
    price_24h_ago = df[df["date"] >= (df["date"].iloc[-1] - pd.Timedelta(hours=24))]["price"].iloc[0]
    change_24h = ((current_price - price_24h_ago) / price_24h_ago) * 100

    # Volatilidad semanal (desviación estándar de 7 días)
    volatility_week = df["price"].pct_change().rolling(window=24*7).std().mean() * 100  # en porcentaje

    col1, col2, col3 = st.columns(3)
    col1.metric("Precio Actual (EUR)", f"{current_price:,.2f} €")
    col2.metric("Cambio 24h", f"{change_24h:.2f} %")
    col3.metric("Volatilidad Semanal", f"{volatility_week:.2f} %")

# Streamlit App
st.set_page_config(page_title="BTC Forecast", layout="wide")

st.title("BTC Forecast Dashboard")
st.markdown("Visualiza la evolución reciente de Bitcoin en dos modos distintos:")

mode = st.selectbox("Selecciona el modo de visualización:", ("Últimos 30 días (diario)", "Última semana (1H)"))

if mode == "Últimos 30 días (diario)":
    df_daily = load_csv("btc_prices.csv")
    show_metrics(df_daily)
    plot_daily(df_daily)
else:
    df_hourly = load_csv("btc_hourly.csv")
    show_metrics(df_hourly)
    plot_hourly(df_hourly)
