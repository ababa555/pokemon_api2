from django.db import models

from . import Pokemon

class PokemonType(models.Model):
  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

  class Meta:
    db_table = 'pokemon_type'
    ordering = ['id', 'type_id']
    verbose_name = verbose_name_plural = 'ポケモンタイプ'
    constraints = [
      models.UniqueConstraint(
        fields=["pokemon_id", "type_id"],
        name="unique_pokemon_type"
      ),
    ]

  id = models.CharField(primary_key=True, max_length=10)
  type_id = models.CharField(verbose_name='タイプ', max_length=2)
  pokemon = models.ForeignKey(Pokemon, verbose_name='ポケモン', on_delete=models.CASCADE)

  def __str__(self):
    return str(self.id) +  ' ' + self.ability_name
