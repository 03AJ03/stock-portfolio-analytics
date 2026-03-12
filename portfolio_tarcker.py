import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

print("\nLoading portfolio...\n")

# ---------------------------------
# LOAD PORTFOLIO
# ---------------------------------

portfolio = pd.read_csv("Portfolio.csv")
portfolio = portfolio[["Ticker","Quantity"]]

portfolio["CurrentPrice"] = 0
portfolio["Value"] = 0

# ---------------------------------
# FETCH REAL STOCK PRICES
# ---------------------------------

for i,row in portfolio.iterrows():

    ticker = row["Ticker"]
    shares = row["Quantity"]

    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")

        price = data["Close"].iloc[-1]

        portfolio.loc[i,"CurrentPrice"] = price
        portfolio.loc[i,"Value"] = price * shares

        print(f"{ticker} price fetched successfully")

    except:
        print(f"Could not fetch data for {ticker}")

# ---------------------------------
# PORTFOLIO SUMMARY
# ---------------------------------

print("\nPortfolio with Real-Time Prices\n")
print(portfolio)

total_value = portfolio["Value"].sum()

print("\nTotal Portfolio Value:", round(total_value,2))

# ---------------------------------
# PORTFOLIO WEIGHTS
# ---------------------------------

portfolio["Weight"] = portfolio["Value"] / total_value

# ---------------------------------
# CLEAN PIE CHART (TOP HOLDINGS)
# ---------------------------------

portfolio_sorted = portfolio.sort_values(by="Value", ascending=False)

top8 = portfolio_sorted.head(8)

others_value = portfolio_sorted["Value"][8:].sum()

labels = list(top8["Ticker"])
values = list(top8["Value"])

if others_value > 0:
    labels.append("Others")
    values.append(others_value)

plt.figure(figsize=(10,7))

plt.pie(
    values,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140
)

plt.title("Portfolio Allocation (Top Holdings)")

plt.show()

# ---------------------------------
# BAR CHART OF TOP HOLDINGS
# ---------------------------------

top10 = portfolio.sort_values(by="Value", ascending=False).head(10)

plt.figure(figsize=(10,6))

sns.barplot(
    x="Ticker",
    y="Value",
    data=top10,
    palette="viridis"
)

plt.title("Top Portfolio Holdings by Value")
plt.xlabel("Stock")
plt.ylabel("Investment Value")

plt.xticks(rotation=45)

plt.show()

# ---------------------------------
# HISTORICAL PRICE DATA
# ---------------------------------

print("\nFetching 30-day stock history...\n")

valid_tickers = portfolio[portfolio["CurrentPrice"] > 0]["Ticker"].tolist()

history = yf.download(valid_tickers, period="30d")["Close"]

# ---------------------------------
# HISTORICAL PRICE CHART
# ---------------------------------

plt.figure(figsize=(12,7))

for stock in history.columns:
    plt.plot(history.index, history[stock], label=stock)

plt.title("Stock Price Trends (Last 30 Days)")
plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()

plt.show()

# ---------------------------------
# MOMENTUM CALCULATION
# ---------------------------------

momentum = (history.iloc[-1] - history.iloc[0]) / history.iloc[0]

print("\n30-Day Momentum\n")
print(momentum.sort_values(ascending=False))

# ---------------------------------
# BUY / SELL RECOMMENDATION ENGINE
# ---------------------------------

print("\nPortfolio Recommendations\n")

for i,row in portfolio.iterrows():

    ticker = row["Ticker"]
    weight = row["Weight"]

    try:
        mom = momentum[ticker]
    except:
        mom = 0

    if weight > 0.15:
        recommendation = "SELL (Too much portfolio concentration)"

    elif mom > 0.10:
        recommendation = "BUY MORE (Strong upward momentum)"

    elif mom < -0.10:
        recommendation = "SELL (Negative momentum)"

    else:
        recommendation = "HOLD"

    print(f"{ticker} → {recommendation}")