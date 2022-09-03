import re
from rest_framework import serializers
from ..models import Pokemon, PokemonMove

class PokemonMoveSerializer(serializers.ModelSerializer):
  class Meta:
    model = PokemonMove
    fields = ['id','move_name']

  def create(self, validated_data):
    id = validated_data['id']
    pokemon = Pokemon.objects.get(pk=id)
    
    pokemonMove = PokemonMove.objects.create(
      id=id, 
      move_name=validated_data['move_name'],
      pokemon_id=pokemon.id)
    return pokemonMove

class PokemonMoveListSerializer(serializers.ListSerializer):
  child = PokemonMoveSerializer()
