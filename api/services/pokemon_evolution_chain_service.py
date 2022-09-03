from ..repositories import IPokemonEvolutionChainRepository

class PokemonEvolutionChainService:
  def __init__(self, repository:IPokemonEvolutionChainRepository):
    self.repository = repository

  def find(self, id, version):
    return self.repository.find(id, version)