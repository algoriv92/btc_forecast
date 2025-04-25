# Análisis Visual de Bitcoin

Un proyecto personal que me permite descargar, visualizar y analizar el precio de Bitcoin (BTC) durante los últimos 30 días utilizando datos de CoinGecko.

## Scripts

- get_data.py: Descarga automáticamente los precios de BTC en USD
- plot_prices.py: Genera un gráfico de línea con colores de tendencia alcista-bajista
- indicator.py: Calcula:
  - Media Móvil Simple (SMA)
  - Volatilidad diaria

## 📂 Estructura del proyecto



btc_forecast/
├── data/                ← Aquí guardaremos los CSVs
├── scripts/             ← Aquí van los scripts de Python
│   └── get_data.py      ← Primer script: descarga de precios BTC
├── README.md            ← Descripción del proyecto

