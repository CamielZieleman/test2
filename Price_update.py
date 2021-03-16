import os
import requests
from datetime import datetime
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%('B', 'A'), timeout = 500)


def getprice():

    price_file = open("Price.txt","a")
    latest_block = rpc_connection.getmininginfo()["blocks"]
    print(latest_block)
    data = requests.get("https://www.bitstamp.net/api/ticker/").json()
    day = datetime.utcfromtimestamp(int(data["timestamp"])).strftime('%d')
    if day == "01":
        print(latest_block,data["last"],file=price_file)

