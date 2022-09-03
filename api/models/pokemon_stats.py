from django.db import models

from . import Pokemon

class PokemonStats(models.Model):
  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

  class Meta:
    db_table = 'pokemon_stats'
    ordering = ['id']
    verbose_name = verbose_name_plural = 'ポケモン種族値'

  id = models.CharField(primary_key=True, max_length=10)
  hp = models.IntegerField(verbose_name='HP')
  attack = models.IntegerField(verbose_name='こうげき')
  defense = models.IntegerField(verbose_name='ぼうぎょ')
  sp_attack = models.IntegerField(verbose_name='とくこう')
  sp_defense = models.IntegerField(verbose_name='とくぼう')
  speed = models.IntegerField(verbose_name='すばやさ')
  pokemon = models.ForeignKey(Pokemon, verbose_name='ポケモン', on_delete=models.CASCADE)

  def __str__(self):
    return str(self.id)
