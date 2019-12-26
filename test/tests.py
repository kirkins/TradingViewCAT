import sys
from os import path
sys.path.append(path.dirname( path.dirname( path.abspath(__file__))))
import requests
from actions import parse_webhook

# Example Order
# https://github.com/ccxt/ccxt/wiki/Manual#symbols-and-market-ids

# symbol = 'BTC/USD'
# type = 'limit'
# side = 'buy'
# amount = 0.01
# price = 7000


def post_test():
    r = requests.post('http://localhost:5000/webhook', data=str({"type": "limit", "side": "buy", "amount": "0.01", "symbol": "BTC/USD", "price": "7000", "key": "99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319"}))
    print(r)

parse_webhook(str({"type": "limit", "side": "buy", "amount": "0.01", "symbol": "BTC/USD", "price": "7000", "key": "99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319"}))


post_test()