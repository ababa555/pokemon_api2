from abc import ABCMeta, abstractmethod
from ..models import PokemonMove

class IPokemonMoveRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, id, version):
    pass

class PokemonMoveRepository(IPokemonMoveRepository):
  def find(self, id=None, version=None):
    list = PokemonMove.objects.all()

    if version:
      list = list.filter(
        id__startswith = version + "-"
      )
    
    if id:
      list = list.filter(
        pokemon__id__endswith = "-" + id
      )

    return list
