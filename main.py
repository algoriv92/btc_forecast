import requests
import pandas as pd
import matplotlib.pyplot as plt


# Obtener datos de CoinGecko
def get_crypto_data(crypto_id="bitcoin", currency="usd", days=30):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"
    params = {"vs_currency": currency, "days": days, "interval": "daily"}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        prices = data["prices"]
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df
    else:
        print("Error al obtener datos:", response.status_code)
        return None


# Descargar datos de los últimos 30 días
df = get_crypto_data()

# Graficar
if df is not None:
    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["price"], label="Bitcoin Price")
    plt.xlabel("Fecha")
    plt.ylabel("Precio (USD)")
    plt.title("Precio histórico de Bitcoin")
    plt.legend()
    plt.show()