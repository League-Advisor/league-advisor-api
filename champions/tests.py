"""This module tests champions app"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
import environ
from rest_framework import status
from rest_framework.test import APITestCase
from .apps import ChampionsConfig
from django.apps import AppConfig
from .models import Champion
import requests
import json
import environ
from champions.management.commands.populate_champions import Command
from items.management.commands.items import Command as ItemsCommand
from unittest import skip
from .models import Champion

env = environ.Env()
environ.Env.read_env()

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()


class ChampionModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username="tester",
            password="pass",
            summoner_name="mohahamo",
            summoner_server="euw1",
            email="dua@tester.com",
        )
        test_user.save()

        test_champion = Champion.objects.create(
            pk=999,
            champion_id="Rai",
            name="Rai",
            title="Rai",
            lore="The best",
            attack=10,
            defense=10,
            magic=10,
            difficulty=10,
            image="http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Irelia_0.jpg",
            tags="stronk",
            stats="stronk",
        )
        test_champion.save()

    def test_champion_content(self):
        champion = Champion.objects.get(pk=999)

        self.assertEqual(champion.champion_id, "Rai")
        self.assertEqual(champion.name, "Rai")
        self.assertEqual(champion.title, "Rai")
        self.assertEqual(champion.lore, "The best")
        self.assertEqual(champion.attack, 10)
        self.assertEqual(champion.defense, 10)
        self.assertEqual(champion.magic, 10)
        self.assertEqual(champion.difficulty, 10)
        self.assertEqual(
            champion.image,
            "http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Irelia_0.jpg",
        )
        self.assertEqual(champion.tags, "stronk")
        self.assertEqual(champion.stats, "stronk")


class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse("champion_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(
            username="tester",
            password="pass",
            summoner_name="mohahamo",
            summoner_server="euw1",
            email="dua@tester.com",
        )
        test_user.save()

        test_champion = Champion.objects.create(
            pk=999,
            champion_id="Rai",
            key=999,
            name="Rai",
            title="Rai",
            lore="The best",
            attack=10,
            defense=10,
            magic=10,
            difficulty=10,
            image="http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Irelia_0.jpg",
            tags="stronk",
            stats="stronk",
        )
        test_champion.save()

        response = self.client.get(reverse("champion_detail", args=[999]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": test_champion.id,
                "champion_id": test_champion.champion_id,
                "key": test_champion.key,
                "name": test_champion.name,
                "title": test_champion.title,
                "lore": test_champion.lore,
                "attack": test_champion.attack,
                "defense": test_champion.defense,
                "magic": test_champion.magic,
                "difficulty": test_champion.difficulty,
                "skills": test_champion.skills,
                "image": test_champion.image,
                "skins": test_champion.skins,
                "tags": test_champion.tags,
                "stats": test_champion.stats,
            },
        )


# @skip('ONLY RUNE THIS TEST IF YOU HAVE AN EXCELLENT CONNECTION BECAUSE IT WILL EMPTY THE DB AND REPOPULATE IT')
# class ChampionAppTests(TestCase):
#     # Arrange
#     current_versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()
#     with open("static/versions.json") as local_versions:
#                 local_version = json.load(local_versions)
#     expected = current_versions[0]
#     command = Command()
#     items = ItemsCommand()

#     # Act
#     ChampionsConfig.ready(AppConfig)
#     command.handle()
#     items.handle()

#     actual = local_version[0]

#     # Assert
#     assert actual == expected

