import requests
import json


exchange_rate = {}
coin = input().lower()
while True:
    get_data = requests.get(f"http://www.floatrates.com/daily/{coin}.json")
    json_data = get_data.text
    python_data = json.loads(json_data)
    if coin != "usd":
        usd_cash = python_data["usd"]["rate"]
        exchange_rate["usd"] = usd_cash
    if coin != "eur":
        eur_cash = python_data["eur"]["rate"]
        exchange_rate["eur"] = eur_cash
    currency_code = input().lower()
    if not currency_code:
        break
    amount = int(input())
    print("Checking the cache...")
    if currency_code in exchange_rate:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        code_cash = python_data[f"{currency_code}"]["rate"]
        exchange_rate[f"{currency_code}"] = code_cash
    money = round(amount * exchange_rate[f"{currency_code}"], 2)
    print(f"You received {money} {currency_code}.")
