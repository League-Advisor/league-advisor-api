# Generated by Django 4.0 on 2021-12-15 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('champions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='creator',
        ),
    ]