from rest_framework import status, views
from rest_framework.response import Response
import requests
import json

# http://127.0.0.1:8000/api/seasons
class SeasonAPIView(views.APIView):  
  def get(self, request, format=None):
    seasons = self.get_seasons()
    text = seasons.text
    response = json.loads(json.loads(json.dumps(text)))
    if response["code"] != 200:
      return

    return Response(response["list"], status.HTTP_200_OK)

  def get_seasons(self):
    headers = {
      'accept': 'application/json, text/javascript, */*; q=0.01',
      'countrycode': '304',
      'authorization': 'Bearer',
      'langcode': '1',
      'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
    }

    json_data = {
      'soft': 'Sw',
    }

    response = requests.post('https://api.battle.pokemon-home.com/cbd/competition/rankmatch/list', headers=headers, json=json_data)

    return response
