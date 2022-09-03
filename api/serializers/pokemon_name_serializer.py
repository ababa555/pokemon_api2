import re
from rest_framework import serializers
from ..models import Pokemon, PokemonName 

class PokemonNameSerializer(serializers.ModelSerializer):
  pokemon_no = serializers.ReadOnlyField(source='pokemon.no', read_only=True)
  name_with_form_name = serializers.SerializerMethodField()

  class Meta:
    model = PokemonName
    fields = ['id', 'local_language_id', 'name', 'form_name', 'pokemon_id', 'pokemon_no', 'name_with_form_name']

  def get_name_with_form_name(self, instance):
    if instance is None:
      return None

    name = instance.name
    form_name = '' if not instance.form_name else '（{}）'.format(instance.form_name)
    return name + form_name

  def create(self, validated_data):
    id = validated_data['id']
    repatter = re.compile('^.*-')
    result = repatter.match(id)
    # ex:n1-1⇒n1
    pokemon = Pokemon.objects.get(pk=id[result.start():result.end()-1])
    
    pokemonName = PokemonName.objects.create(
      id=id, 
      local_language_id=validated_data['local_language_id'], 
      name=validated_data['name'], 
      form_name=validated_data['form_name'] if validated_data['form_name'] != '""' else '',
      pokemon_id=pokemon.id)
    return pokemonName

class PokemonNameWithPokemonSerializer(PokemonNameSerializer):
  pokemon_order = serializers.ReadOnlyField(source='pokemon.order', read_only=True)
  pokemon_is_default = serializers.ReadOnlyField(source='pokemon.is_default', read_only=True)

  class Meta:
    model = PokemonNameSerializer.Meta.model
    fields = PokemonNameSerializer.Meta.fields + ['pokemon_order', 'pokemon_is_default']

class PokemonNameListSerializer(serializers.ListSerializer):
  child = PokemonNameSerializer()

class PokemonNameWithPokemonListSerializer(serializers.ListSerializer):
  child = PokemonNameWithPokemonSerializer()