from abc import ABCMeta, abstractmethod
from ..models import PokemonStats

class IPokemonStatsRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, id, version):
    pass

class PokemonStatsRepository(IPokemonStatsRepository):
  def find(self, id=None, version=None):
    list = PokemonStats.objects.all()

    if version:
      list = list.filter(
        id__startswith = version + "-"
      )

    if id:
      list = list.filter(
        pokemon__id__endswith = "-" + id
      )

    return list
