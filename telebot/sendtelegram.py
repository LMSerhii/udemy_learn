import requests
from .models import TeleSettings


def send_telegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)

        token = settings.tg_token
        chat_id = settings.tg_chat
        text = settings.tg_message

        text_slise = f"{text}\n" \
                     f"Имя: {tg_name}\n" \
                     f"Телефон: {tg_phone}"

        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'
        data = {
            'chat_id': chat_id,
            'text': text_slise
        }
        try:
            req = requests.post(method, data)
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Все ок')