from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=64)
    encrypted_password = models.CharField(max_length=64)
    summoner_name = models.CharField(max_length=64)
    summoner_server = models.CharField(max_length=64)
    summoner_level = models.IntegerField( default=0 )
    summoner_rank = models.CharField(max_length=64)

    def contact_default():
        return {"email": "to1@example.com"}

    summoner_champion_mastery = models.JSONField( default=contact_default)
    summoner_match_history = models.JSONField( default=contact_default)

    USERNAME_FIELD = 'username'
    PASSWORD_FIELD = 'encrypted_password'
    REQUIRED_FIELDS = ["email", "password"]

    # created_at = models.DateTimeField(auto_now_add = True)


    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username