from django.http import Http404
from rest_framework import status, views
from rest_framework.response import Response
from ..models import Pokemon
from ..serializers import PokemonSerializer, PokemonListSerializer
from ..services import PokemonService
from ..repositories import PokemonRepository

# http://127.0.0.1:8000/api/pokemons/?version=1&id=n1
class PokemonListAPIView(views.APIView):  
  def get(self, request, format=None):
    id = request.query_params.get('id')
    no = request.query_params.get('no')
    version = request.query_params.get('version')

    service = PokemonService(PokemonRepository())
    list = service.find(id, no, version)

    if not list:
      return Response(status.HTTP_404_NOT_FOUND)
    
    serializer = PokemonListSerializer(list)
    return Response(serializer.data, status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    serializer = PokemonListSerializer(data=request.data)
    list = Pokemon.objects.all()
    list.delete()
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)

class PokemonAPIView(views.APIView):
  def get(self, request, pk, format=None):
    try:
      data = Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
      raise Http404("data not found")

    serializer = PokemonSerializer(data)
    return Response(serializer.data, status.HTTP_200_OK)

