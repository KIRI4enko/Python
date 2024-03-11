'''
Парсер Stackoverflow
Parser Stackoverflow
'''
from bs4 import BeautifulSoup
import requests


def stringing(string):
    az = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    az += az.lower() + '0123456789'
    flag = ''
    for i in string:
        if i in az:
            flag += i
    return flag


main_url = 'https://stackoverflow.com'
request = requests.get(main_url + '/users')
if request:
    soup_main = BeautifulSoup(request.text, 'lxml')
    list_users = soup_main.find('div', class_='d-grid grid__4 lg:grid__3 md:grid__2 sm:grid__1 g12')
    for user in list_users.find_all('div', class_='grid--item'):
        user_details = user.find('div', class_='user-details')
        user_a = user_details.find('a')
        user_name = stringing(user_a.text)
        user_url = main_url + user_a['href']
        request_user = requests.get(user_url)
        if request_user:
            soup_user = BeautifulSoup(request_user.text, 'lxml')
            user_stats = soup_user.find('div', class_='s-card fc-light bar-md').find_all('div',
                                                                                         class_='flex--item md:fl-auto')
            user_answers = stringing(user_stats[2].find('div').text)
            user_question = stringing(user_stats[3].find('div').text)
            number_page = 1
            badges_url = user_url + f'?tab=badges&sort-recent&page={number_page}'
            request_user_badges = requests.get(badges_url)
            list_badges = []
            cnt_pages = 1
            if request_user_badges:
                soup_badges = BeautifulSoup(request_user_badges.text, 'lxml')
                cnt_pages = int(
                soup_badges.find('div', class_='s-pagination site1 themed pager float-right').find_all('a')[-2].text
                                )
            else:
                print(request_user_badges.status_code)
            while number_page <= cnt_pages:
                badges_url = user_url + f'?tab=badges&sort-recent&page={number_page}'
                request_user_badges = requests.get(badges_url)
                if request_user_badges:
                    soup_badges = BeautifulSoup(request_user_badges.text, 'lxml')
                    div_badges = soup_badges.find('div',
                                                  class_='d-grid g16 grid__4 lg:grid__3 md:grid__2 sm:grid__1 py8')
                    for badge in div_badges.find_all('div', class_='grid--item'):
                        name_badge = badge.find('a').text
                        name_badge = name_badge.replace('\xa0', '')
                        list_badges.append(name_badge)
                else:
                    print(request_user_badges.status_code)
                number_page += 1
            print(f'{user_name}: {user_answers} answers, {user_question} questions \n'
                  f'Badges: {", ".join(list_badges)}.\n')
        else:
            print(request_user.status_code)
else:
    print(request.status_code)
