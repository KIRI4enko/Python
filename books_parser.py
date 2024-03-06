'''
Парсер книг, их стоимости, UPC, кол-во(10 первых страниц)
Parser of books, their cost, UPC, quantity (first 10 pages)
'''
from bs4 import BeautifulSoup
import requests

base_url = 'https://books.toscrape.com/catalogue/'
pages = {}
for number_page in range(1, 11):
    page = []
    url = base_url + f'category/books_1/page-{number_page}.html'
    res = requests.get(url)
    if res:
        bsoup = BeautifulSoup(res.text, 'lxml')
        for li in bsoup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):
            title = li.findNext('h3').text
            price = li.findNext('p', class_='price_color').text[1::]
            a_book = li.findNext('h3').findNext('a')
            url_book = base_url + a_book['href'][6:]
            res_book = requests.get(url_book)
            if res_book:
                soup_book = BeautifulSoup(res_book.text, 'lxml')
                trs = soup_book.find_all('tr')
                upc = trs[0].findNext('td').text
                availability = trs[5].findNext('td').text
                page.append([title, price, upc, availability])
                print(title, price, upc, availability, '=' * 50, sep='\n')
            else:
                print('Ссылка на книгу не найдена')

        pages[f'{number_page}'] = page
    else:
        print('ERROR!!!')

for num, page in pages.items():
    print(num, page)
