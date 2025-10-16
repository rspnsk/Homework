import os
from dotenv import load_dotenv
import requests

load_dotenv()


def get_convert_sum(transaction: dict) -> float:
    """Функция для конвертации валюты"""
    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {
        "amount": transaction["operationAmount"]["amount"],
        "from": transaction["operationAmount"]["currency"]["code"],
        "to": "RUB"
    }

    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        response = requests.get(url, headers=headers, params=payload)
        result = response.json()
        return  float(result["result"])

my_convert = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
print(get_convert_sum(my_convert))
print(type(get_convert_sum(my_convert)))