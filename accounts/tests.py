"""This module tests Accounts app"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserModel


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
        hit = UserModel.save(user)
        self.assertEqual(hit, status.HTTP_200_OK)


# ///////////test APIViews
class TistView(APITestCase):

    user_data = {
        "username": "bashar",
        "password": "pass",
        "summoner_name": "bashar",
        "summoner_server": "euw1",
        "email": "bashar@gmail.com",
    }
    user_info = {
        "username": "bashar",
        "summoner_name": "bashar",
        "summoner_server": "euw1",
        "email": "bashar@gmail.com",
    }

    login_data = {"password": "pass", "email": "shar@gmail.com"}

    login_data_T = {"password": "pass", "email": "bashar@gmail.com"}
    # ///////////test registerview
    def test_user_cannot_register_without_data(self):
        register_url = reverse("register")
        response = self.client.post(register_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_register(self):
        register_url = reverse("register")
        response = self.client.post(register_url, self.user_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.user_info)

    
    # ///////////test loginview
    def test_user_cannot_login_without_data(self):
        login_url = reverse("login")
        response = self.client.post(login_url)
        self.assertEqual(response.status_code, 400)

    def test_user_not_found(self):
        login_url = reverse("login")
        response = self.client.post(login_url, self.login_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ///////////test logoutview
    def test_user__logout(self):
        logout_url = reverse("logout")
        response = self.client.post(logout_url)
        self.assertEqual(response.status_code, 200)
