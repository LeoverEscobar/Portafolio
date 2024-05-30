# Aplicaciones/tictactoe/urls.py
from django.urls import path
from .views import display_board, make_move

urlpatterns = [
    path('board/', display_board, name='display_board'),
    path('make_move/', make_move, name='make_move'),
]
