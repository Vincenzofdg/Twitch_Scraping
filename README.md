## Prepering the Inviroment
- Install Python lts;
- `python -m pip install --user --upgrade pip`;
- `python -m pip --version`;
- `python -m pip install --user virtualenv`;
- `python -m venv .venv`;
- `venv\Scripts\activate.bat`;
- `python -m pip install -r requirements.txt`.


`https://api.twitch.tv/helix/users?login=<username>`

```json
{
  "data": [
    {
      "id": "123456",
      "login": "nome_do_usuario",
      "display_name": "Nome do Usuário",
      "type": "parceiro",
      "broadcaster_type": "parceiro",
      "description": "Descrição do usuário",
      "profile_image_url": "https://link_da_imagem_do_perfil",
      "offline_image_url": "https://link_da_imagem_offline_do_usuario",
      "view_count": 123456,
      "email": "email_do_usuario@provedor.com"

    }
  ]
}
```

Para as Pessoas que estiverem transmitindo no momento:

`https://api.twitch.tv/helix/streams?user_id=12345678`
```json
{
  "data": [
    {
      "id": "123456789",
      "user_id": "12345678",
      "user_name": "twitchusername",
      "game_id": "1234",
      "type": "live",
      "title": "Stream Title",
      "viewer_count": 1234,
      "started_at": "2023-03-16T14:30:00Z",
      "language": "en",
      "thumbnail_url": "https://link-to-thumbnail-image.jpg",
      "tag_ids": [
        "1234",
        "5678"
      ],
      "is_mature": false
    }
  ],
  "pagination": {
    "cursor": "eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6MX19"
  }
}

```