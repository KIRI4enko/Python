'''
Конвертер валют
Currency Converter
'''
import requests
import json

cur_from = input('Из какой валюты вы хотите перевести: ')
cur_into = input('В какую валюту вы хотите перевести: ')
pairs = cur_from + cur_into
value = float(input(f'Сколько {cur_from} у вас есть: '))
response = requests.get('https://currate.ru/api/', params={"get": "rates", "key": input('API-KEY: '), "pairs": pairs})
# API-KEY 17d5ad9e6b9d1023a978257019b16bca

json_obj = json.loads(response.content)
if json_obj['status'] == 200:
    data = json_obj['data']
    print(f'1 {cur_from} = {data[pairs]} {cur_into}')
    print(f'Вы можете получить {round(float(data[pairs]) * value, ndigits=4)} {cur_into}')
else:
    print(f'ERROR {json_obj["status"]}')
    print(json_obj)
