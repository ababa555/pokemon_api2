import os
from pathlib import Path

from rest_framework import status, views
from rest_framework.response import Response
from ..services import PokemonNameService, PokemonHomeService
from ..repositories import PokemonNameInMemoryRepository, PokemonHomeInMemoryRepository

# http://127.0.0.1:8000/api/reload
# http://127.0.0.1:8000/api/reload?generation=2
class ReloadCacheAPIView(views.APIView):  
  def get(self, request, format=None):
    pokemonNameService = PokemonNameService(PokemonNameInMemoryRepository())
    _ = pokemonNameService.findForInMemory('1-n1', None, None, None, refresh=True)

    base_dir = Path(__file__).resolve().parent.parent.parent
    file_list = list(Path(os.path.join(base_dir, "static/json/pdetail")).glob('*'))
    seasons = sorted(set([i.name[:5] for i in file_list]), reverse=True)

    generation = request.query_params.get('generation')
    if generation:
      seasons = seasons[:int(generation)]

    for season_id in seasons:
      pokemonHomeService = PokemonHomeService(PokemonHomeInMemoryRepository())
      _ = pokemonHomeService.findForInMemory(season_id, None, None, refresh=True)

    return Response({"message": "データを更新しました。"}, status.HTTP_200_OK)
