from django.http import Http404
from rest_framework import status, views
from rest_framework.response import Response

from ..models import Pokemon, PokemonStats
from ..serializers import PokemonSerializer, PokemonStatsSerializer, PokemonStatsListSerializer
from ..services import PokemonStatsService
from ..repositories import PokemonStatsRepository

# http://127.0.0.1:8000/api/pokemon-statuses/?version=1&id=n1
class PokemonStatsListAPIView(views.APIView):  
  def get(self, request, format=None):
    id = request.query_params.get('id')
    version = request.query_params.get('version')

    service = PokemonStatsService(PokemonStatsRepository())
    list = service.find(id, version)

    serializer = PokemonStatsListSerializer(list)
    return Response(serializer.data, status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    serializer = PokemonStatsListSerializer(data=request.data)
    list = PokemonStats.objects.all()
    list.delete()
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response(serializer.data, status.HTTP_201_CREATED)

class PokemonStatsAPIView(views.APIView):
  def get(self, request, pk, format=None):
    try:
      data = PokemonStats.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
      raise Http404("data not found")

    serializer = PokemonStatsSerializer(data)
    return Response(serializer.data, status.HTTP_200_OK)