import requests


class SuperHero:
    def __init__(self, token):
        self.token = token
        if self.token == '':
            print('Укажите токен')

    def most_intelligent_superhero(self, heroes):
        heroes_dict = {}
        most_intelligent_heroes = {}
        for hero in heroes:
            url = f'https://www.superheroapi.com/api/{self.token}/search/{hero}'
            if requests.get(url).status_code == 200:
                response = (requests.get(url)).json()
                for item in response['results']:
                    if item['name'] == hero:
                        heroes_dict[hero] = int(item['powerstats']['intelligence'])
            else:
                print('Ошибка')
        max_intelligence = max(heroes_dict.values())
        most_intelligent_heroes = {k:v for k, v in heroes_dict.items() if v == max_intelligence}
        heroes_list = list(most_intelligent_heroes.keys())
        if len(most_intelligent_heroes) == 1:
            print(f'{heroes_list[0]} самый умный супергерой.\n')
        else:
            print(f'Самые умные супергерои: {", ".join(heroes_list)}\n')


