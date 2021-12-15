"""This module tests Accounts app"""

# from os import environ
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserModel
# env = environ.Env()
# environ.Env.read_env()

class UserModelModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username="bashar",
            password="pass",
            summoner_name="bashar",
            summoner_server="euw1",
            email="bashar@gmail.com",
        )
        test_user.save()

    def test_accoun_content(self):
        user = UserModel.objects.filter(id=1)
        user = user.first()
        self.assertEqual(user.username, "bashar")
        self.assertEqual(user.summoner_name, "bashar")
        self.assertEqual(user.email, "bashar@gmail.com")
        self.assertEqual(user.summoner_server, "euw1")

    def test_account_save(self):
        user = UserModel.objects.filter(id=1)
        user = user.first()
        response = UserModel.save(user)
        self.assertEqual(response, None)

# ///////////test APIViews
class TistView(APITestCase):

    user_data = {
        "username": "bashar",
        "password": "pass",
        "summoner_name": "bashar",
        "summoner_server": "euw1",
        "email": "bashar@gmail.com",
    }

    # ///////////test registerview
    def test_user_cannot_register_without_data(self):
        register_url = reverse("register")
        response = self.client.post(register_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_register(self):
        register_url = reverse("register")
        response = self.client.post(register_url, self.user_data)
        self.assertEqual(response.status_code, 200)
        print(response.data["email"])
        self.assertEqual(response.data["email"], "bashar@gmail.com")

    
  


