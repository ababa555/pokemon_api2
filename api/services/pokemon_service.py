from ..repositories import IPokemonRepository

class PokemonService:
  def __init__(self, repository:IPokemonRepository):
    self.repository = repository

  def find(self, id, no, version):
    return self.repository.find(id, no, version)