from django.urls import path
from .views import AccountListView, AccountDetailView

urlpatterns = [
    path('', AccountListView.as_view(), name = 'Account_list'),
    path('<int:pk>', AccountDetailView.as_view(), name = 'Account_detail'),
    ]