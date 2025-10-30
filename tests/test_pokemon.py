import requests
import pytest

URL = 'https://api.pokemonbattle.ru/'
TOKEN = 'dfcb14fb66d08c96a81bb6560ad3d7fc'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '38733'

def test_status_code():
    response = requests.get(url = f'{URL}v2/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}v2/pokemons', params = {'trainer_id' : TRAINER_ID})
    print('trainer_id.text: {38733}')
    assert response_get.json()["data"][0]["name"] == 'Ури'

@pytest.mark.parametrize('key, value', [('name', 'Ури'), ('trainer_id', TRAINER_ID), ('id', '522287')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}v2/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value