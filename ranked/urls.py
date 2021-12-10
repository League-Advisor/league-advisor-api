from django.urls import path 
from .views import data_analyzer,data_analyzer_items


urlpatterns = [
	# path('',data_analyzer, name="ranked"),
	path('',data_analyzer_items, name="ranked_items")
]