from django.urls import path, re_path
import api.views as views

urlpatterns = [
  path('pokemon-names/', views.PokemonNameListV2APIView.as_view()),
  path('pokemon-home/', views.PokemonHomeV2APIView.as_view()),
]
