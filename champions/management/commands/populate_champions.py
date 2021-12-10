import json
from django.core.management.base import BaseCommand
from champions.models import Champion

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('static/champions_data.json') as f:
            json_file = json.load(f)
        counter = 0
        for champion in json_file['data']:

            Champion.objects.get_or_create(
            pk=json_file['data'][champion]['key'],
            champion_id=json_file['data'][champion]['id'],
            name=json_file['data'][champion]['name'],
            title=json_file['data'][champion]['title'],
            lore=json_file['data'][champion]['blurb'],

            attack=json_file['data'][champion]['info']['attack'],
            defense=json_file['data'][champion]['info']['defense'],
            magic=json_file['data'][champion]['info']['magic'],
            difficulty=json_file['data'][champion]['info']['difficulty'],

            image=f"http://ddragon.leagueoflegends.com/cdn/img/champion/loading/{json_file['data'][champion]['name']}_0.jpg",

            tags=json_file['data'][champion]['tags'],
            stats=json_file['data'][champion]['stats'])
