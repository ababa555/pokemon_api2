from django.db import models

from . import Pokemon

class PokemonMove(models.Model):
  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

  class Meta:
    db_table = 'pokemon_move'
    ordering = ['id', 'move_name']
    verbose_name = verbose_name_plural = 'ポケモン技'
    constraints = [
      models.UniqueConstraint(
        fields=["pokemon_id", "move_name"],
        name="unique_pokemon_move"
      ),
    ]

  id = models.CharField(primary_key=True, max_length=10)
  move_name = models.CharField(verbose_name='技名', max_length=10)
  pokemon = models.ForeignKey(Pokemon, verbose_name='ポケモン', on_delete=models.CASCADE)

  def __str__(self):
    return str(self.id) +  ' ' + self.move_name
