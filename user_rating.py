'''
Рейтинг пользователя CodeForce(с диаграммой)
CodeForce user rating (with chart)
'''
import json
import matplotlib.pyplot as plt
import requests

url = 'https://codeforces.com/api/user.rating'
handle = input('Хэндл пользователя: ')
response = requests.get(url, params={'handle': handle})
rating = []

if response:
    json_result = json.loads(response.content)
    #print(json_result)
    for contest in json_result['result']:
        rating.append(contest['newRating'])
    plt.plot(rating)
    plt.ylabel('PTS')
    plt.title(f'История рейтинга пользователя под ником {handle}')
    plt.show()
else:
    print('ERROR', response.status_code)
