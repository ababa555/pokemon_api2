from abc import ABCMeta, abstractmethod
from ..models import Pokemon

class IPokemonRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, id, no, version):
    pass

class PokemonRepository(IPokemonRepository):
  def find(self, id=None, no=None, version=None):
    list = Pokemon.objects.all()

    if version:
      list = list.filter(
        id__startswith = version + "-"
      )

    if id:
      list = list.filter(
        id__endswith = id
      )

    if no:
      list = list.filter(
        no = no
      )

    return list