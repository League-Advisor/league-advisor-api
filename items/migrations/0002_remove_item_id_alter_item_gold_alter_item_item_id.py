# Generated by Django 4.0 on 2021-12-10 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.AlterField(
            model_name='item',
            name='gold',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
