from django.http import Http404
from rest_framework import status, views
from rest_framework.response import Response

from ..models import Move
from ..serializers import MoveSerializer, MoveListSerializer
from ..services import MoveService
from ..repositories import MoveRepository

# http://127.0.0.1:8000/api/moves/?version=1
class MoveListAPIView(views.APIView):  
  def get(self, request, format=None):
    version = request.query_params.get('version')

    service = MoveService(MoveRepository())
    list = service.find(id, version)

    serializer = MoveListSerializer(list)

    return Response(serializer.data, status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    serializer = MoveListSerializer(data=request.data)
    list = Move.objects.all()
    list.delete()
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)

class MoveAPIView(views.APIView):
  def get(self, request, pk, format=None):
    try:
      data = Move.objects.get(pk=pk)
    except Move.DoesNotExist:
      raise Http404("data not found")

    serializer = MoveSerializer(data)
    return Response(serializer.data, status.HTTP_200_OK)

