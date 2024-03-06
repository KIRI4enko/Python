'''
Парсер цитат(1 страница)
Quote parser(1 page)
'''
from bs4 import BeautifulSoup
import requests

res = requests.get('https://quotes.toscrape.com/')
Quotes = []
Authors = []
Tags = []

if res:
    soup = BeautifulSoup(res.text, 'lxml')

    for q in soup.find_all('div', class_='quote'):
        quote = q.find('span', class_='text').text
        author = q.find('small').text
        tags = [i.text for i in q.findAll('a', class_='tag')]

        Quotes.append(quote)
        Authors.append(author)
        Tags.append(tags)

else:
    print(res.status_code)

for i in zip(Quotes,Authors,Tags):
    ans = f'Цитата: {i[0]}\nАвтор: {i[1]}\nТеги: {", ".join(i[2])}'
    print(ans)
    print('='*50)

