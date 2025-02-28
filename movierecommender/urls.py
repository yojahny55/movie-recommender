from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_recommendations_list, name='recomendations'),
]
