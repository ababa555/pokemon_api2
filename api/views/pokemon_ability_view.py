from django.http import Http404
from rest_framework import status, views
from rest_framework.response import Response

from ..models import Pokemon, PokemonAbility
from ..serializers import PokemonAbilitySerializer, PokemonAbilityListSerializer
from ..services import PokemonAbilityService
from ..repositories import PokemonAbilityRepository

# http://127.0.0.1:8000/api/pokemon-abilities/?version=1&id=n1
class PokemonAbilityListAPIView(views.APIView):  
  def get(self, request, format=None):
    id = request.query_params.get('id')
    version = request.query_params.get('version')

    service = PokemonAbilityService(PokemonAbilityRepository())
    list = service.find(id, version)
      
    serializer = PokemonAbilityListSerializer(list)
    return Response(serializer.data, status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    serializer = PokemonAbilityListSerializer(data=request.data)
    list = PokemonAbility.objects.all()
    list.delete()
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response(serializer.data, status.HTTP_201_CREATED)

class PokemonAbilityAPIView(views.APIView):
  def get(self, request, pk, format=None):
    try:
      data = PokemonAbility.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
      raise Http404("data not found")

    serializer = PokemonAbilitySerializer(data)
    return Response(serializer.data, status.HTTP_200_OK)