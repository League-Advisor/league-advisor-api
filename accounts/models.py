from django.db import models
import environ
from django.contrib.auth.models import AbstractUser
from rest_framework.response import Response
from rest_framework import status

import requests
import json
import  environ
# NOTE: READ ENV VARIABLES
env = environ.Env()
environ.Env.read_env()
# NOTE: SET DEFAULT JSON FIELDS VALUE
def no_data_default():
    return {"champion_mastery":"not enough data"}

# NOTE: READ THE LATEST PATCH NOTES
with open("static/versions.json") as local_versions:
    local_version = json.load(local_versions)

class UserModel(AbstractUser):

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    summoner_name = models.CharField(max_length=255)
    summoner_server = models.CharField(max_length=255)
    summoner_level = models.IntegerField(default=0)
    summoner_rank = models.JSONField(default= no_data_default)
    profile_icon = models.URLField(default=f"https://ddragon.leagueoflegends.com/cdn/{local_version[0]}/img/profileicon/0.png")
    summoner_champion_mastery = models.JSONField(default= no_data_default)
    summoner_match_history = models.JSONField(default= no_data_default)
    REQUIRED_FIELDS = ["summoner_name", "summoner_server", "email"]

    # NOTE: OVERRIDE DEFAULT VALUES WITH REAL SUMMONER DATA
    def save(self, *args, **kwargs):
        # NOTE: GET SUMMONER DATA USING SUMMONERNAME
        response = requests.get(
            f"https://{self.summoner_server}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner_name}", headers = {"X-Riot-Token":f"{env('API_KEY')}"}
            )

        # NOTE: IF SUMMONERNAME IS VALID
        if response.status_code == 200:
            response_data = response.json()
            self.summoner_level = response_data["summonerLevel"]
            self.summoner_name = response_data["name"]
            profileIconId = response_data["profileIconId"]
            id = response_data["id"]
            puuid = response_data["puuid"]
            # //////////////////////////////////////////
            # NOTE: GET SUMMONER ICON
            self.profile_icon = f"https://ddragon.leagueoflegends.com/cdn/{local_version[0]}/img/profileicon/{profileIconId}.png"
            # //////////////////////////////////////////
            # NOTE: GET SUMMONER CHAMPION MASTERY DATA
            champion_mastery = requests.get(
                f"https://{self.summoner_server}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{id}", headers = {"X-Riot-Token":f"{env('API_KEY')}"}
            ).json()
            # //////////////////////////////////////////
            # NOTE: STORE THE 3 HIGHEST MASTERY CHAMPIONS
            self.summoner_champion_mastery = champion_mastery[:3]
            # //////////////////////////////////////////
            # NOTE: GET SUMMONER RANK DATA
            summoner_rank = requests.get(
                f"https://{self.summoner_server}.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}", headers = {"X-Riot-Token":f"{env('API_KEY')}"}
            ).json()
            # //////////////////////////////////////////
            # NOTE: STORE SUMMONER RANK DATA
            self.summoner_rank = summoner_rank
            # //////////////////////////////////////////
            # NOTE: SET RIOT ROUTING SERVER
            if self.summoner_server in ["br1", "la1", "la2", "na1"]:
                riot_routing = "AMERICAS"
            elif self.summoner_server in ["eun1", "euw1", "ru", "tr1", "oc1"]:
                riot_routing = "EUROPE"
            elif self.summoner_server in ["jp1", "kr"]:
                riot_routing = "ASIA"
            
            # NOTE: GET SUMMONER MOST RECENT MATCH HISTORY
            match_history = requests.get(
                f"https://{riot_routing}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?count=5", headers = {"X-Riot-Token":f"{env('API_KEY')}"}
            ).json()
            # //////////////////////////////////////////
            # NOTE: GET MATCH DATA FOR MATCH HISTORY
            match_history_list = match_history[:5]
            match_history_data = []
            for match in match_history_list:
                single_match = requests.get(
                    f"https://europe.api.riotgames.com/lol/match/v5/matches/{match}", headers = {"X-Riot-Token":f"{env('API_KEY')}"}
                ).json()
                match_history_data.append(single_match)
                
            # NOTE: STORE SUMMONER MATCH DATA
            self.summoner_match_history = match_history_data
            # //////////////////////////////////////////
        super(UserModel, self).save(*args, **kwargs)
        return Response(status= status.HTTP_200_OK)

    def __str__(self):
        return self.email
