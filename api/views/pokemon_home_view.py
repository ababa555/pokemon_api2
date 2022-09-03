from rest_framework import status, views
from rest_framework.response import Response

from ..models import PokemonHome
from ..serializers import PokemonHomeListSerializer
from ..services import PokemonHomeService
from ..repositories import PokemonHomeRepository

class PokemonHomeAPIView(views.APIView):
  def get(self, request, format=None):
    season_id = request.query_params.get('season_id')
    pokemon_id = request.query_params.get('pokemon_id')
    type = request.query_params.get('type')

    service = PokemonHomeService(PokemonHomeRepository())
    list = service.find(season_id, pokemon_id, type)

    serializer = PokemonHomeListSerializer(list)

    return Response(serializer.data, status.HTTP_200_OK)
    