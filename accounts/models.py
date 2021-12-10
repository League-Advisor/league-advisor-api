from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):

    def contact_default():
        return {"email": "to1@example.com"}

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255,  unique=True)
    password = models.CharField(max_length=255)
    summoner_name = models.CharField(max_length=255)
    summoner_server = models.CharField(max_length=255)
    summoner_level = models.IntegerField(default=0)
    summoner_rank = models.CharField(max_length=255)
    summoner_champion_mastery = models.JSONField(default=contact_default)
    summoner_match_history = models.JSONField(default=contact_default)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
