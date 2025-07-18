import yfinance as yf
from email.message import EmailMessage
import smtplib

class GenerateReport():
    """Object for handling report generation."""


    def get_ticker_list(portfolio: dict[str, int | float]) -> list:
        """Returns a list of all ticker symbols in portfolio."""

        ticker_list = []
        for ticker in portfolio.keys():
            ticker_list.append(ticker)
        
        return ticker_list


    def gatherData(ticker_list: list[str]) -> dict:
        """Returns a dict of data about each ticker symbol."""

        ticker_data = {}

        for ticker_symbol in ticker_list:
            ticker = yf.Ticker(ticker_symbol)
            print(ticker.fast_info.last_price - ticker.fast_info.open) # TODO: change to actual data logic
