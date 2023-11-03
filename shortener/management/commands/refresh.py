from django.core.management.base import BaseCommand, CommandError
from shortener.models import URL

# python manage.py refresh --items 5 => file name is refresh.py, items option is 5 optional
class Command(BaseCommand):
  help = 'Refreshes all shortcodes'

  def add_arguments(self, parser):
    parser.add_argument('--items', type=int)

  def handle(self, *args, **options):
    return URL.objects.refresh(items=options['items'])