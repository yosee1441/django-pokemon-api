from django.urls import path
from .views import PokemonListCreateView, PokemonDetailView

urlpatterns = [
    path('pokemon/', PokemonListCreateView.as_view(), name='pokemon-list'),
    path('pokemon/<int:pk>/', PokemonDetailView.as_view(), name='pokemon-detail'),
]
