import requests
import os
from dotenv import load_dotenv
load_dotenv()

class Naver():
  def __init__(self):
    self._naver_client = os.environ.get('NAVER_CLIENT_ID')
    self._naver_client_secret = os.environ.get('NAVER_CLIENT_SECRET')
    self.header = {
      "X-Naver-Client-ID": self._naver_client,
      "X-Naver-Client-Secret": self._naver_client_secret
    }