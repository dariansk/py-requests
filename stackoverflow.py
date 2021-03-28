import requests
import time


class StackoverflowApi:
    def __init__(self, site='stackoverflow'):
        self.site = site

    def get_python_questions(self,tag):
        url = 'https://api.stackexchange.com/2.2/search'
        params = {'page': 1, 'pagesize': 100, 'order': 'desc',
                  'min': int(time.time()) - 172800, 'sort': 'creation', 'tagged': tag, 'site': self.site}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(f'Список вопросов за последние два дня по тегу {tag} с сайта {self.site}:')
            while response.json()['has_more']:
                for elements in response.json()['items']:
                    print(elements['title'])
                    print(elements['link'])
                    with open('stackoverflow_python.txt', 'a', encoding='utf=8') as file:
                        file.write(elements['title'])
                        file.write('\n')
                        file.write(elements['link'])
                        file.write('\n')
                        file.write('\n')
                params['page'] += 1
                response = requests.get(url, params=params)
        else:
            print('Что-то пошло не так.')