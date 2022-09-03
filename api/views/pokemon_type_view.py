from django.http import Http404
from rest_framework import status, views
from rest_framework.response import Response

from ..models import Pokemon, PokemonType
from ..serializers import PokemonSerializer, PokemonTypeSerializer, PokemonTypeListSerializer
from ..services import PokemonTypeService
from ..repositories import PokemonTypeRepository

# http://127.0.0.1:8000/api/pokemon-types/?version=1&id=n1
class PokemonTypeListAPIView(views.APIView):  
  def get(self, request, format=None):
    id = request.query_params.get('id')
    version = request.query_params.get('version')

    service = PokemonTypeService(PokemonTypeRepository())
    list = service.find(id, version)

    serializer = PokemonTypeListSerializer(list)
    return Response(serializer.data, status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    serializer = PokemonTypeListSerializer(data=request.data)
    list = PokemonType.objects.all()
    list.delete()
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response(serializer.data, status.HTTP_201_CREATED)

class PokemonTypeAPIView(views.APIView):
  def get(self, request, pk, format=None):
    try:
      data = PokemonType.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
      raise Http404("data not found")

    serializer = PokemonTypeSerializer(data)
    return Response(serializer.data, status.HTTP_200_OK)