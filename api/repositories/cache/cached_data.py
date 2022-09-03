from abc import ABCMeta, abstractmethod
import csv
import json
import os
from pathlib import Path
import re
from ...enums import Version_Type, Pokemon_Home_Data_Type
from ...models import Pokemon, PokemonName, PokemonHome

class CachedData:
  _pokemon_data = []
  _pokemon_name_data = []
  _pokemon_home_data = []

  @classmethod
  def pokemon_data(cls):
    return cls._get_or_create_pokemon_data()

  @classmethod
  def pokemon_name_data(cls, refresh=False):
    return cls._get_or_create_pokemon_name_data()

  @classmethod
  def pokemon_home_data(cls, season_id=None, refresh=False):
    return cls._get_or_create_pokemon_home_data(season_id, refresh)

  @classmethod
  def _get_or_create_pokemon_data(cls, refresh=False):
    if cls._pokemon_data and not refresh:
      return cls._pokemon_data

    pokemon_data = []

    base_dir = Path(__file__).resolve().parent.parent.parent.parent
    file_base = "static/csv/"
    versions = ["1-sm", "2-pika_vee", "3-swsh"]

    for index, version in enumerate(versions):
      file_dir = os.path.join(base_dir, file_base, version)
      file_csv = os.path.join(file_dir, "pokemons.csv")
      fp = open(file_csv, 'r')
      reader = csv.reader(fp)
      next(reader, None)

      for record in reader:
        data = Pokemon()
        data.id = record[0]
        data.no = record[1]
        data.height = record[2]
        data.weight = record[3]
        data.order = record[4]
        data.is_default = True if record[5] == "true" else False
        pokemon_data.append(data)
    
    cls._pokemon_data = pokemon_data.copy()
    return cls._pokemon_data

  @classmethod
  def _get_or_create_pokemon_name_data(cls, refresh=False):
    if cls._pokemon_name_data and not refresh:
      return cls._pokemon_name_data

    pokemon_name_data = []

    base_dir = Path(__file__).resolve().parent.parent.parent.parent
    file_base = "static/csv/"
    versions = ["1-sm", "2-pika_vee", "3-swsh"]

    pokemon_data = cls._get_or_create_pokemon_data()

    for index, version in enumerate(versions):
      file_dir = os.path.join(base_dir, file_base, version)
      file_csv = os.path.join(file_dir, "pokemonNames.csv")
      fp = open(file_csv, 'r')
      reader = csv.reader(fp)
      next(reader, None)

      for record in reader:
        data = PokemonName()
        data.id = record[0]
        data.local_language_id = record[1]
        data.name = record[2]
        data.form_name = record[3]
        repatter = re.compile('^.*-')
        result = repatter.match(data.id)
        pokemon_id = data.id[result.start():result.end()-1]
        # data.pokemon = self.get_pokemon(pokemon_id)
        data.pokemon = next(filter(lambda x: x.id == pokemon_id, pokemon_data))
        pokemon_name_data.append(data)

    cls._pokemon_name_data = pokemon_name_data.copy()
    return cls._pokemon_name_data

  @classmethod
  def _get_or_create_pokemon_home_data(cls, season_id, refresh=False):
    base_dir = Path(__file__).resolve().parent.parent.parent.parent

    pokemon_data = cls._get_or_create_pokemon_data()
    pokemon_name_data = cls._get_or_create_pokemon_name_data()

    # seasons = sorted(set([i.name[:5] for i in file_list]), reverse=True)
    if season_id and cls._pokemon_home_data:
      # exits = next(filter(lambda data: data.season_id == season_id, cls._pokemon_home_data))
      exits = any(data.season_id == season_id for data in cls._pokemon_home_data)
      # for i, data in enumerate(cls._pokemon_home_data):
      #   if data['shape'] == 'square':
      #     index = i
      #     break
      if exits and not refresh:
        return cls._pokemon_home_data

    pokemon_home_data = []

    version = str(Version_Type.SWSH.value) # 現状はソードシールド固定
    print(season_id)

    file_path = os.path.join(base_dir, "static/bundle", "bundle.json")
    with open(file_path, 'r') as f:
      pokedex = json.load(f)

    for i in range(1, 6):
      file_path = os.path.join(base_dir, "static/json/pdetail", f"{season_id}-{i}.json")
      with open(file_path, 'r') as f:
        pdetail = json.load(f)
      for pokenum in pdetail.keys():
        for p_detail_id in pdetail[pokenum].keys():
          # pokemons = Pokemon.objects.filter(
          #   id__startswith = version + "-",
          #   no = pokenum
          # )
          pokemons = list(filter(lambda x: x.id.startswith(version + "-") and x.no == pokenum.zfill(3), pokemon_data))

          # シルヴァディ
          if pokenum == "773":
            pokemon = pokemons[0]
          # メガシンカを考慮したフォルムになっている？
          elif int(p_detail_id) > 1 and int(p_detail_id) > len(pokemons) - 1 and pokenum != "773":
            pokemon = pokemons[int(p_detail_id) - 1]
          else:
            pokemon = pokemons[int(p_detail_id)]
          # pokemonName = PokemonName.objects.get(
          #   id = pokemon.id + "-" + "1"
          # )
          pokemonName = next(filter(lambda x: x.id == pokemon.id + "-" + "1", pokemon_name_data))

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
              pokemon_home_data.append(entity)

          if 'tokusei' in pdetail[pokenum][p_detail_id]['temoti']:
            for pokewaza in pdetail[pokenum][p_detail_id]['temoti']['tokusei']:
              entity = PokemonHome.create(season_id, pokemon.id, Pokemon_Home_Data_Type.TOKUSEI.value, name, 
                                          pokedex['tokusei'][pokewaza['id']], pokewaza['val'])
              pokemon_home_data.append(entity)

          if 'seikaku' in pdetail[pokenum][p_detail_id]['temoti']:
            for pokewaza in pdetail[pokenum][p_detail_id]['temoti']['seikaku']:
              entity = PokemonHome.create(season_id, pokemon.id, Pokemon_Home_Data_Type.SEIKAKU.value, name, 
                                          pokedex['seikaku'][pokewaza['id']], pokewaza['val'])
              pokemon_home_data.append(entity)

          if 'motimono' in pdetail[pokenum][p_detail_id]['temoti']:
            for pokewaza in pdetail[pokenum][p_detail_id]['temoti']['motimono']:
              entity = PokemonHome.create(season_id, pokemon.id, Pokemon_Home_Data_Type.MOTIMONO.value, name, 
                                          pokedex['item'][pokewaza['id']], pokewaza['val'])
              pokemon_home_data.append(entity)

    cls._pokemon_home_data = [data for data in cls._pokemon_home_data if data.season_id != season_id]
    cls._pokemon_home_data.extend(pokemon_home_data)
    return cls._pokemon_home_data      
