from ast import Not
from operator import truediv
import requests
import json
import os
from pathlib import Path

from django.core.management.base import BaseCommand 

class Command(BaseCommand):
  def add_arguments(self, parser):
    parser.add_argument('--generation', nargs=1, default=1, required=True)
    parser.add_argument('--seasons', nargs='+')

  def handle(self, *args, **options):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    FILE_DIR = os.path.join(BASE_DIR, "static/json/pdetail")

    response = self.get_seasons()

    responseText = response.text
    responseJson = json.loads(json.loads(json.dumps(responseText)))
    if responseJson["code"] != 200:
      return

    seasons = responseJson["list"]
    targetSeasonIndexes = sorted(set([int(i) for i in seasons]), reverse=True)[:int(options['generation'][0])]
    
    os.makedirs(FILE_DIR, exist_ok=True)

    for i in targetSeasonIndexes:
      season = seasons[str(i)]
    
      for season_id in season:
        target_season = season[season_id]
        id = season_id
        rst = target_season["rst"]
        ts2 = target_season["ts2"]
      
        for i in range(1, 6):
          pdetails = self.get_pdetails(id, rst, ts2, i)
          file_path = os.path.join(FILE_DIR, f"{id}-{i}.json")
          with open(file_path, mode='w') as f:
            data = pdetails.json()
            json.dump(data, f, ensure_ascii=False, indent=2)

  def get_pokemons(self, id, rst, ts2):
    headers = {
      'accept': 'application/json',
      'user-agent': 'user-agent: Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
    }

    response = requests.get(f'https://resource.pokemon-home.com/battledata/ranking/{id}/{rst}/{ts2}/pokemon', headers)

    return response

  def get_pdetails(self, id, rst, ts2, i):
    headers = {
      'accept': 'application/json',
      'user-agent': 'user-agent: Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
    }

    response = requests.get(f'https://resource.pokemon-home.com/battledata/ranking/{id}/{rst}/{ts2}/pdetail-{i}', headers)

    return response

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
