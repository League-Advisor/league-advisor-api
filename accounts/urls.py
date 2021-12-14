
from django.urls import path
from .views import RegisterView, UpdateProfile
urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('update/', UpdateProfile, name = 'update'),

]