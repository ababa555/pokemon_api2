from ..repositories import IMoveRepository

class MoveService:
  def __init__(self, repository:IMoveRepository):
    self.repository = repository

  def find(self, version):
    return self.repository.find(version)