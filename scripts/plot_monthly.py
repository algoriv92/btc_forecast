import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

def load_csv(filename="btc_prices.csv"):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "data", filename)
    return pd.read_csv(data_path, parse_dates=["date"])

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_prices(df):
    # Calculamos la Media Móvil de 7 días
    df["sma_7"] = df["price"].rolling(window=7, center=True).mean()

    # Evaluamos tendencia general
    is_bullish = df["price"].iloc[-1] > df["price"].iloc[0]
    line_color = '#00FF7F' if is_bullish else '#FF4C4C'  # Verde lima o rojo coral

    # Estilo oscuro minimalista
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_facecolor('#111111')         # Fondo gráfico
    fig.patch.set_facecolor('#111111')  # Fondo ventana

    # Gráfico principal - Precio
    ax.plot(df["date"], df["price"], color=line_color, linewidth=2.5, label="Precio BTC")

    # Gráfico Media Móvil
    ax.plot(df["date"], df["sma_7"], color="#1E90FF", linestyle="--", linewidth=2, label="SMA 7 días")

    # Ejes minimalistas
    ax.tick_params(axis='x', colors='white', labelsize=9)
    ax.tick_params(axis='y', colors='white', labelsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#444444')
    ax.spines['bottom'].set_color('#444444')

    # Eje de fechas
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
    plt.xticks(rotation=45)

    # Título
    ax.set_title("Bitcoin - Últimos 30 días", fontsize=14, color='white', pad=15)

    # Limpiar ejes
    ax.set_xlabel("")
    ax.set_ylabel("")

    # Añadimos leyenda elegante
    legend = ax.legend(loc="upper left", fontsize=10)
    for text in legend.get_texts():
        text.set_color("white")

    # Margen automático
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_csv()
    plot_prices(df)
