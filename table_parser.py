'''
Парсер таблицы(фильмы победители)
Table parser (winner films)
'''

from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'
res = requests.get(url)
winners = []
if res:
    soup = BeautifulSoup(res.text, 'lxml')
    table = soup.find('table')
    for tr in table.find_all('tr')[1:]:
        tds = tr.find_all_next('td')
        film = tds[0].text
        if tds[0].find('b'):
            year = tds[1].text
            nomin = tds[3].text
            if '[' in nomin:
                nomin = nomin[:nomin.find('[')]
            winner = [film, year, int(nomin)]
            winners.append(winner)
            

else:
    print(res.status_code)
for f in winners:
    print(f'Фильм {f[0]} в {f[1]} году выиграл в {f[2]} номинациях')

