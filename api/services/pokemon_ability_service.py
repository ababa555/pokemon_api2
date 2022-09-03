from ..repositories import IPokemonAbilityRepository

class PokemonAbilityService:
  def __init__(self, repository:IPokemonAbilityRepository):
    self.repository = repository

  def find(self, id, version):
    return self.repository.find(id, version)