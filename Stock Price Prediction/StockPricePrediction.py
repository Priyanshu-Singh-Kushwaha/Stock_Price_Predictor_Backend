import yfinance as yf
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import datetime

# Fetch real-time data
def fetch_real_time_data(symbol, interval):
    try:
        if interval == '60min':
            data = yf.download(symbol, interval='60m', period='7d')
        elif interval == 'daily':
            data = yf.download(symbol, interval='1d', period='1mo')
        else:
            print(f"Invalid interval: {interval}")
            return pd.DataFrame()

        if data.empty or 'Close' not in data.columns:
            print(f"Data format issue or invalid symbol: {symbol}")
            return pd.DataFrame()

        data = data[['Close']]
        return data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return pd.DataFrame()

# Using ARIMA
def forecast_future_prices(data, days_ahead=5):
    data = data.copy()
    # Fiting ARIMA model
    model = ARIMA(data['Close'], order=(5,1,0))
    model_fit = model.fit()

    # Future prices
    forecast = model_fit.get_forecast(steps=days_ahead)
    forecast_mean = forecast.predicted_mean
    forecast_conf_int = forecast.conf_int()

    # Future dates
    future_dates = [data.index[-1] + datetime.timedelta(days=i) for i in range(1, days_ahead + 1)]
    
    return future_dates, forecast_mean

# Update and plot data based on the selected interval
def update_plot():
    try:
        print("Update button clicked")
        symbol = symbol_entry.get().strip()
        interval = interval_combobox.get()

        if not symbol:
            print("Please enter a stock symbol.")
            return

        data = fetch_real_time_data(symbol, interval)
        print(f"Data fetched: {data.head()}")

        if data.empty:
            print("No data available.")
            return

        # Forecast future prices
        future_dates, future_prices = forecast_future_prices(data)
        print(f"Future dates: {future_dates}")
        print(f"Future prices: {future_prices}")

        data['Days'] = np.arange(len(data))
        X = data[['Days']].values
        y = data['Close'].values
        model = ARIMA(y, order=(5,1,0))  
        model_fit = model.fit()
        predictions = model_fit.predict(start=0, end=len(y)-1)

        plot_data = pd.DataFrame(index=data.index)
        plot_data['Actual Prices'] = y
        plot_data['Predicted Prices'] = predictions

        plt.figure(figsize=(12, 6))
        plt.plot(plot_data.index, plot_data['Actual Prices'], color='blue', label='Actual Prices')
        plt.plot(plot_data.index, plot_data['Predicted Prices'], color='red', linestyle='--', label='Predicted Prices')

        plt.plot(future_dates, future_prices, color='green', linestyle=':', marker='o', label='Future Predictions')

        plt.xlabel('Datetime')
        plt.ylabel('Price')
        plt.title(f'{symbol} - Actual vs Predicted Prices and Future Forecast ({interval})')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")

root = tk.Tk()
root.title("Stock Market Prediction")

tk.Label(root, text="Stock Symbol:").grid(row=0, column=0, padx=10, pady=10)
symbol_entry = tk.Entry(root)
symbol_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Interval:").grid(row=1, column=0, padx=10, pady=10)
interval_combobox = ttk.Combobox(root, values=["60min", "daily"])
interval_combobox.set("60min")  # Default value
interval_combobox.grid(row=1, column=1, padx=10, pady=10)

update_button = tk.Button(root, text="Update Plot", command=update_plot)
update_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()