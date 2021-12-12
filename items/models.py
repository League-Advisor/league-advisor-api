from django.db import models

class Item(models.Model):

    item_id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=64)
    description = models.TextField(default='')
    plaintext = models.TextField(default='')
    image = models.TextField(default='')
    gold = models.IntegerField( default=0)
    tags = models.TextField(default='')

    def __str__(self):
        return self.item_id