import requests
import json

from django.apps import AppConfig

class ChampionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'champions'

    # NOTE:CHECK FOR VERSIONS AS SOON AS THE API IS UP AND RUNNING
    def ready(self):
        # NOTE: GET THE LASTEST VERSIONS FROM RIOT API
        current_versions = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()

        # NOTE: GET THE LASTEST VERSIONS FROM RIOT API
        with open('static/versions.json') as local_versions:
            local_version = json.load(local_versions)

        # NOTE: IF THE FETCHED VERSION NEWER THAN THE CURRRENT OVERRIDE THE CURRENT
        if current_versions[0] > local_version[0]:
            from champions.management.commands.populate_champions import Command

            with open('static/versions.json', 'w') as local_versions:
                json.dump(current_versions, local_versions)
            print("Version Updated")

            Command.handle(self)