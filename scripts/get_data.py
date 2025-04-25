import requests
import pandas as pd
import os

def get_btc_prices(days=30):
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        prices = data["prices"]
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
        df = df[["date", "price"]]
        return df
    else:
        raise Exception(f"Error fetching data: {response.status_code}")

def save_to_csv(df, filename="btc_prices.csv"):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Va de scripts/ a raíz
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    output_path = os.path.join(data_dir, filename)
    df.to_csv(output_path, index=False)
    print(f"✅ Data saved to {os.path.abspath(output_path)}")

if __name__ == "__main__":
    df = get_btc_prices(days=30)
    save_to_csv(df)
    print("📈 BTC prices fetched successfully!")   