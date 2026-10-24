# Tesla Stock Market Analysis and Forecasting 📈

## Overview

This project explores historical Tesla (TSLA) stock market data using Python and time-series analysis techniques. It combines exploratory data analysis, stock return calculations, volatility analysis, moving averages, seasonal decomposition, and Facebook Prophet to analyze historical price movements and forecast future closing prices.

The goal is to understand historical stock price behavior and demonstrate the application of time-series forecasting techniques to financial market data.

## Objectives

- Analyze historical Tesla stock prices and trading volume.
- Visualize stock price trends over time.
- Examine trend and seasonal components using time-series decomposition.
- Calculate daily stock returns and rolling annualized volatility.
- Analyze 10-day and 50-day moving averages.
- Build a forecasting model using Facebook Prophet.
- Generate and visualize a 365-calendar-day forecast.
- Explore forecast trends and seasonal components.

## Technologies and Libraries

- **Python** — Data analysis and modeling.
- **Pandas** — Data manipulation and preprocessing.
- **NumPy** — Numerical calculations.
- **Matplotlib** — Data visualization.
- **Statsmodels** — Seasonal decomposition.
- **Facebook Prophet** — Time-series forecasting.

## Dataset

The project uses historical Tesla stock market data stored in `TSLA.csv`.

The dataset contains the following features:

| Feature | Description |
|---|---|
| Date | Stock trading date |
| Open | Opening stock price |
| High | Highest price during the trading day |
| Low | Lowest price during the trading day |
| Close | Closing stock price |
| Adj Close | Adjusted closing price |
| Volume | Number of shares traded |

The `Close` column is used as the target variable for forecasting.

## Project Workflow

### 1. Data Loading and Inspection
- Load the dataset using Pandas.
- Inspect the first few rows.
- Check for missing values.
- Generate descriptive statistics.
- Convert the date column to datetime format.

### 2. Exploratory Data Analysis
Visualize historical closing prices and trading volume to identify patterns and changes in market activity.

### 3. Time-Series Decomposition
Apply seasonal decomposition using Statsmodels to examine:
- Trend component
- Seasonal component
- Residual component

A multiplicative decomposition model with a 30-observation period is used.

### 4. Stock Return Analysis
Calculate daily stock returns using the percentage change in closing prices to examine daily price movements.

### 5. Volatility Analysis
Calculate rolling annualized volatility using a 282-observation window and an annualization factor of 252 trading days.

### 6. Moving Average Analysis
Calculate and visualize:
- **MA10:** 10-trading-day moving average.
- **MA50:** 50-trading-day moving average.

These indicators help illustrate short-term and longer-term price trends.

### 7. Stock Price Forecasting with Prophet
Prepare the dataset in Prophet's required format:
- `ds`: Date
- `y`: Closing price

Fit a Prophet model with daily seasonality enabled and generate forecasts for the next 365 calendar days.

### 8. Forecast Visualization
Visualize the predicted closing prices and examine the model's estimated trend and seasonal components.

## Installation

Clone the repository:

```bash
git clone https://github.com/Vedline2547/Stock-market-prediction.git
cd Stock-market-prediction
```

Create a virtual environment on Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the required libraries:

```bash
python -m pip install pandas numpy matplotlib statsmodels prophet
```

## How to Run

1. Ensure `TSLA.csv` is available in your project directory.
2. Update the dataset path in your Python script if necessary.
3. Run the script:

```bash
python main.py
```

The script produces visualizations of stock prices, trading volume, seasonal decomposition, volatility, moving averages, returns, and Prophet forecasts.

## Key Learning Outcomes

- Financial time-series data analysis.
- Data preprocessing and visualization.
- Trend and seasonal decomposition.
- Daily return and rolling volatility calculations.
- Moving average analysis.
- Time-series forecasting with Facebook Prophet.
- Visualization and interpretation of forecasting components.

## Future Improvements

- Evaluate forecasts using a chronological train-test split.
- Calculate MAE, RMSE, and other appropriate evaluation metrics.
- Compare Prophet with ARIMA and other time-series models.
- Incorporate relevant external variables and market events.
- Generate predictions for actual trading dates rather than all calendar days.
- Investigate whether additional features improve forecasting performance.

## Limitations

Stock prices are affected by market sentiment, economic conditions, company announcements, and other factors that the current model does not explicitly incorporate. The model's predictive performance has not yet been established through held-out testing.

This project is intended for educational purposes and should not be used as the sole basis for investment decisions.

## Author

**Vedline Ochieng**

- GitHub: [Vedline2547](https://github.com/Vedline2547)
- LinkedIn: [Vedline Ochieng](https://www.linkedin.com/in/vedline-ochieng-025146290/)
