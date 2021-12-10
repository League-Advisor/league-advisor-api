import json
from django.core.management.base import BaseCommand
from champions.models import Champion
import requests
import time

class Command(BaseCommand):

    def handle(self, *args, **options):

        # NOTE: UNCOMMENT IF YOU ARE USING STATIC FILES
        # with open('static/champions_data.json') as f:
        #     json_file = json.load(f)

        # NOTE: GET ALL CHAMPIONS JSON FILE FROM RIOT API
        champions_json_url = f"http://ddragon.leagueoflegends.com/cdn/11.24.1/data/en_US/champion.json"
        json_file = requests.get(champions_json_url).json()

        counter = 0
        # NOTE: LOOP OVER EACH CHAMPION
        for champion in json_file['data']:
            # NOTE: GET EACH CHAMPION'S DETAILED JSON FILE FROM RIOT API
            champion_json_url = f"http://ddragon.leagueoflegends.com/cdn/11.24.1/data/en_US/champion/{json_file['data'][champion]['id']}.json"
            champion_json = requests.get(champion_json_url).json()

            # NOTE: TRY NOT TO GET BLACKLISTED
            time.sleep(5)   

            # NOTE: GATHER NECESSARY SKIN INFO
            champion_skins = []
            for skin in champion_json['data'][champion]['skins']:
                champion_skins.append({skin["name"]:f'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/{json_file["data"][champion]["name"]}_{skin["num"]}.jpg'})                
            
            # NOTE: GATHER NECESSARY SKILLS INFO
            champion_skills = []
            for skill in champion_json['data'][champion]['spells']:
                champion_skills.append({skill["name"]:f'http://ddragon.leagueoflegends.com/cdn/11.24.1/img/spell/{skill["id"]}.png'})

            # NOTE: CREATE AN OBJECT
            # NOTE: STORE LISTS AS STR

            Champion.objects.get_or_create(
            pk=counter,
            champion_id=champion_json['data'][champion]['id'],
            key = champion_json['data'][champion]['key'],
            name=champion_json['data'][champion]['name'],
            title=champion_json['data'][champion]['title'],
            lore=champion_json['data'][champion]['lore'],

            attack=json_file['data'][champion]['info']['attack'],
            defense=json_file['data'][champion]['info']['defense'],
            magic=json_file['data'][champion]['info']['magic'],
            difficulty=json_file['data'][champion]['info']['difficulty'],
            skills = str(champion_skills),
            image=f"http://ddragon.leagueoflegends.com/cdn/img/champion/loading/{json_file['data'][champion]['name']}_0.jpg",
            skins = str(champion_skins),
            tags=json_file['data'][champion]['tags'],
            stats=json_file['data'][champion]['stats'])

            counter += 1