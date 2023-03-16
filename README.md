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