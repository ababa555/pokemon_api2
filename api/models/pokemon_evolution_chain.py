from django.db import models

from . import Pokemon

class PokemonEvolutionChain(models.Model):
  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

  class Meta:
    db_table = 'pokemon_evolution_chain'
    ordering = ['id', 'evolution_chain_id']
    verbose_name = verbose_name_plural = 'ポケモン進化'
    constraints = [
      models.UniqueConstraint(
        fields=["pokemon_id", "evolution_chain_id"],
        name="unique_pokemon_evolution_chain"
      ),
    ]

  id = models.CharField(primary_key=True, max_length=10)
  evolution_chain_id = models.CharField(verbose_name='特性名', max_length=10)
  order = models.IntegerField(verbose_name='並び順')
  pokemon = models.ForeignKey(Pokemon, verbose_name='ポケモン', on_delete=models.CASCADE)

  def __str__(self):
    return str(self.id) +  ' ' + str(self.evolution_chain_id)
