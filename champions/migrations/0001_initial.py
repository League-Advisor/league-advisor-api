# Generated by Django 4.0 on 2021-12-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('champion_id', models.CharField(max_length=64, unique=True)),
                ('key', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('lore', models.TextField(default='')),
                ('attack', models.IntegerField(default=0)),
                ('defense', models.IntegerField(default=0)),
                ('magic', models.IntegerField(default=0)),
                ('difficulty', models.IntegerField(default=0)),
                ('skills', models.TextField(default='')),
                ('image', models.TextField(default='')),
                ('skins', models.TextField(default='')),
                ('tags', models.TextField(default='')),
                ('stats', models.TextField(default='')),
            ],
        ),
    ]
