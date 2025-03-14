import requests
import pandas as pd
import time
import matplotlib.pyplot as plt


# Función para obtener datos de CryptoCompare
def get_crypto_data(crypto_id="BTC", currency="USD", days=730):
    url = f"https://min-api.cryptocompare.com/data/v2/histoday"
    params = {
        "fsym": crypto_id,
        "tsym": currency,
        "limit": days,
        "toTs": int(time.time())
    }

    while True:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data["Data"]["Data"], columns=["time", "close"])
            df["timestamp"] = pd.to_datetime(df["time"], unit="s")
            df["price"] = df["close"]
            return df.drop(columns=["time", "close"])
        else:
            print(f"Error al obtener datos: {response.status_code}")
            return None


# Fechas de los halvings de Bitcoin (en formato de fecha)
halvings = {
    "2012": "2012-11-28",
    "2016": "2016-07-09",
    "2020": "2020-05-11",
    "2024": "2024-04-09",  # Halving de 2024
}

# Obtener los datos históricos para cada halving
dfs = {}
for year, date in halvings.items():
    df = get_crypto_data()
    if df is not None:
        dfs[year] = df


# Función para normalizar las fechas con respecto al halving
def normalize_dates(df, halving_date):
    df["days_since_halving"] = (df["timestamp"] - pd.to_datetime(halving_date)).dt.days
    return df


# Normalizamos los datos de los halvings
normalized_dfs = {}
for year, df in dfs.items():
    normalized_dfs[year] = normalize_dates(df, halvings[year])

# Graficamos los datos de cada halving superpuestos
plt.figure(figsize=(14, 7))  # Aumentar tamaño de la figura

# Recorremos todos los halvings y graficamos las curvas de precios
for year, df in normalized_dfs.items():
    plt.plot(df["days_since_halving"], df["price"], label=f"Halving {year}")

# Mejorar la visualización
plt.axvline(x=0, color='black', linestyle='--', linewidth=1)  # Línea de separación para el halving
plt.xlabel("Días desde el halving")
plt.ylabel("Precio (USD)")
plt.title("Comparativa de Halvings de Bitcoin (Incluido 2024)")
plt.legend(loc='upper left', fontsize=10)  # Añadir leyenda
plt.grid(True)  # Añadir una cuadrícula para facilitar la lectura
plt.tight_layout()  # Ajustar el diseño para que se vea todo bien

# Mostrar el gráfico
plt.show()
