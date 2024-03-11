'''
Парсер студентов
Parser students
'''
from bs4 import BeautifulSoup
import requests

main_url = 'https://rating.unecon.ru/'
url = main_url + 'index.php'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
courses = soup.find('li')
peoples = []
for a in courses.find_all('a'):
    if a.text == '4 курс':
        url_course = main_url + a['href']
        course_get = requests.get(url_course)
        soup_course = BeautifulSoup(course_get.text, 'lxml')
        napravs = soup_course.find_all('li')[3]
        for div in napravs.find_all('div', class_='options'):
            for a in div.findAllNext('a')[1:2]:
                url_naprav = main_url + a['href']
                naprav_get = requests.get(url_naprav)
                soup_naprav = BeautifulSoup(naprav_get.text, 'lxml')
                table = soup_naprav.find('table')
                tbody = table.find('tbody')
                for tr in tbody.find_all('tr'):
                    tds = tr.find_all('td')
                    cnt_pred = 0
                    full_name = tds[1].text
                    if full_name == '':
                        continue
                    number_group = tds[2].text
                    for pred in tds[3:-1]:
                        if pred.text != '':
                            cnt_pred += 1

                    try:
                        e_ball = float(tds[-1].text) / cnt_pred
                    except:
                        e_ball = 0
                    if e_ball > 100:
                        print(a.text)
                        print(full_name,number_group,e_ball)
                    peoples.append([e_ball, number_group, full_name])

peoples.sort()
for p in peoples[::-1]:
    print(*p,sep='\n')
    print('='*50)
