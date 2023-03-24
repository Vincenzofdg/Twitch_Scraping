import requests
from dotenv import dotenv_values

env = dotenv_values('.env')

# Dados para enviar na solicitação
data = {
    "client_id": env['client_id'],
    "client_secret": env['client_secret'],
    "grant_type": "client_credentials"
}

# Fazer a solicitação POST
response = requests.post(env['url_token'], data=data)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    token = response.json()["access_token"]
    print("Token gerado com sucesso: ", token)
else:
    print("Erro na solicitação: ", response.text)
