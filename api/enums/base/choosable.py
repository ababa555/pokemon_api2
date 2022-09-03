from enum import IntFlag

class choosable(IntFlag):
  @classmethod
  def choices(cls):
    return [(m.name, m.value) for m in cls]
        
  @classmethod
  def contains(cls, val):
    return val in [m.name for m in cls]