from ..repositories import IPokemonTypeRepository

class PokemonTypeService:
  def __init__(self, repository:IPokemonTypeRepository):
    self.repository = repository

  def find(self, id, version):
    return self.repository.find(id, version)