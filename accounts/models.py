from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
import requests, json


class UserModel(AbstractUser):
    def contact_default_1():

        return {"mastery_history_None": "there is no match_history or champion_mastery"}

    def contact_default_2():

        return {"rank_None ": "there is no rank"}

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    summoner_name = models.CharField(max_length=255)
    summoner_server = models.CharField(max_length=255)
    summoner_level = models.IntegerField(default=0)
    summoner_rank = models.JSONField(default=contact_default_2)
    profile_icon = models.URLField()
    summoner_champion_mastery = models.JSONField(default=contact_default_1)
    summoner_match_history = models.JSONField(default=contact_default_1)
    REQUIRED_FIELDS = ["summoner_name", "summoner_server", "email"]

    def save(self, *args, **kwargs):
        response = requests.get(
            f"https://{self.summoner_server}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner_name}?api_key=RGAPI-38ab2df3-7125-426c-986a-f30ce2b95bfe"
        )
        response_data = response.json()
        self.summoner_level = response_data["summonerLevel"]
        self.summoner_name = response_data["name"]
        profileIconId = response_data["profileIconId"]
        id = response_data["id"]
        puuid = response_data["puuid"]
        rank = []
        # //////////////////////////////////////////
        self.profile_icon = f"https://ddragon.leagueoflegends.com/cdn/11.24.1/img/profileicon/{profileIconId}.png"
        # //////////////////////////////////////////
        champion_mastery = requests.get(
            f"https://{self.summoner_server}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{id}?api_key=RGAPI-38ab2df3-7125-426c-986a-f30ce2b95bfe"
        ).json()
        # //////////////////////////////////////////
        with open("static/champion_mastery.json", "w") as f:
            f.write(json.dumps(champion_mastery))
        # //////////////////////////////////////////
        with open("static/champion_mastery.json", "r") as f:
            championmastery = f.read()
        self.summoner_champion_mastery = championmastery
        # //////////////////////////////////////////
        summoner_rank = requests.get(
            f"https://{self.summoner_server}.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key=RGAPI-38ab2df3-7125-426c-986a-f30ce2b95bfe"
        ).json()
        # //////////////////////////////////////////
        with open("static/summoner_rank.json", "w") as f:
            f.write(json.dumps(summoner_rank))
        # //////////////////////////////////////////
        with open("static/summoner_rank.json", "r") as f:
            summonerrank = f.read()
        # //////////////////////////////////////////
        if summonerrank != []:
            self.summonerrank = rank
        else:
            self.summoner_rank = self.contact_default_2
        # //////////////////////////////////////////
        riot_dsenter = self.summoner_server
        if riot_dsenter in ["br1", "la1", "la2", "na1"]:
            riot_dsenter = "AMERICAS"
        if riot_dsenter in ["eun1", "euw1", "ru", "tr1", "oc1"]:
            riot_dsenter = "EUROPE"
        if riot_dsenter in ["jp1", "kr"]:
            riot_dsenter = "ASIA"
        match_history = summoner_rank = requests.get(
            f"https://{riot_dsenter}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?count=5&api_key=RGAPI-38ab2df3-7125-426c-986a-f30ce2b95bfe"
        ).json()
        # //////////////////////////////////////////
        matchhistory = requests.get(
            f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_history[0]}?api_key=RGAPI-38ab2df3-7125-426c-986a-f30ce2b95bfe"
        ).json()
        # //////////////////////////////////////////
        with open("static/match_history.json", "w") as f:
            f.write(json.dumps(matchhistory))
        # //////////////////////////////////////////
        with open("static/match_history.json", "r") as f:
            matchhistory_data = f.read()
        self.summoner_match_history = matchhistory_data
        # //////////////////////////////////////////
        super(UserModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
