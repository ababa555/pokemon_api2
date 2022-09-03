from rest_framework import serializers
from ..models import Move

class MoveSerializer(serializers.ModelSerializer):
  class Meta:
    model = Move
    fields = ['id','name','type','power1','power2','pp','accuracy','priority','damage_type','is_direct','can_protect']

class MoveListSerializer(serializers.ListSerializer):
  child = MoveSerializer()
