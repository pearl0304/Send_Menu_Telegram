from weather import get_current_weather
from menu import get_food_list
from naver import Naver
from telegram_class import Telegram

naver = Naver()
telegram = Telegram()

current_weather = get_current_weather("Busan")
food_list = get_food_list(current_weather)
search_result = naver.search_naver("서면", food_list)
telegram.send_telegram_message(search_result)