from requests import get
from re import search


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

url = "https://api.twitch.tv/helix/users?login="
token = "67gnkzlzdlqa1taezidvgay0zdxiuw"
client_id = "r7wkrhz20rr2kmrwrchwyd74xs1nnb"

params = {"Authorization": f"Bearer {token}", "Client-ID": client_id}


def user_twitch_api(param):
    response = get(url + param, headers=params)

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
        # print(f'User {param} returning Bad Request (400)')
        return None
    else:
        print("Erro na solicitação: ", response.text)
        return None
