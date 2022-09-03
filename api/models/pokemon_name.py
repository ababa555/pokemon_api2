from django.db import models

from . import Pokemon

class PokemonName(models.Model):
  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

  class Meta:
    db_table = 'pokemon_name'
    ordering = ['pokemon_id', 'local_language_id']
    verbose_name = verbose_name_plural = 'ポケモン名'
    constraints = [
      models.UniqueConstraint(
        fields=["pokemon_id", "local_language_id"],
        name="unique_pokemon_name"
      ),
    ]

  id = models.CharField(primary_key=True, max_length=10)
  local_language_id = models.IntegerField(verbose_name='言語')
  name = models.CharField(verbose_name='ポケモン名', max_length=10)
  form_name = models.CharField(verbose_name='フォルム名', max_length=20, null=True, blank=True)
  pokemon = models.ForeignKey(Pokemon, verbose_name='ポケモン', on_delete=models.CASCADE)

  def __str__(self):
    name = self.name
    form_name = '' if not self.form_name else '（{}）'.format(self.form_name)
    return str(self.id) +  ' ' + name +  ' ' + form_name
