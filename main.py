# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet
from statsmodels.tsa.seasonal import seasonal_decompose
# Load dataset
df = pd.read_csv(r"C:\Users\HP\Desktop\New ML\Stock-market-prediction\TSLA.csv")
print(df.head())
# Check for missing values
print(df.isnull().sum())
# Basic statistical details
statistics = df.describe()
print(statistics)
# Convert date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
# Set date as index for dataframe for plotting
df.set_index('Date',inplace=True)
# Create a figure and a set of subplots
fig,ax = plt.subplots(nrows=2,ncols=1,figsize=(15,10))
# # Plot closing price over time
df['Close'].plot(ax=ax[0],color='blue')
ax[0].set_title('Closing price over time')
ax[0].set_ylabel('Price($)')
# Plot the volume over time
df['Volume'].plot(ax=ax[1],color='green')
ax[0].set_title('Trading volume over time')
ax[0].set_ylabel('Volume')
# Improve layout
plt.tight_layout()
plt.show()
# Seasonality analysis
decomposition = seasonal_decompose(df['Close'],model='multiplicative',period=30)
fig = decomposition.plot()
plt.show()
# Volatility analysis
df['Return'] = df['Close'].pct_change()
# Formula for calculating volatility
df['Volatility'] = df['Return'].rolling(window=282).std() * np.sqrt(252)
df[['Close','Volatility']].plot(subplots=True,color='blue',figsize=(8,6))
plt.show()
# Moving average analysis
df['MA10'] = df['Close'].rolling(window=10).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()
df[['Close','MA10','MA50']].plot(label='Tesla',figsize=(10,8))
plt.show()
# Return Analysis
df[['Return']].plot(label='Return',figsize=(10,8))
plt.show()
# Prepare data for prophet
prophet_df = df.reset_index()[['Date','Close']]
prophet_df.rename(columns={'Date':'ds','Close':'y'},inplace=True)
print(prophet_df.head())
# Initiate the prophet model
model = Prophet(daily_seasonality=True)
# Fit model to data
model.fit(prophet_df)
# Specify number of days for prediction
future = model.make_future_dataframe(periods=365)
# Use model to make prediction
forecast = model.predict(future)
# Visualize the forecast
model.plot(forecast)
plt.show()
# Model components
model.plot_components(forecast)
plt.show()