import requests

def get_arid_planets_films(data):
    arid_planet_films = 0
    for film in data['results']:
        for planet in film['planets']:
            planet_data = requests.get(planet).json()
            if planet_data['climate'] == 'arid':
                arid_planet_films += 1
                break
    return arid_planet_films

def get_wookies_count(data):
    wookies = 0
    for character in data['results'][-1]['characters']:
        character_data = requests.get(character).json()
        if 'https://swapi.dev/api/species/3/' in character_data['species']:
            wookies += 1
    return wookies

def get_largest_starship(data):
    largest_starship = {'name': '', 'length': 0}
    for starship in data['results']:
        length = float(starship['length'].replace(',', '.'))
        if largest_starship['length'] < length:
            largest_starship['name'] = starship['name']
            largest_starship['length'] = length
    return largest_starship['name']

data = requests.get('https://swapi.dev/api/films').json()

arid_planet_films = get_arid_planets_films(data)
wookies = get_wookies_count(data)
largest_starship_name = get_largest_starship(requests.get('https://swapi.dev/api/starships/').json())

print('¿En cuántas películas aparecen planetas cuyo clima sea árido?')
print(arid_planet_films)
print('¿Cuántos Wookies aparecen en la sexta película?')
print(wookies)
print('¿Cuál es el nombre de la aeronave más grande en toda la saga?')
print(largest_starship_name)
