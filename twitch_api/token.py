import requests

client_id = "r7wkrhz20rr2kmrwrchwyd74xs1nnb"
client_secret = "yghcoo6hdbnp81yym8x5oakounod8j"

# URL para fazer a solicitação de token
url = "https://id.twitch.tv/oauth2/token"

# Dados para enviar na solicitação
data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}

# Fazer a solicitação POST
response = requests.post(url, data=data)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    token = response.json()["access_token"]
    print("Token gerado com sucesso: ", token)
else:
    print("Erro na solicitação: ", response.text)
