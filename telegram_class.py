import json

import telegram
import os
from dotenv import load_dotenv

load_dotenv()


class Telegram():
  def __init__(self):
    self._api = os.environ.get('TELEGRAM_API_KEY')
    self._chat_id = os.environ.get('TELECRAM_CHAT_ID')
    self.bot = telegram.Bot(token=self._api)

  def send_telegram_message(self, search_result):
    for item in search_result:
      category = item['category']
      title = item['title']
      url = item['url']
      text = f"[{title}]({url})"
      self.bot.sendMessage(self._chat_id, text=text, parse_mode="Markdown")
