import requests
import os
from twilio.rest import Client

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key=os.environ.get("OWM_API_KEY")
account_sid = "ACabb6c10fc2b521c4ab8bdd615749e0fa"
auth_token =os.environ.get("AUTH_TOKEN")

weather_params={
    'appid':api_key,
    'lat':12.971599,
    'lon':77.594566,
    #'lat':45.15,
    #'lon':60.30,
    'cnt':4
}

response=requests.get(url=OWM_Endpoint,params=weather_params)
# print(response.status_code)
response.raise_for_status()
weather_data=response.json()
# print(weather_data['list'][0]['weather'][0]['id'])
will_rain=False
for hour_data in weather_data['list']:
    condition_code=hour_data['weather'][0]['id']
    print(condition_code)
    if int(condition_code)<700:
        will_rain=True

if will_rain:
    # print("Bring an Umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today,Remember to bring ☂️",
        from_="+14783129255",
        to="+919980362734",
    )
    print(message.status)
