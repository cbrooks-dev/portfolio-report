from portfolio import Portfolio as P
from emailer import Emailer as E
from file_handler import FileHandler as FH
import os, base64

# Decode and recreate csv file at runtime
b64_data = os.environ["PORTFOLIO_B64"]
decoded = base64.b64decode(b64_data)
with open("portfolio.csv", "wb") as f:
    f.write(decoded)

assets = FH.read_portfolio_csv("portfolio.csv") # Create asset dict

portfolio = P(assets) # Create a portfolio object

# Gather statistics to show
statistics = {}
statistics["sum_of_assets"] = portfolio.get_sum()
statistics["percent_increase"] = portfolio.get_day_percentage_increase()
statistics["dollar_increase"] = portfolio.get_day_dollar_increase()
statistics["best_performer"] = portfolio.asset_of_the_day()

# Generate email report
email = E(statistics)
email.send()
