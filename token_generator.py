from requests import post
from dotenv import dotenv_values

env = dotenv_values('.env')

data = {
    "client_id": env['client_id'],
    "client_secret": env['client_secret'],
    "grant_type": "client_credentials"
}

# Fazer a solicitação POST
response = post(env['url_token'], data=data)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    token = response.json()["access_token"]
    print("Add the following token into your env file: ", token)
else:
    print("Request Error: ", response.text)
