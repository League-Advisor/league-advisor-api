# Generated by Django 4.0 on 2021-12-09 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_summoner_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='summoner_champion_mastery',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='summoner_match_history',
            field=models.JSONField(blank=True),
        ),
    ]