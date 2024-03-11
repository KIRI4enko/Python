'''
Генерация QR-кода по заданному тексту и размеру
Generating a QR code based on specified text and size
'''
def download_image(title, url):
    with open(f'{title}.jpeg', 'wb') as f:
        f.write(requests.get(url).content)

import requests
data = input('Текст: ')
size = input('Размер QR-кода через "х": ')
url = f'http://api.qrserver.com/v1/create-qr-code/?data={data}&size={size}'

download_image(f'{data},{size}', url)