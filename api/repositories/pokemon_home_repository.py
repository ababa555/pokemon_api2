from abc import ABCMeta, abstractmethod
from ..models import PokemonHome
from .cache import CachedData

class IPokemonHomeRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, season_id, pokemon_id, type):
    pass

class PokemonHomeRepository(IPokemonHomeRepository):
  def find(self, season_id, pokemon_id, type):
    list = PokemonHome.objects.all()

    if season_id:
      list = list.filter(
        season_id = season_id
      )

    if pokemon_id:
      list = list.filter(
        pokemon_id = pokemon_id
      )

    if type:
      list = list.filter(
        type = type
      )

    return list

class IPokemonHomeInMemoryRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, season_id, pokemon_id, type, refresh):
    pass

class PokemonHomeInMemoryRepository(IPokemonHomeInMemoryRepository):
  def find(self, season_id=None, pokemon_id=None, type=None, refresh=None):
    list_data = CachedData.pokemon_home_data(season_id, refresh)
    
    if season_id:
      list_data = list(filter(lambda x: x.season_id == season_id, list_data))

    if pokemon_id:
      list_data = list(filter(lambda x: x.pokemon_id == pokemon_id, list_data))
    
    if type:
      list_data = list(filter(lambda x: x.type == type, list_data))

    return list_data
