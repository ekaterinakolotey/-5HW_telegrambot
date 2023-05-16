import requests
import json
from config import keys


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            qoute_key = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_key = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise APIException(f'Не удалось обработать количество  {amount}')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={base_key}&from={qoute_key}&amount={amount}"

        payload = {}
        headers = {"apikey": "8iBeJcNOEfNe5P7McNp7sc4fOtFbTRz8"}

        response = requests.request("GET", url, headers=headers, data=payload)

        total_base = json.loads(response.content)['result']
        print(total_base)

        return total_base