from abc import ABCMeta, abstractmethod
from ..models import PokemonEvolutionChain

class IPokemonEvolutionChainRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, id, version):
    pass

class PokemonEvolutionChainRepository(IPokemonEvolutionChainRepository):
  def find(self, id=None, version=None):
    list = PokemonEvolutionChain.objects.all()

    if id:
      list = list.filter(
        pokemon__id__endswith = "-" + id
      )

    if version:
      list = list.filter(
        id__startswith = version + "-"
      )

    return list
