from django.core.management.base import BaseCommand

class Command(BaseCommand):
  help = 'Example Command'

  def handle(self, *args, **kwargs):
    print('execute Example Command')
