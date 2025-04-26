import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

def load_hourly_csv(filename="btc_hourly.csv"):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "data", filename)
    return pd.read_csv(data_path, parse_dates=["date"])

def plot_hourly(df):
    # Calculamos Media Móvil de 24 horas
    df["sma_24h"] = df["price"].rolling(window=24).mean()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_facecolor('#111111')
    fig.patch.set_facecolor('#111111')

    # Línea principal: precio 1h
    ax.plot(df["date"], df["price"], color="#00FF7F", linewidth=2.0, label="Precio BTC (1H)")

    # Línea secundaria: SMA 24H
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
    ax.set_xlabel("")
    ax.set_ylabel("")

    # Añadimos leyenda elegante
    legend = ax.legend(loc="upper left", fontsize=10)
    for text in legend.get_texts():
        text.set_color("white")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_hourly_csv()
    plot_hourly(df)
