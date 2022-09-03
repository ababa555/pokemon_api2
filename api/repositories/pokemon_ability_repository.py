from abc import ABCMeta, abstractmethod
from ..models import PokemonAbility

class IPokemonAbilityRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, id, version):
    pass

class PokemonAbilityRepository(IPokemonAbilityRepository):
  def find(self, id=None, version=None):
    list = PokemonAbility.objects.all()

    if id:
      list = list.filter(
        pokemon__id__endswith = "-" + id
      )

    if version:
      list = list.filter(
        id__startswith = version + "-"
      )

    return list