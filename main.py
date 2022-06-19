#!/usr/bin/env python

"""
TradeOgre API Dollar Cost Average Script
https://github.com/terrainduck/tradeogre-dca
"""

import requests
from requests.auth import HTTPBasicAuth
import json
import datetime


# Get config
configFile = open("config.json", "r")
configRead = configFile.read()
configJson = json.loads(configRead)
config = configJson[0]
configFile.close()

publicKey = config["keys"]["public"]
secretKey = config["keys"]["secret"]

markets = config["markets"]

now = datetime.datetime.now()
print(str(now))

API_URL = config["api_url"]

for market in markets:
    pair = market["pair"]
    quantity = market["quantity"]
    maxPrice = market["maxPrice"]

    try:
        orders = requests.get(API_URL + "orders/" + pair).json()
    except Exception as e:
        print(e)
        exit()

    if (not orders["success"]):
        print(orders)
        exit()

    sellOrders = orders["sell"]

    minSellOrderPrice = min(sellOrders.keys())

    if float(minSellOrderPrice) < float(maxPrice):
        data = {
            "market": pair,
            "quantity": quantity,
            "price": minSellOrderPrice
        }

        URL = API_URL + "order/buy"

        try:
            response = requests.post(url=URL, data=data, auth=HTTPBasicAuth(publicKey, secretKey))
        except Exception as e:
            print(e)
            exit()

        print(response.text)
    else:
        print("Minimum sell order price is not less than max buy price. Not buying.")

print("")
