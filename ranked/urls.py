from django.urls import path 
from .views import data_analyzer


urlpatterns = [
	path('',data_analyzer, name="ranked"),
	
]