from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
import requests
from .views import data_analyzer
import environ
from django.urls import reverse

env = environ.Env()
environ.Env.read_env()

from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request


# Create your tests here.
class RankedTest(APITestCase):
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

    def test_get_items_json_response(self):
        url = "http://127.0.0.1:8000/ranked?composition=Ezreal,Nami,Syndra,Nidalee,Yone,Blitzcranck,Lillia,Jax,Sejuani,Morgana,Ezreal"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {
                "common items": [
                    "Serylda's Grudge",
                    "Muramana",
                    "Executioner's Calling",
                    "Ionian Boots of Lucidity",
                    "Divine Sunderer",
                    "Tiamat",
                    "Farsight Alteration",
                    "Doran's Blade",
                    "Muramana",
                    "Divine Sunderer",
                ],
                "recommended_build": [
                    "Ionian Boots of Lucidity",
                    "Farsight Alteration",
                    "Divine Sunderer",
                    "Muramana",
                    "Doran's Blade",
                ],
            },
        )

    def test_data_analyzer(self):
        factory = APIRequestFactory()
        url = "http://127.0.0.1:8000/ranked?composition=Ezreal,Nami,Syndra,Nidalee,Yone,Blitzcranck,Lillia,Jax,Sejuani,Morgana,Ezreal"
        request = factory.get(url)
        actual = data_analyzer(request).status_code
        expected = 200
        assert actual == expected
