from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import TokenPairSerializer

class TokenObtainedPairCustomView(TokenObtainPairView):
    serializer_class = TokenPairSerializer