# Stock Market Prediction Tool

This Python application provides a simple graphical interface for fetching stock market data using `yfinance`, forecasting future prices using the ARIMA model, and visualizing the results.

## Description

This tool allows users to:
* Fetch real-time stock data from Yahoo Finance for a specified symbol and interval (60min or daily).
* Forecast future stock prices using the ARIMA time series model.
* Visualize the actual stock prices, predicted prices, and future price forecasts in a single plot.
* Interact with the tool through a user-friendly Tkinter graphical interface.

## Features

* **Real-time Data Fetching:** Utilizes `yfinance` to retrieve up-to-date stock data.
* **ARIMA Forecasting:** Employs the `statsmodels` ARIMA model for price prediction.
* **Interactive Visualization:** Generates plots using `matplotlib` to compare actual, predicted, and forecasted prices.
* **User-Friendly Interface:** Provides a simple Tkinter GUI for easy input and data visualization.
* **Interval Selection:** Allows users to select between 60-minute and daily data intervals.

## Installation

1.  **Clone the repository (or download the Python file):**

    ```bash
    git clone [[repository URL]](https://github.com/Priyanshu-Singh-Kushwaha/Stock_Price_Predictor_Backend.git)
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install yfinance pandas statsmodels numpy matplotlib tkinter
    ```

## Usage

1.  **Run the Python script:**

    ```bash
    python StockPricePrediction.py
    ```

2.  **Enter the stock symbol:** In the "Stock Symbol" field, enter the stock symbol you want to analyze (e.g., AAPL, GOOG).

3.  **Select the interval:** Choose the data interval from the "Interval" dropdown menu (60min or daily).

4.  **Click "Update Plot":** Click the "Update Plot" button to fetch the data, perform the forecast, and display the plot.

5.  **View the plot:** A new window will display the plot with the actual prices, predicted prices, and future price forecasts.

## Code Explanation
* **`fetch_real_time_data(symbol, interval)`:** Fetches stock data from Yahoo Finance based on the provided symbol and interval.
* **`forecast_future_prices(data, days_ahead=5)`:** Fits an ARIMA model to the data and forecasts future prices.
* **`update_plot()`:** Retrieves user input, fetches data, performs forecasting, and generates the plot.
* **Tkinter GUI:** Creates a window with input fields and a button to trigger the data fetching and plotting.

## Dependencies
* `yfinance`: For fetching stock market data.
* `pandas`: For data manipulation.
* `statsmodels`: For ARIMA time series modeling.
* `numpy`: For numerical operations.
* `matplotlib`: For plotting.
* `tkinter`: For the graphical user interface.
* `datetime`: for date manipulation.

## Notes
* The ARIMA model's accuracy can vary, and stock market predictions are inherently uncertain.
* This tool is for educational purposes and should not be used for financial decision-making without thorough research and professional advice.
* Error handling is implemented to catch potential issues with data fetching and model fitting.
* The default forecast is for 5 days into the future.
