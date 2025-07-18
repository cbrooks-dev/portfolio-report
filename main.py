from file_handler import FileHandler as FH
from report import GenerateReport as GR

json = FH.read_json("config.json")
file_name = json.get("csv_file_name")
csv = FH.read_portfolio_csv(file_name)
#print(csv)

print(GR.gatherData(['BTC-USD']))
