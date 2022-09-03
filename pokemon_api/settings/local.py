from pathlib import Path
from pokemon_api.settings.base import *

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

CORS_ALLOW_ALL_ORIGINS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
