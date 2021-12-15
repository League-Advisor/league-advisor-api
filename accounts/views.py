import requests
import environ
import json

from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from django.http import JsonResponse

env = environ.Env()
environ.Env.read_env()


class RegisterView(APIView):
    def post(self, request):
        if not request.data:
            return Response(status= status.HTTP_400_BAD_REQUEST) 
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            available = {
                "message":"user already exists"
            }
            return Response(available, status=status.HTTP_200_OK)


def UpdateProfile(request):
    requester = request.GET.get('user')
    app_user = UserModel.objects.filter(username=requester)
    app_user = app_user.first()

    with open("static/versions.json") as local_versions:
        local_version = json.load(local_versions)


        response = requests.get(
            f"https://{app_user.summoner_server}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{app_user.summoner_name}", headers = {"X-Riot-Token":f"{env('API_KEY')}"}
            )

        if response.status_code == 200:
            response_data = response.json()
            app_user.summoner_level = response_data["summonerLevel"]
            app_user.summoner_name = response_data["name"]
            profileIconId = response_data["profileIconId"]
            id = response_data["id"]
            puuid = response_data["puuid"]

            # NOTE: GET SUMMONER ICON
            app_user.profile_icon = f"https://ddragon.leagueoflegends.com/cdn/{local_version[0]}/img/profileicon/{profileIconId}.png"

            # NOTE: GET SUMMONER CHAMPION MASTERY DATA
            champion_mastery = requests.get(
                f"https://{app_user.summoner_server}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{id}", headers = {"X-Riot-Token":f"{env('API_KEY')}"}
            ).json()

            # NOTE: STORE THE 3 HIGHEST MASTERY CHAMPIONS
            app_user.summoner_champion_mastery = champion_mastery[:3]

            # NOTE: GET SUMMONER RANK DATA
            summoner_rank = requests.get(f"https://{app_user.summoner_server}.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}", headers = {"X-Riot-Token":f"{env('API_KEY')}"}).json()

            # NOTE: STORE SUMMONER RANK DATA
            app_user.summoner_rank = summoner_rank

            # NOTE: SET RIOT ROUTING SERVER
            if app_user.summoner_server in ["br1", "la1", "la2", "na1"]:
                riot_routing = "AMERICAS"
            elif app_user.summoner_server in ["eun1", "euw1", "ru", "tr1", "oc1"]:
                riot_routing = "EUROPE"
            elif app_user.summoner_server in ["jp1", "kr"]:
                riot_routing = "ASIA"
            
            # NOTE: GET SUMMONER MOST RECENT MATCH HISTORY
            match_history = requests.get(
                f"https://{riot_routing}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?count=5", headers = {"X-Riot-Token":f"{env('API_KEY')}"}
            ).json()

            # NOTE: GET MATCH DATA FOR MATCH HISTORY
            match_history_list = match_history[:5]
            match_history_data = []
            for match in match_history_list:
                single_match = requests.get(
                    f"https://europe.api.riotgames.com/lol/match/v5/matches/{match}", headers = {"X-Riot-Token":f"{env('API_KEY')}"}
                ).json()
                match_history_data.append(single_match)
                
            # NOTE: STORE SUMMONER MATCH DATA
            app_user.summoner_match_history = match_history_data


        # NOTE: SET AND RETURN UPDATED app_user DATA
            updated_data = {
                "email":app_user.email,
                "username" : app_user.username,
                "summoner_name" : app_user.summoner_name,
                "summoner_server" : app_user.summoner_server,
                "profile_icon" : app_user.profile_icon,
                "summoner_level" : app_user.summoner_level,
                "summoner_rank" : app_user.summoner_rank,
                "summoner_champion_mastery" : app_user.summoner_champion_mastery,
                "summoner_match_history" : app_user.summoner_match_history
                }
        super(UserModel, app_user).save()
        return JsonResponse(updated_data)