import yfinance as yf

class Screening:
    """Contains functions for screening the market."""


    def __init__(self):
        pass


    def best_pe_ratio(self):
        etf = yf.Ticker("QQQ")
        holdings = etf.fund_holdings
        print(holdings.head())


import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
df = pd.read_html(url)[0]  # First table
print(pd.read_html(url)[1])
tickers = df['Symbol'].tolist()

# Optional: Clean up tickers (e.g., BRK.B becomes BRK-B for yfinance)
tickers = [ticker.replace('.', '-') for ticker in tickers]

#print(tickers)
