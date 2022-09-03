from django.http import Http404
from rest_framework import status, views
from rest_framework.response import Response

from ..models import Pokemon, PokemonEvolutionChain
from ..serializers import PokemonSerializer, PokemonEvolutionChainSerializer, PokemonEvolutionChainListSerializer
from ..services import PokemonEvolutionChainService
from ..repositories import PokemonEvolutionChainRepository

# http://127.0.0.1:8000/api/pokemon-evolution-chains/?version=1&id=n1
class PokemonEvolutionChainListAPIView(views.APIView):  
  def get(self, request, format=None):
    id = request.query_params.get('id')
    version = request.query_params.get('version')

    service = PokemonEvolutionChainService(PokemonEvolutionChainRepository())
    list = service.find(id, version)

    serializer = PokemonEvolutionChainListSerializer(list)
    return Response(serializer.data, status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    serializer = PokemonEvolutionChainListSerializer(data=request.data)
    list = PokemonEvolutionChain.objects.all()
    list.delete()
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response(serializer.data, status.HTTP_201_CREATED)

class PokemonEvolutionChainAPIView(views.APIView):
  def get(self, request, pk, format=None):
    try:
      data = PokemonEvolutionChain.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
      raise Http404("data not found")

    serializer = PokemonEvolutionChainSerializer(data)
    return Response(serializer.data, status.HTTP_200_OK)