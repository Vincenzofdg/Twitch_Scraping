from requests import get
from dotenv import dotenv_values
from re import search

env = dotenv_values('.env')

headers = {
    "Authorization": f"Bearer {env['token']}",
    "Client-ID": env['client_id']
}

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def get_email(param):
    response = get(env['url_user'] + param, headers=headers)

    if response.status_code == 200:
        res = response.json()["data"]

        if res == []:
            return None
        else:
            data = res[0]
            if "email" in data:
                return ["email"]
            elif "description" in data:
                email = search(regex, data["description"])
                if email:
                    return email.group(0)
                else:
                    return None

    elif response.status_code == 400:
        return None
    else:
        print("Erro na solicitação: ", response.text)
        return None

# {
#   "data": [
#     {
#       "id": "12345678",
#       "login": "twitchusername",
#       "display_name": "Twitch Username",
#       "type": "",
#       "broadcaster_type": "",
#       "description": "",
#       "profile_image_url": "https://link-to-profile-image.jpg",
#       "offline_image_url": "https://link-to-offline-image.jpg",
#       "view_count": 1234,
#       "email": "email@example.com"
#     }
#   ],
#   "pagination": {}
# }
