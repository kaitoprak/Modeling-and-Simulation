import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# ==========================================
# Task 2: Stock Price Prediction
# Monte Carlo Simulation with GBM
# ==========================================

# Reproducibility
np.random.seed(42)

# ------------------------------------------
# 1. Parameters
# ------------------------------------------

ticker = "BBCA.JK"      # Contoh: Bank Central Asia
period = "1y"           # Historical data
forecast_days = 30      # Predict 30 trading days ahead
num_simulations = 10_000
trading_days = 252

# ------------------------------------------
# 2. Retrieve historical stock data
# ------------------------------------------

data = yf.download(
    ticker,
    period=period,
    auto_adjust=True,
    progress=False
)

if data.empty:
    raise ValueError("Data saham tidak berhasil diambil.")

# Close price
prices = data["Close"]

# Jika hasil Close berbentuk DataFrame
if isinstance(prices, pd.DataFrame):
    prices = prices.iloc[:, 0]

prices = prices.dropna()

# ------------------------------------------
# 3. Calculate logarithmic returns
# ------------------------------------------

log_returns = np.log(prices / prices.shift(1)).dropna()

# Daily volatility
daily_volatility = log_returns.std()

# Annualized volatility
annual_volatility = daily_volatility * np.sqrt(trading_days)

# Mean daily log return
mean_daily_log_return = log_returns.mean()

# Annualized drift (mu)
annual_drift = (
    mean_daily_log_return * trading_days
    + 0.5 * annual_volatility**2
)

# ------------------------------------------
# 4. Initial stock price
# ------------------------------------------

S0 = float(prices.iloc[-1])

print("==========================================")
print("STOCK INFORMATION")
print("==========================================")
print(f"Ticker              : {ticker}")
print(f"Current Price       : {S0:.2f}")
print(f"Annual Drift (mu)   : {annual_drift:.4f}")
print(f"Annual Volatility   : {annual_volatility:.4f}")
print(f"Daily Volatility    : {daily_volatility:.4f}")
print()

# ------------------------------------------
# 5. Monte Carlo Simulation
# Geometric Brownian Motion
# ------------------------------------------

dt = 1 / trading_days

# Matrix of random numbers
Z = np.random.standard_normal(
    (forecast_days, num_simulations)
)

# Price matrix
simulated_prices = np.zeros(
    (forecast_days + 1, num_simulations)
)

# Initial price
simulated_prices[0] = S0

# Generate price paths
for t in range(1, forecast_days + 1):

    simulated_prices[t] = simulated_prices[t - 1] * np.exp(
        (annual_drift - 0.5 * annual_volatility**2) * dt
        + annual_volatility * np.sqrt(dt) * Z[t - 1]
    )

# ------------------------------------------
# 6. Final prices after 30 days
# ------------------------------------------

final_prices = simulated_prices[-1]

expected_price = np.mean(final_prices)
median_price = np.median(final_prices)

percentile_5 = np.percentile(final_prices, 5)
percentile_95 = np.percentile(final_prices, 95)

print("==========================================")
print("SIMULATION RESULTS")
print("==========================================")
print(f"Initial Price           : {S0:.2f}")
print(f"Expected Price (30d)    : {expected_price:.2f}")
print(f"Median Price (30d)     : {median_price:.2f}")
print(f"5th Percentile          : {percentile_5:.2f}")
print(f"95th Percentile         : {percentile_95:.2f}")

# ------------------------------------------
# 7. Probability price increases
# ------------------------------------------

prob_increase = np.mean(final_prices > S0)

print(f"Probability Price Rises : {prob_increase:.2%}")

# ------------------------------------------
# 8. Visualize simulated paths
# ------------------------------------------

plt.figure(figsize=(12, 6))

# Show only 100 paths
num_paths_to_plot = 100

for i in range(num_paths_to_plot):
    plt.plot(
        simulated_prices[:, i],
        linewidth=0.8,
        alpha=0.5
    )

plt.axhline(
    S0,
    linestyle="--",
    label="Initial Price"
)

plt.title(
    f"Monte Carlo Simulation of {ticker} "
    f"for {forecast_days} Trading Days"
)

plt.xlabel("Trading Days")
plt.ylabel("Stock Price")
plt.legend()
plt.grid(True)

plt.show()

# ------------------------------------------
# 9. Distribution of final prices
# ------------------------------------------

plt.figure(figsize=(10, 6))

plt.hist(
    final_prices,
    bins=50,
    edgecolor="black"
)

plt.axvline(
    expected_price,
    linestyle="--",
    linewidth=2,
    label=f"Expected = {expected_price:.2f}"
)

plt.axvline(
    S0,
    linestyle="--",
    linewidth=2,
    label=f"Initial = {S0:.2f}"
)

plt.title(
    f"Distribution of Simulated {ticker} Prices "
    f"After {forecast_days} Days"
)

plt.xlabel("Stock Price")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)

plt.show()