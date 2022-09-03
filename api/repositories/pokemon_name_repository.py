from abc import ABCMeta, abstractmethod
import csv
import os
from pathlib import Path
import re
from ..models import Pokemon, PokemonName
from .cache import CachedData

class IPokemonNameRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, id, version, local_language_id, name):
    pass

class PokemonNameRepository(IPokemonNameRepository):
  def find(self, id=None, version=None, local_language_id=None, name=None):
    list = PokemonName.objects.all()
    
    if version:
      list = list.filter(
        id__startswith = version + "-"
      )
 
    if id:
      list = list.filter(
        pokemon__id__endswith = "-" + id
      )

    if local_language_id:
      list = list.filter(
        local_language_id = local_language_id
      )

    if name:
      list = list.filter(
        name__icontains = name
      )

    return list

class IPokemonNameInMemoryRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, id, version, local_language_id, name):
    pass

class PokemonNameInMemoryRepository(IPokemonNameInMemoryRepository):
  def find(self, id=None, version=None, local_language_id=None, name=None, refresh=None):
    list_data = CachedData.pokemon_name_data(refresh)
    
    if version:
      list_data = list(filter(lambda x: x.id.startswith(version + "-"), list_data))

    if id:
      list_data = list(filter(lambda x: x.pokemon.id.endswith("-" + id), list_data))
    
    if local_language_id:
      list_data = list(filter(lambda x: x.local_language_id == local_language_id, list_data))
    
    if name:
      list_data = list(filter(lambda x: x.name.contains(name), list_data))

    return list_data
