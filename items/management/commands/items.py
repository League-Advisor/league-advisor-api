import json
from django.core.management.base import BaseCommand
from items.models import Item
import time
import requests
import re


class Command(BaseCommand):
    def handle(self, *args, **options):

        # NOTE: Remove all old model objects
        Item.objects.all().delete()

        print("REMOVING OLD ITEMS DATA")

        time.sleep(10)

        # NOTE: GET THE LATEST VERSION
        with open("static/versions.json") as local_versions:
            local_version = json.load(local_versions)

        # NOTE: GET ALL ITEMS JSON FILE FROM RIOT API
        items_json_url = f"http://ddragon.leagueoflegends.com/cdn/{local_version[0]}/data/en_US/item.json"
        json_file = requests.get(items_json_url).json()

        for item in json_file["data"]:
            print(f"POPULATING DATABSE WITH {json_file['data'][item]['name']} DATA")
            Item.objects.get_or_create(
                pk=int(item),
                name=json_file["data"][item]["name"],
                description=re.sub(
                    r"<[^>]*>", "", json_file["data"][item]["description"]
                ),
                plaintext=json_file["data"][item]["plaintext"],
                image=f"http://ddragon.leagueoflegends.com/cdn/{local_version[0]}/img/item/{int(item)}.png",
                gold=json_file["data"][item]["gold"]["base"],
                tags=json_file["data"][item]["tags"],
            )
