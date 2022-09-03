from crypt import methods
from django.http import Http404
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.decorators import action

from ..models import Pokemon, PokemonName
from ..serializers import PokemonSerializer, PokemonNameSerializer, PokemonNameListSerializer, PokemonNameWithPokemonSerializer, PokemonNameWithPokemonListSerializer
from ..services import PokemonNameService
from ..repositories import PokemonNameInMemoryRepository

# http://127.0.0.1:8000/v2/api/pokemon-names/?version=1&local_language_id=1&id=n1&response_format=1
class PokemonNameListV2APIView(views.APIView):
  def get_serializer_class(self, request):
    if request.query_params.get('response_format') == "1":
      return PokemonNameWithPokemonListSerializer
    return PokemonNameListSerializer

  def get(self, request, format=None):
    id = request.query_params.get('id')
    version = request.query_params.get('version')
    local_language_id = request.query_params.get('local_language_id')
    name = request.query_params.get('name')
    
    service = PokemonNameService(PokemonNameInMemoryRepository())
    list = service.findForInMemory(id, version, local_language_id, name, refresh=False)
    
    if not list:
      return Response(status.HTTP_404_NOT_FOUND)

    serializer_class = self.get_serializer_class(request)
    serializer = serializer_class(list)

    return Response(serializer.data, status.HTTP_200_OK)
