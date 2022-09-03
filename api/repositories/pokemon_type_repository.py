from abc import ABCMeta, abstractmethod
from ..models import PokemonType

class IPokemonTypeRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, id, version):
    pass

class PokemonTypeRepository(IPokemonTypeRepository):
  def find(self, id=None, version=None):
    list = PokemonType.objects.all()

    if version:
      list = list.filter(
        id__startswith = version + "-"
      )

    if id:
      list = list.filter(
        pokemon__id__endswith = "-" + id
      )

    return list
