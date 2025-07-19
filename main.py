from file_handler import FileHandler as FH
from portfolio import Portfolio as P
from emailer import Emailer as E

# Create a portfolio object
json_config = FH.read_json("config.json")
portfolio_file_name = json_config.get("csv_file_name")
assets = FH.read_portfolio_csv(portfolio_file_name)
portfolio = P(assets)

# Gather statistics to show
statistics = {}
statistics["sum_of_assets"] = portfolio.get_sum()
statistics["percent_increase"] = portfolio.get_day_percentage_increase()
statistics["dollar_increase"] = portfolio.get_day_dollar_increase()
statistics["best_performer"] = portfolio.asset_of_the_day()

# Generate email report
email = E(statistics)
email.send()
