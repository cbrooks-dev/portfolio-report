from file_handler import FileHandler as FH
from portfolio import Portfolio as P

json = FH.read_json("config.json")
file_name = json.get("csv_file_name")
assets = FH.read_portfolio_csv(file_name)
portfolio = P(assets)
print(portfolio.asset_of_the_day())
