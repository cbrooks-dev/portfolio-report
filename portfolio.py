import yfinance as yf

class Portfolio():
    """Model of an investor's portfolio."""


    def __init__(self, portfolio: dict[str, float]):
        """Constructs the investor's portfolio."""

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
        
        return (current_sum - open_sum) / current_sum

    
    def get_day_dollar_increase(self) -> float:
        """Returns the total $ increase of portfolio."""
            
        current_sum = self.get_sum()
        open_sum = self.get_sum("open")
        
        return (current_sum - open_sum)
                
    
    def asset_of_the_day(self) -> str:
        """Get the asset of the day based on % increase."""

        asset_of_the_day = ""

        for ticker in self.portfolio.keys():
            if (asset_of_the_day == ""):
                asset_of_the_day = ticker
                continue # Skip if first asset
            asset = yf.Ticker(ticker).fast_info
            top_earner = yf.Ticker(asset_of_the_day).fast_info
            open_price = float(asset.open)
            current_price = float(asset.last_price)
            increase = (current_price - open_price) / current_price
            asset_of_the_day_open_price = float(top_earner.open)
            asset_of_the_day_current_price = float(top_earner.last_price)
            asset_of_the_day_increase = ((asset_of_the_day_current_price -
                                         asset_of_the_day_open_price)
                                         / asset_of_the_day_current_price)
            if increase > asset_of_the_day_increase:
                asset_of_the_day = ticker
        
        return asset_of_the_day
