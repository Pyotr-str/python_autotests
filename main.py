import requests

URL = 'https://api.pokemonbattle.ru/'
TOKEN = 'dfcb14fb66d08c96a81bb6560ad3d7fc'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "gilletteseries@yandex.ru",
    "password": "kanopus3D%1",
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "КисчЁнка",
    "photo_id": 52
}
body_rename = {
    "pokemon_id": "424478",
    "name": "Жорка",
    "photo_id": 509
}
body_in_pokeball = {
    "pokemon_id": "424478"
}

response = requests.post(url = f'{URL}trainers/reg', headers = HEADER, json = body_registration)
print(response)

'''response_create = requests.post(url = f'{URL}v2/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''body_rename = requests.put(url = f'{URL}v2/pokemons', headers = HEADER, json = body_rename)
print(body_rename.text)'''

'''body_in_pokeball = requests.post(url = f'{URL}v2/trainers/add_pokeball', headers = HEADER, json = body_in_pokeball)
print(body_in_pokeball.text)'''