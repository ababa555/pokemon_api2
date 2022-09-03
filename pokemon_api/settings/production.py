from pathlib import Path
import dj_database_url
from pokemon_api.settings.base import *

# BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = False

# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
DATABASES = {"default": dj_database_url.config()}
