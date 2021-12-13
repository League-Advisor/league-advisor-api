from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token =  super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username
        token['summoner_name'] = user.summoner_name
        token['summoner_server'] = user.summoner_server
        token['profile_icon'] = user.profile_icon
        token['summoner_level'] = user.summoner_level
        token['summoner_rank'] = user.summoner_rank
        token['summoner_champion_mastery'] = user.summoner_champion_mastery
        token['summoner_match_history'] = user.summoner_match_history
        return token
