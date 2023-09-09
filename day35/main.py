import requests
import os


def telegram_bot_send_text(bot_message):
    bot_token = os.environ.get("BOT_TOKEN")
    bot_chat_id = os.environ.get("BOT_CHAT_ID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id \
                + '&parse_mode=Markdown&text=' + bot_message

    bot_response = requests.get(send_text)
    return bot_response.json()


api_key = os.environ.get("API_KEY")

parameters = {
    "lat": 50.438215,
    "lon": 30.624366,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour in range(12):
    weather_id = (weather_data['hourly'][hour]['weather'][0]['id'])
    if weather_id < 700:
        will_rain = True

if will_rain:
    message = "Vlad, it's probably going to rain 🌧️today, bring an umbrella ☔️ with you."
    telegram_bot_send_text(message)