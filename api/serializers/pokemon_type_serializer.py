import re
from rest_framework import serializers
from ..models import Pokemon, PokemonType

class PokemonTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PokemonType
    fields = ['id','type_id']

  def create(self, validated_data):
    id = validated_data['id']
    pokemon = Pokemon.objects.get(pk=id)
    
    pokemonStats = PokemonType.objects.create(
      id=id, 
      type_id=validated_data['type_id'],
      pokemon_id=pokemon.id)
    return pokemonStats

class PokemonTypeListSerializer(serializers.ListSerializer):
  child = PokemonTypeSerializer()
