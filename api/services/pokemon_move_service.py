from ..repositories import IPokemonMoveRepository

class PokemonMoveService:
  def __init__(self, repository:IPokemonMoveRepository):
    self.repository = repository

  def find(self, id, version):
    return self.repository.find(id, version)