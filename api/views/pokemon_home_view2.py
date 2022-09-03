from rest_framework import status, views
from rest_framework.response import Response

from ..serializers import PokemonHomeListSerializer
from ..services import PokemonHomeService
from ..repositories import PokemonHomeInMemoryRepository

# http://127.0.0.1:8000/v2/api/pokemon-home/?season_id=10311&pokemon_id=3-n3
class PokemonHomeV2APIView(views.APIView):
  def get(self, request, format=None):
    season_id = request.query_params.get('season_id')
    pokemon_id = request.query_params.get('pokemon_id')
    type = request.query_params.get('type')

    service = PokemonHomeService(PokemonHomeInMemoryRepository())
    list = service.findForInMemory(season_id, pokemon_id, type, refresh=False)

    serializer = PokemonHomeListSerializer(list)

    return Response(serializer.data, status.HTTP_200_OK)
    