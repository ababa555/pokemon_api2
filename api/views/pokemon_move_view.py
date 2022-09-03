from django.http import Http404
from rest_framework import status, views
from rest_framework.response import Response

from ..models import Pokemon, PokemonMove
from ..serializers import PokemonMoveSerializer, PokemonMoveListSerializer
from ..services import PokemonMoveService
from ..repositories import PokemonMoveRepository

# http://127.0.0.1:8000/api/pokemon-moves/?version=1&id=n1
class PokemonMoveListAPIView(views.APIView):
  def get(self, request, format=None):
    id = request.query_params.get('id')
    version = request.query_params.get('version')
    
    service = PokemonMoveService(PokemonMoveRepository())
    list = service.find(id, version)

    if not list:
      return Response(status.HTTP_404_NOT_FOUND)

    serializer = PokemonMoveListSerializer(list)
    return Response(serializer.data, status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    serializer = PokemonMoveListSerializer(data=request.data)
    list = PokemonMove.objects.all()
    list.delete()
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response(serializer.data, status.HTTP_201_CREATED)

class PokemonMoveAPIView(views.APIView):
  def get(self, request, pk, format=None):
    try:
      data = PokemonMove.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
      raise Http404("data not found")

    serializer = PokemonMoveSerializer(data)
    return Response(serializer.data, status.HTTP_200_OK)