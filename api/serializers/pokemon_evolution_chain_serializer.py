import re
from rest_framework import serializers
from ..models import Pokemon, PokemonEvolutionChain

class PokemonEvolutionChainSerializer(serializers.ModelSerializer):
  class Meta:
    model = PokemonEvolutionChain
    fields = ['id', 'evolution_chain_id', 'order']

  def create(self, validated_data):
    id = validated_data['id']
    pokemon = Pokemon.objects.get(pk=id)
    
    pokemonEvolutionChain = PokemonEvolutionChain.objects.create(
      id=id, 
      evolution_chain_id=validated_data['evolution_chain_id'], 
      order=validated_data['order'],
      pokemon_id=pokemon.id)
    return pokemonEvolutionChain

class PokemonEvolutionChainListSerializer(serializers.ListSerializer):
  child = PokemonEvolutionChainSerializer()
