from django.urls import path,include
from .views import recommend_game

urlpatterns = [
    path('recommend/', recommend_game, name='recommend_game'),
]