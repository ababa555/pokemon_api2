import re
from rest_framework import serializers
from ..models import Pokemon, PokemonStats

class PokemonStatsSerializer(serializers.ModelSerializer):
  class Meta:
    model = PokemonStats
    fields = ['pokemon_id','hp' ,'attack' ,'defense' ,'sp_attack' ,'sp_defense' ,'speed']

  def create(self, validated_data):
    id = validated_data['id']
    pokemon = Pokemon.objects.get(pk=id)
    
    pokemonStats = PokemonStats.objects.create(
      id=id, 
      hp=validated_data['hp'], 
      attack=validated_data['attack'],
      defense=validated_data['defense'],
      sp_attack=validated_data['sp_attack'],
      sp_defense=validated_data['sp_defense'],
      speed=validated_data['speed'],
      pokemon_id=pokemon.id)
    return pokemonStats

class PokemonStatsListSerializer(serializers.ListSerializer):
  child = PokemonStatsSerializer()
