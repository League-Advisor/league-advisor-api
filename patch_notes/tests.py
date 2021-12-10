"""This module tests patch_notes module"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class APITest(APITestCase):
    def test_patch_notes(self):
        response = self.client.get(reverse('patch-notes'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)