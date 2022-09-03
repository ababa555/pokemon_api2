from django.db import models

class Move(models.Model):
  class Meta:
    db_table = 'move'
    ordering = ['id']
    verbose_name = verbose_name_plural = '技'

  id = models.CharField(primary_key=True, max_length=10)
  name = models.CharField(verbose_name='技名', max_length=10)
  type = models.CharField(verbose_name='タイプ', max_length=1)
  power1 = models.CharField(verbose_name='威力1', max_length=3)
  power2 = models.CharField(verbose_name='威力2', max_length=3)
  pp = models.CharField(verbose_name='PP', max_length=2)
  accuracy = models.CharField(verbose_name='命中', max_length=3)
  priority = models.CharField(verbose_name='優先度', max_length=3)
  damage_type = models.CharField(verbose_name='分類', max_length=3)  # 1（ステータス変化）２（物理技）3（特殊技）
  is_direct = models.BooleanField(verbose_name='直接')
  can_protect = models.BooleanField(verbose_name='守る')

  def __str__(self):
    return str(self.id)
