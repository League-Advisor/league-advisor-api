from django.db.models import fields
from rest_framework import serializers
from .models import UserModel


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['profile_icon', 'username', 'summoner_name', 'email', 'summoner_server', 'summoner_level',
                  'summoner_rank', 'summoner_champion_mastery', 'summoner_match_history']
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'summoner_name', 'summoner_server', 'email', 'password']
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


