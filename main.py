# TODO: Add error handling
# Write output to log if success or not

import requests
import json

API_URL = "https://tradeogre.com/api/v1/"

# Get config
configFile = open("config.json", "r")
config = json.loads(configFile.read())[0] # TODO: Loop through all the items
configFile.close()

market = config["market"]
amountDollar = config["amountDollar"]
maxPrice = config["maxPrice"]

orders = requests.get(API_URL + "orders/" + market).json()

sellOrders = orders["sell"]

minSellOrderPrice = min(sellOrders.keys())

if float(minSellOrderPrice) < float(maxPrice):
    print("buy")
else:
    print("don't buy")

