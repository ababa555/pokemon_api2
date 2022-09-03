from ..repositories import IPokemonStatsRepository

class PokemonStatsService:
  def __init__(self, repository:IPokemonStatsRepository):
    self.repository = repository

  def find(self, id, version):
    return self.repository.find(id, version)