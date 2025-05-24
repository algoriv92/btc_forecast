import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Generamos datos dummy
dates = pd.date_range(start="2025-04-01", periods=30, freq="D")
prices = np.random.uniform(20000, 70000, size=30)

# Creamos figura Plotly
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=dates,
    y=prices,
    mode="lines",
    name="Precio BTC simulado",
    line=dict(color="#00FF7F", width=2)
))

fig.update_layout(
    title="Test Interactividad Plotly",
    xaxis_title="Fecha",
    yaxis_title="Precio (€)",
    font=dict(color="white"),
    plot_bgcolor="#111111",
    paper_bgcolor="#111111",
    hovermode="x unified"  # Activa el hover informativo
)

# Streamlit config
st.set_page_config(page_title="Test Plotly", layout="wide")
st.title("🚀 Test Hover Interactivo Plotly")

# ¡Aquí está el render!
st.plotly_chart(fig, use_container_width=True)
