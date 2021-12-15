from django.db.models import fields
from rest_framework import serializers
from .models import UserModel


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'profile_icon','password', 'username', 'summoner_name', 'email', 'summoner_server', 'summoner_level',
                  'summoner_rank', 'summoner_champion_mastery', 'summoner_match_history']
        extra_kwargs = {
            'password': {'write_only': True}
        }       

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'profile_icon', 'username','password', 'summoner_name', 'email', 'summoner_server', 'summoner_level',
                  'summoner_rank', 'summoner_champion_mastery', 'summoner_match_history']
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


