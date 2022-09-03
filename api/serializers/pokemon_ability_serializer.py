import re
from rest_framework import serializers
from ..models import Pokemon, PokemonAbility

class PokemonAbilitySerializer(serializers.ModelSerializer):
  class Meta:
    model = PokemonAbility
    fields = ['id', 'ability_name', 'is_hidden']

  def create(self, validated_data):
    id = validated_data['id']
    pokemon = Pokemon.objects.get(pk=id)
    
    pokemonAbility = PokemonAbility.objects.create(
      id=id, 
      ability_name=validated_data['ability_name'], 
      is_hidden=validated_data['is_hidden'],
      pokemon_id=pokemon.id)
    return pokemonAbility

class PokemonAbilityListSerializer(serializers.ListSerializer):
  child = PokemonAbilitySerializer()
