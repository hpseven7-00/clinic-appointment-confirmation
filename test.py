import requests

def enviar_template_whatsapp(token: str, phone_number_id: str, to: str) -> dict:
    url = f"https://graph.facebook.com/v25.0/{phone_number_id}/messages"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {"code": "en_US"}
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if not response.ok:
        raise Exception(f"Erro {response.status_code}: {response.text}")

    return response.json()

resposta = enviar_template_whatsapp(
    token="EAAX26DVFAigBRdkiYThxgZAxPynYkoydvAyoB2jauai40D6bRFHZBDZA08dc8loZB32wZCLxhfMEHZClja9Yx0GHBxFznrWEU4EnKhtJweM4b1gJO3OZC8x9fUEKHnNRRCx41gEyEvfzJMTVT4XktApZCZBeNwHbntwew698WsFPcGoaZBT1KP7rP5ZAzkvpgZAkbWh5sTaqM3juhW4q0ZCaEEmFQdkvIiw8R3XZAGee3bIEzDVa3AaPIbBKrW2VXmR5ocAmNScddkLoMXuh3tg5RH3MzB8M7ZC",
    phone_number_id="1125211887336698",
    to="5599984864678"
)

print(resposta)