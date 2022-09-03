from rest_framework import serializers
from ..models import Pokemon, PokemonName 

class PokemonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pokemon
    fields = ['id', 'no', 'height', 'weight', 'order', 'is_default']

class PokemonListSerializer(serializers.ListSerializer):
  child = PokemonSerializer()
