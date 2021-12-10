from django.urls import path
from .views import patch_notes

urlpatterns = [
  path('',patch_notes ,name = 'patch-notes')
]