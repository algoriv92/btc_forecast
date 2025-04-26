import os
import requests
import pandas as pd

def get_hourly_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "eur",
        "days": "7"  # NO ponemos interval
    }
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print(f"❌ Error {response.status_code}: {response.text}")
        return

    data = response.json().get("prices")
    if data is None:
        print("❌ No se encontró el campo 'prices' en la respuesta.")
        return

    df = pd.DataFrame(data, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df = df.drop("timestamp", axis=1)

    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    output_path = os.path.join(data_dir, "btc_hourly.csv")
    df.to_csv(output_path, index=False)
    print(f"✅ Datos horarios guardados en {output_path}")

if __name__ == "__main__":
    get_hourly_data()
