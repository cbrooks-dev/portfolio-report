import csv
import json

class FileHandler():
    """Object for handling file management and access."""


    def __init__(self):
        pass


    def read_json(file_path: str) -> dict:
        """Convert generic JSON file to dictionary."""
        
        with open(f'{file_path}', 'r') as file:
            return json.load(file)
        
    
    def read_portfolio_csv(file_path: str) -> dict:
        """
        Convert specific portfolio CSV file to dictionary.
        Key-value pairs will be ticker symbols and shared owned.
        """

        header_row = True
        csv_dict = {}

        with open(f'{file_path}', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if header_row:
                    header_row = False
                    continue
                ticker_symbol = row[0]
                shares = row[1]
                csv_dict[ticker_symbol] = shares
        
        return csv_dict
