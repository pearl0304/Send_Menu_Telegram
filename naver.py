import os
import requests
from dotenv import load_dotenv
import urllib

load_dotenv()


class Naver():
  def __init__(self):
    self._naver_client = os.environ.get('NAVER_CLIENT_ID')
    self._naver_client_secret = os.environ.get('NAVER_CLIENT_SECRET')
    self.header = {
      "X-Naver-Client-ID": self._naver_client,
      "X-Naver-Client-Secret": self._naver_client_secret
    }

  def search_naver(self, location, food_list):
    naver_local_url = "https://openapi.naver.com/v1/search/local.json?"
    recommends = []
    result = []

    for food in food_list:
      query = f"{location}{food} 맛집"
      params = f"sort=comment&query={query}&display=5"

      res = requests.get(f"{naver_local_url}{params}", headers=self.header)
      if res.status_code != 200:
        print(f"ERROR SEARCH_NAVER {res.status_code}")
      result_list = res.json().get('items')

      if result_list:
        recommends.append(result_list[0])
        if len(recommends) >= 3:
          break

    for place in recommends:
      title = place.get('title')
      title = title.replace('<b>', '').replace('</b>', '')
      category = place.get('category')
      roadAddress = place.get('roadAddress')

      ## Connect to naver search when click the place
      enc_address = urllib.parse.quote(f"{roadAddress} {title}")
      query = f"query={enc_address}"

      url = f"https://search.naver.com/search.naver?{query}"

      content = {
        "title": title,
        "category": category,
        "url": url
      }
      result.append(content)

    return result
