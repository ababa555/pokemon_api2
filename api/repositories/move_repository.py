from abc import ABCMeta, abstractmethod
from ..models import Move

class IMoveRepository(metaclass=ABCMeta):
  @abstractmethod
  def find(self, version):
    pass

class MoveRepository(IMoveRepository):
  def find(self, version=None):
    list = Move.objects.all()

    if version:
      list = list.filter(
        id__startswith = version + "-"
      )

    return list