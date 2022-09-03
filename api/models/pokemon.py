from django.db import models
from django.utils import timezone

class Pokemon(models.Model):
  class Meta:
    db_table = 'pokemon'
    ordering = ['no', 'order']
    verbose_name = verbose_name_plural = 'ポケモン'

  id = models.CharField(primary_key=True, max_length=10)
  no = models.IntegerField(verbose_name='No')
  height = models.CharField(verbose_name='高さ', max_length=10)
  weight = models.CharField(verbose_name='重さ', max_length=10)
  order = models.IntegerField(verbose_name='並び順')
  is_default = models.BooleanField(verbose_name='デフォルトフォルム')
  created_at = models.DateTimeField(verbose_name='登録日', default=timezone.now)

  def __str__(self):
    return str(self.id)
