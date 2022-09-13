import requests
import os
from dotenv import load_dotenv

load_dotenv()


## 섭씨 온도 &units=metric <-추가하기
def get_current_weather(city_name):
  appid = os.environ.get('OPEN_WEATHER_API_KEY')
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={appid}"
  res = requests.get(url)
  if res.status_code != 200:
    print(f"ERROR OF GET CURRENT WEATHER, {res.status_code}")
  else:
    weather = res.json().get("weather")
    current_weather = weather[0]
    main = res.json().get("main")
    current_weather['temp'] = round(main['temp'])
    return current_weather
