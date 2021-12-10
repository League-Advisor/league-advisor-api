from django.db import models
from django.db.models.fields import IntegerField, TextField


class Champion(models.Model):
    id = models.IntegerField(default=0, primary_key= True, unique= True)
    champion_id = models.CharField(max_length=64, unique= True)
    key = models.IntegerField(default=0)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    lore = models.TextField(default='')
    attack = IntegerField(default=0)
    defense = IntegerField(default=0)
    magic = IntegerField(default=0)
    difficulty = IntegerField(default=0)
    skills = TextField(default='')
    image = TextField(default = '')
    skins = TextField(default= '')
    tags = TextField(default='')
    stats = TextField(default='')

    def __str__(self):
      return self.champion_id