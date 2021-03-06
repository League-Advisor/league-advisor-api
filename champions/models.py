from django.db import models
from django.db.models.fields import IntegerField, TextField,  CharField

class Champion(models.Model):
    id = IntegerField(default=0, primary_key= True, unique= True)
    champion_id = CharField(max_length=64, unique= True)
    key = IntegerField(default=0)
    name = CharField(max_length=64)
    title = CharField(max_length=64)
    lore = TextField(default='')
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