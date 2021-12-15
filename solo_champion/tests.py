from rest_framework.test import APITestCase
import requests
from rest_framework.test import APIRequestFactory
from .views import get_items

class SoloChampionTest(APITestCase):
    def test_solo_champion(self):
        request = requests.get(
            "http://127.0.0.1:8000/solo_champion/?champion_name=morgana"
        )

        expected = request.json()

        actual = {
            "morgana": [
                "Mobility Boots",
                "Imperial Mandate",
                "Zhonya's Hourglass",
                "Redemption",
                "Demonic Embrace",
                "Shard of True Ice",
            ]
        }
        assert actual == expected

    def test_solo_items(self):
        request = requests.get("http://127.0.0.1:8000/solo_champion/?champion_name=zoe")

        expected = request.json()

        actual = {
            "zoe": [
                "Doran's Ring",
                "Sorcerer's Shoes",
                "Luden's Tempest",
                "Mejai's Soulstealer",
                "Horizon Focus",
                "Zhonya's Hourglass",
                "Morellonomicon",
            ]
        }
        assert actual == expected
    
    
    def test_solo_champion2(self):
        factory = APIRequestFactory()
        url ='http://127.0.0.1:8000/solo_champion/?champion_name=zoe'
        request = factory.get(url)
        expected = 200
        actual = get_items(request).status_code  
        assert expected == actual
    
     
    
        
