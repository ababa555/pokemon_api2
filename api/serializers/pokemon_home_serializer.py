from rest_framework import serializers
from ..models import PokemonHome

class PokemonHomeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PokemonHome
    fields = ['id','season_id','pokemon_id','type','pokemon_name','name','percent']

class PokemonHomeListSerializer(serializers.ListSerializer):
  child = PokemonHomeSerializer()
