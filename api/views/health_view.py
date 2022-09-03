from rest_framework import status, views
from rest_framework.response import Response

class HealthAPIView(views.APIView):  
  def get(self, request, format=None):
    return Response({"message": "OK"}, status.HTTP_200_OK)
