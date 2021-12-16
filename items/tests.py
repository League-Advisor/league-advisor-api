from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
import environ
from rest_framework import status
from rest_framework.test import APITestCase


from .models import Item

env = environ.Env()
environ.Env.read_env()


class ItemModelTests(TestCase):
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

        test_item = Item.objects.create(
            item_id=1001,
            name="Boots",
            description="<mainText><stats><attention>25</attention> Move Speed</stats></mainText><br>",
            plaintext="Slightly increases Movement Speed",
            image="http://ddragon.leagueoflegends.com/cdn/11.24.1/img/item/1001.png",
            gold=300,
            tags="['Boots']",
        )
        test_item.save()

    def test_blog_content(self):
        item = Item.objects.get(item_id=1001)

        self.assertEqual(item.name, "Boots")
        self.assertEqual(item.gold, 300)


class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse("item_list"))
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

        test_item = Item.objects.create(
            item_id=1001,
            name="Boots",
            description="<mainText><stats><attention>25</attention> Move Speed</stats></mainText><br>",
            plaintext="Slightly increases Movement Speed",
            image="http://ddragon.leagueoflegends.com/cdn/11.24.1/img/item/1001.png",
            gold=300,
            tags="['Boots']",
        )
        test_item.save()

        response = self.client.get(reverse("item_detail", args=[1001]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "item_id": test_item.item_id,
                "name": test_item.name,
                "description": test_item.description,
                "plaintext": test_item.plaintext,
                "image": test_item.image,
                "gold": test_item.gold,
                "tags": test_item.tags,
            },
        )
