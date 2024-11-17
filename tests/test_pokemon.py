import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '396a49f53fca255f311a444a711478a1' 
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN,} 
TRAINER_ID = '7050'

'''def test_status_code():
    response = requests.get(url= f'{URL}/pokemons',params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200'''

def test_trainer_id():
    response_get = requests.get(url= f'{URL}/pokemons',params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]["trainer_id"] == '7050'