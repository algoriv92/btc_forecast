import pandas as pd
import os

def load_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "data", "btc_prices.csv")
    return pd.read_csv(data_path, parse_dates=["date"])

def calculate_sma(df, window=7):
    df["SMA"] = df["price"].rolling(window=window).mean()
    return df

def calculate_volatility(df, window=7):
    df["Volatility"] = df["price"].rolling(window=window).std()
    return df

if __name__ == "__main__":
    df = load_data()
    df = calculate_sma(df)
    df = calculate_volatility(df)

    # Mostrar últimos 10 días con indicadores
    print(df.tail(10)[["date", "price", "SMA", "Volatility"]])
