from ..repositories import IPokemonHomeRepository

class PokemonHomeService:
  def __init__(self, repository:IPokemonHomeRepository):
    self.repository = repository

  def find(self, season_id, pokemon_id, type):
    return self.repository.find(season_id, pokemon_id, type)

  def findForInMemory(self, season_id, pokemon_id, type, refresh):
    return self.repository.find(season_id, pokemon_id, type, refresh)