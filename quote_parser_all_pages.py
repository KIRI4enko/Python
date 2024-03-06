'''
    Парсер цитат(все страницы)
    Quote parser (all pages)
'''
from bs4 import BeautifulSoup
import requests
number_page = 1
res = requests.get(f'https://quotes.toscrape.com/')
Quotes = []
Authors = []
Tags = []


if res:
    soup = BeautifulSoup(res.text, 'lxml')
    while True:
        soup = BeautifulSoup(res.text, 'lxml')
        print(number_page)
        for q in soup.find_all('div', class_='quote'):
            quote = q.find('span', class_='text').text
            author = q.find('small').text
            tags = [i.text for i in q.findAll('a', class_='tag')]
            print(quote,author,sep='\n')
            print(*tags,sep=', ')
            print('='*70)
            Quotes.append(quote)
            Authors.append(author)
            Tags.append(tags)
        if soup.find('li', class_='next'):
            number_page += 1
            res = requests.get(f'https://quotes.toscrape.com/page/{number_page}')
        else:
            break

else:
    print(res.status_code)

