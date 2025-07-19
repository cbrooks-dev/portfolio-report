import yfinance as yf

class Portfolio():
    """Model of an investor's portfolio."""


    def __init__(self, portfolio: dict[str, float]):
        """
        Constructs the investor's portfolio from a
        dict like: {ticker_symbol: shares_owned}
        """

        self.portfolio = portfolio
    
    
    def get_sum(self, type: str = "current") -> float:
        """Returns $ sum of all portfolio assets."""

        sum = 0.0 # Sum of investments
        
        # Gather total worth of investments
        for ticker in self.portfolio.keys():
            shares = float(self.portfolio.get(ticker))
            asset = yf.Ticker(ticker).fast_info
            if type == "open":
                price = asset.open
            else:
                price = asset.last_price
            sum += shares * float(price)

        return sum
    

    def get_day_percentage_increase(self):
        """Returns the total % increase of portfolio."""

        current_sum = self.get_sum()
        open_sum = self.get_sum("open")

        if current_sum == 0: # Avoid division by 0
            return current_sum
        
        return (current_sum - open_sum) / current_sum

    
    def get_day_dollar_increase(self) -> float:
        """Returns the total $ increase of portfolio."""
            
        current_sum = self.get_sum()
        open_sum = self.get_sum("open")
        
        return (current_sum - open_sum)
                
    
    def asset_of_the_day(self) -> str:
        """Returns the asset with the highest % increase today."""

        best_ticker = None
        best_increase = float('-inf')

        for ticker in self.portfolio:
            asset = yf.Ticker(ticker).fast_info
            open_price = float(asset.open)
            current_price = float(asset.last_price)
            if open_price == 0:
                continue  # Avoid division by zero
            increase = (current_price - open_price) / open_price
            if increase > best_increase:
                best_increase = increase
                best_ticker = ticker

        return best_ticker if best_ticker is not None else ""
