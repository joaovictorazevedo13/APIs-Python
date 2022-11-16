import requests

to_coin = input("Moeda origem(ex: EUR): ")
from_coin = input("Moeda a ser convertida(ex: BRL): ")
value_coin = float(input("Valor a ser convertido: "))

payload = {}
headers= {
  "apikey": "19y08ONRz6oGvbyurX7XkPUaCRXNmzw7"
}
url_api = requests.get(f"https://api.apilayer.com/fixer/convert?to={to_coin}&from={from_coin}&amount={value_coin}", headers=headers, data = payload)

status_code = url_api.status_code
result = url_api.text

print(result)

