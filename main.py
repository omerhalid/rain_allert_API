import requests
import twilio.rest import Client
import os

#env olarak kaydettim api keyimi (export OWM_API_KEY=sifre)
api_key = os.environ.get("OWM_API_KEY")

MY_LAT = "47.497913"
MY_LONG = "19.040236"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = "AC7c357bb2c70d78979800071781270f39"
auth_token = "0549b71f9a1e07f77368c2e0bac53485"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(response.status_code)

# if weather_data["hourly"][0]["weather"][0]["id"] < 700:
#     print("Bring an umbrella")

will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.nessages \
        .create(
        body="It is going to rain today.",
        from="+..",
        to="+.."
    )

    print(message.status)
