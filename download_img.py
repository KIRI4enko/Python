'''
Скачивание картинки
Downloading a picture
'''
from bs4 import BeautifulSoup
import requests
main_url = 'https://books.toscrape.com/'
res = requests.get('https://books.toscrape.com/catalogue/category/books_1/page-1.html')
root = BeautifulSoup(res.text, 'lxml')
img = root.find('img')
img_url = main_url + img['src'][9:]
img_res = requests.get(img_url)
print(img_res)
with open('img.jpg', 'wb') as f:
    f.write(img_res.content)
