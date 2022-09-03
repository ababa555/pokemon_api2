from crypt import methods
from django.http import Http404
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.decorators import action

from ..models import Pokemon, PokemonName
from ..serializers import PokemonSerializer, PokemonNameSerializer, PokemonNameListSerializer, PokemonNameWithPokemonSerializer, PokemonNameWithPokemonListSerializer
from ..services import PokemonNameService
from ..repositories import PokemonNameRepository

# http://127.0.0.1:8000/api/pokemon-names/?version=1&local_language_id=1&id=n1&response_format=1
class PokemonNameListAPIView(views.APIView):
  def get_serializer_class(self, request):
    if request.query_params.get('response_format') == "1":
      return PokemonNameWithPokemonListSerializer
    return PokemonNameListSerializer

  def get(self, request, format=None):
    id = request.query_params.get('id')
    version = request.query_params.get('version')
    local_language_id = request.query_params.get('local_language_id')
    name = request.query_params.get('name')
    
    service = PokemonNameService(PokemonNameRepository())
    list = service.find(id, version, local_language_id, name)
    
    if not list:
      return Response(status.HTTP_404_NOT_FOUND)

    serializer_class = self.get_serializer_class(request)
    serializer = serializer_class(list)

    return Response(serializer.data, status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    list = []
    for data in request.data:
      pokemonName = data
      pokemonName["id"] = data["pokemon_id"] + "-" + data["local_language_id"]
      list.append(pokemonName)

    serializer = PokemonNameListSerializer(data=list)
    list = PokemonName.objects.all()
    list.delete()
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response(serializer.data, status.HTTP_201_CREATED)

class PokemonNameAPIView(views.APIView):
  def get(self, request, pk, format=None):
    try:
      data = PokemonName.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
      raise Http404("data not found")

    serializer = PokemonNameSerializer(data)
    return Response(serializer.data, status.HTTP_200_OK)