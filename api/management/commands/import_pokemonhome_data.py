import json
import os
from pathlib import Path

from django.core.management.base import BaseCommand

from ...enums import Version_Type, Pokemon_Home_Data_Type
from ...models import Pokemon, PokemonName, PokemonHome

file_base = "static/csv/"

class Command(BaseCommand):
  def add_arguments(self, parser):
    parser.add_argument('--generation', nargs=1, default=1, required=True)

  def handle(self, *args, **options):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

    file_list = list(Path(os.path.join(BASE_DIR, "static/json/pdetail")).glob('*'))
    seasons = sorted(set([i.name[:5] for i in file_list]), reverse=True)[:int(options['generation'][0])]

    for season_id in seasons:
      version = str(Version_Type.SWSH.value) # 現状はソードシールド固定
      print(season_id)
      insert_list = []

      file_path = os.path.join(BASE_DIR, "static/bundle", "bundle.json")
      with open(file_path, 'r') as f:
        pokedex = json.load(f)

      for i in range(1, 6):
        file_path = os.path.join(BASE_DIR, "static/json/pdetail", f"{season_id}-{i}.json")
        with open(file_path, 'r') as f:
          pdetail = json.load(f)
        for pokenum in pdetail.keys():
          for p_detail_id in pdetail[pokenum].keys():
            pokemons = Pokemon.objects.filter(
              id__startswith = version + "-",
              no = pokenum
            )

            # シルヴァディ
            if pokenum == "773":
              pokemon = pokemons[0]
            # メガシンカを考慮したフォルムになっている？
            elif int(p_detail_id) > 1 and int(p_detail_id) > len(pokemons) - 1 and pokenum != "773":
              pokemon = pokemons[int(p_detail_id) - 1]
            else:
              pokemon = pokemons[int(p_detail_id)]
            pokemonName = PokemonName.objects.get(
              id = pokemon.id + "-" + "1"
            )

            if pokemonName.name == "シルヴァディ":
              name = pokemonName.name + "(" + pokedex['pokeType'][int(p_detail_id)] + ")"
            elif int(p_detail_id) > 0:
              name = pokemonName.name + "(" + pokemonName.form_name + ")"
            else:
              name = pokemonName.name

            if 'waza' in pdetail[pokenum][p_detail_id]['temoti']:
              for pokewaza in pdetail[pokenum][p_detail_id]['temoti']['waza']:
                entity = PokemonHome.create(season_id, pokemon.id, Pokemon_Home_Data_Type.WAZA.value, name, 
                                            pokedex['waza'][pokewaza['id']],pokewaza['val'])
                insert_list.append(entity)

            if 'tokusei' in pdetail[pokenum][p_detail_id]['temoti']:
              for pokewaza in pdetail[pokenum][p_detail_id]['temoti']['tokusei']:
                entity = PokemonHome.create(season_id, pokemon.id, Pokemon_Home_Data_Type.TOKUSEI.value, name, 
                                            pokedex['tokusei'][pokewaza['id']], pokewaza['val'])
                insert_list.append(entity)

            if 'seikaku' in pdetail[pokenum][p_detail_id]['temoti']:
              for pokewaza in pdetail[pokenum][p_detail_id]['temoti']['seikaku']:
                entity = PokemonHome.create(season_id, pokemon.id, Pokemon_Home_Data_Type.SEIKAKU.value, name, 
                                            pokedex['seikaku'][pokewaza['id']], pokewaza['val'])
                insert_list.append(entity)

            if 'motimono' in pdetail[pokenum][p_detail_id]['temoti']:
              for pokewaza in pdetail[pokenum][p_detail_id]['temoti']['motimono']:
                entity = PokemonHome.create(season_id, pokemon.id, Pokemon_Home_Data_Type.MOTIMONO.value, name, 
                                            pokedex['item'][pokewaza['id']], pokewaza['val'])
                insert_list.append(entity)

      # データ削除
      PokemonHome.objects.filter(season_id=season_id).delete()

      # データ登録
      PokemonHome.objects.bulk_create(insert_list)

  def as_json(self):
    json = {
      "waza": [obj.__dict__ for obj in self.waza],
      "tokusei": [obj.__dict__ for obj in self.tokusei],
      "seikaku": [obj.__dict__ for obj in self.seikaku],
      "motimono": [obj.__dict__ for obj in self.motimono],
    }

    return json