from decor import decoration_params
import requests

token = '2619421814940190'
urls = [
    f'https://superheroapi.com/api/{token}/search/Hulk',
    f'https://superheroapi.com/api/{token}/search/Captain America',
    f'https://superheroapi.com/api/{token}/search/Thanos'
]

@decoration_params()
def get_urls(url_all):
    r = (requests.get(url) for url in url_all)
    return r

@decoration_params()
def get_hero_list():
    heroes = []
    for item in get_urls(urls):
        intelligence = item.json()
        for stats in intelligence['results']:
            heroes.append({
                'name': stats['name'],
                'intelligence': stats['powerstats']['intelligence']
            })
    return heroes

@decoration_params()
def compare():
    int_hero = 0
    name_hero = ''
    for hero in get_hero_list():
        if int_hero < int(hero['intelligence']):
            int_hero = int(hero['intelligence'])
            name_hero = hero['name']
    return f'Самый умный герой {name_hero}'


if __name__ == '__main__':
    # get_urls(urls)
    compare()