import json
from django.core.management.base import BaseCommand
from items.models import Item

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('static/items_data.json') as f:
            json_file = json.load(f)

        for item in json_file['data']:
            Item.objects.get_or_create(pk= int(item),name=json_file['data'][item]['name'],
            description=json_file['data'][item]['description'],
            plaintext=json_file['data'][item]['plaintext'],
            image= f'http://ddragon.leagueoflegends.com/cdn/11.24.1/img/item/{int(item)}.png',
            gold=json_file['data'][item]['gold']['base'],
            tags=json_file['data'][item]['tags'])
          