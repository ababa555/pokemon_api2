from django.db import models

from . import Pokemon

class PokemonAbility(models.Model):
  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

  class Meta:
    db_table = 'pokemon_ability'
    ordering = ['id', 'ability_name']
    verbose_name = verbose_name_plural = 'ポケモン特性'
    constraints = [
      models.UniqueConstraint(
        fields=["pokemon_id", "ability_name"],
        name="unique_pokemon_ability"
      ),
    ]

  id = models.CharField(primary_key=True, max_length=10)
  ability_name = models.CharField(verbose_name='特性名', max_length=10)
  is_hidden = models.BooleanField(verbose_name='隠れ特性')
  pokemon = models.ForeignKey(Pokemon, verbose_name='ポケモン', on_delete=models.CASCADE)

  def __str__(self):
    return str(self.id) +  ' ' + self.ability_name
