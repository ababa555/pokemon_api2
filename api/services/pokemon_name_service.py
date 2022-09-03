from ..repositories import IPokemonNameRepository

class PokemonNameService:
  def __init__(self, repository:IPokemonNameRepository):
    self.repository = repository

  def find(self, id, version, local_language_id, name):
    return self.repository.find(id, version, local_language_id, name)

  def findForInMemory(self, id, version, local_language_id, name, refresh):
    return self.repository.find(id, version, local_language_id, name, refresh)