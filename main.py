import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '396a49f53fca255f311a444a711478a1' 
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN,} 

body_create = {
    "name": "sasha",
    "photo_id": 1
}
'''response_create = requests.post(url = f'{URL}/pokemons',headers = HEADER, json = body_create)
message = response_create.json()['message']
print(message)'''



body_new = {
    "pokemon_id": "94070",
    "name": "igor12345",
    "photo_id": 2
}
'''response_new = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_new)
message = response_new.json()['message']
print(message)'''


body_and_pokiball = {
    "pokemon_id": "94070"
}
'''response_pokibool = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER, json = body_new)
message = response_pokibool.json()['message']
print(message)'''