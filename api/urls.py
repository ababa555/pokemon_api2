from django.urls import path, re_path
import api.views as views

urlpatterns = [
  path('pokemons/', views.PokemonListAPIView.as_view()),
  path('pokemons/<pk>/', views.PokemonAPIView.as_view()),

  path('pokemon-names/', views.PokemonNameListAPIView.as_view()),
  path('pokemon-names/<pk>/', views.PokemonNameAPIView.as_view()),
  
  path('pokemon-abilities/', views.PokemonAbilityListAPIView.as_view()),
  path('pokemon-abilities/<pk>/', views.PokemonAbilityAPIView.as_view()),

  path('pokemon-evolution-chains/', views.PokemonEvolutionChainListAPIView.as_view()),
  path('pokemon-evolution-chains/<pk>/', views.PokemonEvolutionChainAPIView.as_view()),

  path('pokemon-moves/', views.PokemonMoveListAPIView.as_view()),
  path('pokemon-moves/<pk>/', views.PokemonMoveAPIView.as_view()),

  path('pokemon-statuses/', views.PokemonStatsListAPIView.as_view()),
  path('pokemon-statuses/<pk>/', views.PokemonStatsAPIView.as_view()),

  path('pokemon-types/', views.PokemonTypeListAPIView.as_view()),
  path('pokemon-types/<pk>/', views.PokemonTypeAPIView.as_view()),

  path('moves/', views.MoveListAPIView.as_view()),
  path('moves/<pk>/', views.MoveAPIView.as_view()),

  path('pokemon-home/', views.PokemonHomeAPIView.as_view()),

  path('health/', views.HealthAPIView.as_view()),
  path('reload/', views.ReloadCacheAPIView.as_view()),
  path('seasons/', views.SeasonAPIView.as_view()),
  path('maintenance/', views.MaintenanceAPIView.as_view()),
]