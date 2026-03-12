# Stock Portfolio Analytics & Recommendation System

A **Python-based portfolio analytics tool** that analyzes stock holdings using **real-time market data from Yahoo Finance**.  
The system calculates **portfolio value, asset allocation, and momentum** while generating **Buy / Sell / Hold recommendations** based on portfolio analytics.

---

##  Features

- Fetches **real-time stock prices** using the **Yahoo Finance API**
- Calculates **portfolio value and asset allocation**
- Performs **30-day momentum analysis**
- Generates **Buy / Sell / Hold recommendations**
- Displays **clean financial visualizations**
- Handles **invalid or delisted tickers automatically**

---

##  Technologies Used

- **Python**
- **Pandas**
- **yFinance API**
- **Matplotlib**
- **Seaborn**

---

##  Project Structure
stock-portfolio-analytics
│
├── portfolio_tracker.py
├── Portfolio.csv
└── README.md


---

##  Example Portfolio File

Your portfolio file should contain:
Ticker,Quantity
AAPL,2
MSFT,3
TSLA,1
JPM,5
SPY,3


---

##  How It Works

1. Loads the **portfolio dataset**
2. Fetches **real-time stock prices from Yahoo Finance**
3. Calculates **portfolio value and asset allocation**
4. Retrieves **30-day historical stock prices**
5. Performs **momentum analysis**
6. Generates **Buy / Sell / Hold recommendations**

---

##  Example Output

**Portfolio Summary**
Ticker Quantity CurrentPrice Value
AAPL 2 255.58 511.16
MSFT 3 402.99 1208.97
TSLA 1 180.20 180.20


**Total Portfolio Value**
$1900+


The program also generates:

-  Portfolio allocation chart  
-  Top holdings visualization  
-  30-day stock price trends  

---

##  Installation

Install required libraries:
pip install yfinance pandas matplotlib seaborn

## Run the Project
python portfolio_tracker.py

