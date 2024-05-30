from django.db import models

class Game(models.Model):
    board = models.CharField(max_length=9, default='         ')
    current_player = models.CharField(max_length=1, default='X')
5