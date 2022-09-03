from django.contrib import admin

from api.models import Move, Pokemon, PokemonAbility, PokemonEvolutionChain, PokemonHome, PokemonMove, PokemonName, PokemonStats, PokemonType

admin.site.register(Move)
admin.site.register(Pokemon)
admin.site.register(PokemonAbility)
admin.site.register(PokemonEvolutionChain)
admin.site.register(PokemonHome)
admin.site.register(PokemonMove)
admin.site.register(PokemonName)
admin.site.register(PokemonStats)
admin.site.register(PokemonType)
