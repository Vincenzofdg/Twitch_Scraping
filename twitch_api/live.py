from requests import get
from dotenv import dotenv_values

env = dotenv_values(".env")

headers = {
    "Authorization": f"Bearer {env['token']}", "Client-ID": env["client_id"]}

params = {
    "first": 100,
    "language": env["language"],
    "sort": "viewer_count",
    # 'sort': 'average_viewer_count',
    # 'average_viewer_count': f"{env['avg_min']}..{env['avg_max']}"
}


def streamers_live():
    streamers = []
    streamers_info = []
    qtd_found = 0
    cursor = None

    while True:
        if cursor:
            params["after"] = cursor

        response = get(env["url_live"], headers=headers, params=params)

        if response.status_code == 200:
            results = response.json()["data"]
            streamers += results

            if (
                "pagination" in response.json()
                and "cursor" in response.json()["pagination"]
            ):
                cursor = response.json()["pagination"]["cursor"]
            else:
                break
        else:
            print(
                "Erro ao fazer solicitação HTTP: ", response.status_code, response.text
            )
            break

    for streamer in streamers:
        if int(env['avg_min']) <= streamer["viewer_count"] <= int(env['avg_max']):
            qtd_found += 1
            streamers_info.append(
                [
                    streamer["user_name"],
                    streamer["viewer_count"],
                    f"https://www.twitch.tv/{streamer['user_login']}",
                ]
            )

    return {"Streamers": streamers_info, "Results": qtd_found}


# {
#   "data": [
#     {
#       "id": "12345678",
#       "user_id": "98765432",
#       "user_name": "TwitchUsername",
#       "game_id": "21779",
#       "type": "live",
#       "title": "Example Stream Title",
#       "viewer_count": 123,
#       "started_at": "2022-03-16T00:00:00Z",
#       "language": "en",
#       "thumbnail_url": "https://link-to-thumbnail.jpg",
#       "tag_ids": [
#         "6ea6bca4-4712-4ab9-a906-e3336a9d8039"
#       ],
#       "is_mature": false
#     }
#   ],
#   "pagination": {}
# }
