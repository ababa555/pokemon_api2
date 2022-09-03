import csv
import os
import re
import sys

from django.core.management.base import BaseCommand

from ...models import Pokemon, PokemonAbility, PokemonEvolutionChain, PokemonMove, PokemonName, PokemonStats, PokemonType, Move

file_base = "static/csv/"
versions = ["1-sm", "2-pika_vee", "3-swsh"]

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    self.remove_all()

    for index, version in enumerate(versions):
      sys.stderr.write("*** start import " + version + "***\n")
      file_dir = os.path.join(file_base, version)
      self.import_pokemon(file_dir)
      self.import_pokemon_name(file_dir)
      self.import_pokemon_ability(file_dir)
      self.import_pokemon_evolution_chain(file_dir)
      self.import_pokemon_move(file_dir)
      self.import_pokemon_stats(file_dir)
      self.import_pokemon_type(file_dir)
      self.import_move(file_dir)
      sys.stderr.write("*** end import " + version + "***\n")

  def import_pokemon(self, file_dir):
    sys.stderr.write("*** start import_pokemon ***\n")
    file_csv = os.path.join(file_dir, "pokemons.csv")
    if not os.path.isfile(file_csv):
      return

    fp = open(file_csv, 'r')
    reader = csv.reader(fp)
    next(reader, None)

    list = []

    for record in reader:
      data = Pokemon()
      data.id = record[0]
      data.no = record[1]
      data.height = record[2]
      data.weight = record[3]
      data.order = record[4]
      data.is_default = True if record[5] == "true" else False
      # data.save()
      list.append(data)

    Pokemon.objects.bulk_create(list)

    fp.close()
    sys.stderr.write("*** end import_pokemon ***\n")

  def import_pokemon_name(self, file_dir):
    sys.stderr.write("*** start import_pokemon_name ***\n")
    file_csv = os.path.join(file_dir, "pokemonNames.csv") 
    if not os.path.isfile(file_csv):
      return

    fp = open(file_csv, 'r')
    reader = csv.reader(fp)
    next(reader, None)

    list = []

    for record in reader:
      data = PokemonName()
      data.id = record[0]
      data.local_language_id = record[1]
      data.name = record[2]
      data.form_name = record[3]
      repatter = re.compile('^.*-')
      result = repatter.match(data.id)
      pokemon_id = data.id[result.start():result.end()-1]
      data.pokemon = self.get_pokemon(pokemon_id)
      # data.save()
      list.append(data)

    PokemonName.objects.bulk_create(list)

    fp.close()
    sys.stderr.write("*** end import_pokemon_name ***\n")

  def import_pokemon_ability(self, file_dir):
    sys.stderr.write("*** start import_pokemon_ability ***\n")
    file_csv = os.path.join(file_dir, "pokemonAbilities.csv")
    if not os.path.isfile(file_csv):
      return

    fp = open(file_csv, 'r')
    reader = csv.reader(fp)
    next(reader, None)

    list = []

    for index, record in enumerate(reader):
      data = PokemonAbility()
      data.id = record[0] + "-" + str(index)
      data.ability_name = record[1]
      data.is_hidden =True if record[2] == "true" else False
      data.pokemon = self.get_pokemon(record[0])
      # data.save()
      list.append(data)

    PokemonAbility.objects.bulk_create(list)

    fp.close()
    sys.stderr.write("*** end import_pokemon_ability ***\n")

  def import_pokemon_evolution_chain(self, file_dir):
    sys.stderr.write("*** start import_pokemon_evolution_chain ***\n")
    file_csv = os.path.join(file_dir, "pokemonEvolutionChains.csv")
    if not os.path.isfile(file_csv):
      return

    fp = open(file_csv, 'r')
    reader = csv.reader(fp)
    next(reader, None)

    list = []

    for index, record in enumerate(reader):
      data = PokemonEvolutionChain()
      data.id = record[0] + "-" + str(index)
      data.evolution_chain_id = record[1]
      data.order = record[2]
      data.pokemon = self.get_pokemon(record[0])
      # data.save()
      list.append(data)

    PokemonEvolutionChain.objects.bulk_create(list)

    fp.close()
    sys.stderr.write("*** end import_pokemon_evolution_chain ***\n")

  def import_pokemon_move(self, file_dir):
    sys.stderr.write("*** start import_pokemon_move ***\n")
    file_csv = os.path.join(file_dir, "pokemonMoves.csv")
    if not os.path.isfile(file_csv):
      return

    fp = open(file_csv, 'r')
    reader = csv.reader(fp)
    next(reader, None)

    list = []

    for index, record in enumerate(reader):
      data = PokemonMove()
      data.id = record[0] + "-" + str(index).zfill(3)
      data.move_name = record[1]
      data.pokemon = self.get_pokemon(record[0])
      # data.save()
      list.append(data)

    PokemonMove.objects.bulk_create(list)

    fp.close()
    sys.stderr.write("*** end import_pokemon_move ***\n")

  def import_pokemon_stats(self, file_dir):
    sys.stderr.write("*** start import_pokemon_stats ***\n")
    file_csv = os.path.join(file_dir, "pokemonStatses.csv")
    if not os.path.isfile(file_csv):
      return

    fp = open(file_csv, 'r')
    reader = csv.reader(fp)
    next(reader, None)

    list = []

    for index, record in enumerate(reader):
      data = PokemonStats()
      data.id = record[0] + "-" + str(index)
      data.hp = record[1]
      data.attack = record[2]
      data.defense = record[3]
      data.sp_attack = record[4]
      data.sp_defense = record[5]
      data.speed = record[6]
      data.pokemon = self.get_pokemon(record[0])
      # data.save()
      list.append(data)

    PokemonStats.objects.bulk_create(list)

    fp.close()
    sys.stderr.write("*** end import_pokemon_stats ***\n")

  def import_pokemon_type(self, file_dir):
    sys.stderr.write("*** start import_pokemon_type ***\n")
    file_csv = os.path.join(file_dir, "pokemonTypes.csv")
    if not os.path.isfile(file_csv):
      return

    fp = open(file_csv, 'r')
    reader = csv.reader(fp)
    next(reader, None)

    list = []

    for index, record in enumerate(reader):
      data = PokemonType()
      data.id = record[0] + "-" + str(index)
      data.type_id = record[1]
      data.pokemon = self.get_pokemon(record[0])
      # data.save()
      list.append(data)

    PokemonType.objects.bulk_create(list)

    fp.close()
    sys.stderr.write("*** end import_pokemon_type ***\n")

  def import_move(self, file_dir):
    sys.stderr.write("*** start import_move ***\n")
    file_csv = os.path.join(file_dir, "Moves.csv")
    if not os.path.isfile(file_csv):
      return

    fp = open(file_csv, 'r')
    reader = csv.reader(fp)
    next(reader, None)

    list = []

    for record in reader:
      data = Move()
      splitId = record[0].split("-")
      data.id = splitId[0] + "-" + splitId[1].zfill(4)
      data.name = record[1]
      data.type = record[2]
      data.power1 = record[3]
      data.power2 = record[4]
      data.pp = record[5]
      data.accuracy = record[6]
      data.priority = record[7]
      data.damage_type = record[8]
      data.is_direct = True if record[9] == "true" else False
      data.can_protect = True if record[10] == "true" else False
      # data.save()
      list.append(data)

    Move.objects.bulk_create(list)

    fp.close()
    sys.stderr.write("*** end import_move ***\n")

  def get_pokemon(self, id):
    result = Pokemon.objects.get(pk=id)
    return result

  def remove_all(self):
    Pokemon.objects.all().delete()
    PokemonName.objects.all().delete()
    PokemonAbility.objects.all().delete()
    PokemonEvolutionChain.objects.all().delete()
    PokemonMove.objects.all().delete()
    PokemonStats.objects.all().delete()
    PokemonType.objects.all().delete()
    Move.objects.all().delete()