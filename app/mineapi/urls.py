from django.urls import path
from .views import status, players, whitelist

urlpatterns = [
  path('status', status, name='status'),
  path('players', players, name='players'),
  path('whitelist', whitelist, name='whitelist'),
]
