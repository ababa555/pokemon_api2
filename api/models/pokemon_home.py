import uuid
from django.db import models
from ..enums import Pokemon_Home_Data_Type

class PokemonHome(models.Model):

  class Meta:
    db_table = 'pokemon_home'
    verbose_name = verbose_name_plural = 'PokemonHOMEデータ'

  id = models.UUIDField(primary_key=True)
  season_id = models.CharField(max_length=5)
  pokemon_id = models.CharField(max_length=10)
  type = models.CharField(verbose_name='データ種別', max_length=8, choices=Pokemon_Home_Data_Type.choices())
  pokemon_name = models.CharField(verbose_name='ポケモン名', max_length=30)
  name = models.CharField(verbose_name='名称', max_length=10)
  percent = models.FloatField(verbose_name='使用率')

  @classmethod
  def create(cls, season_id, pokemon_id, type, pokemon_name, name, percent):
    entity = cls(
      id=uuid.uuid4(),
      season_id=season_id,
      pokemon_id=pokemon_id,
      type=type,
      pokemon_name=pokemon_name,
      name=name,
      percent=percent)
    # do something with the book
    return entity

  def __str__(self):
    return str(self.id)