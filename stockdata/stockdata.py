import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

def get_historical(ticker):
    api_token = config['API_TOKEN']
    res = requests.get(f'https://api.stockdata.org/v1/data/eod?symbols={ticker}&api_token={api_token}')
    return res
