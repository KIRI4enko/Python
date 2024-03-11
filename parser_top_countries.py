'''
Парсер - Топ стран на Codeforce
Parser - Top countries on Codeforce
'''
import requests
import json

url = 'https://codeforces.com/api/user.ratedList?activeOnly=true&includeRetired=false'

response = requests.get(url)
countryes = set(input('Введите страны через пробел: ').split())
number = 1
if response:
    json_obj = json.loads(response.content)
    if json_obj['status'] == 'OK':
        results = json_obj['result']
        for man in results:
            if 'country' in man and man['country'] in countryes:
                print(number, '-', man['handle'], man['rating'], man['country'])
            number += 1
    else:
        print('status not OK')
else:
    print(response.status_code)
