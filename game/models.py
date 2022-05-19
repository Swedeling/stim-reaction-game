from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Game(models.Model):
    player=models.ForeignKey(User, on_delete=models.CASCADE)
    good_answers=models.IntegerField(default=1)
    bad_answers=models.IntegerField(default=1)
    start_time=models.DateTimeField(default=timezone.now())
    STATE_CHOICES = (
        ('B', 'Im before work'),
        ('A', 'Im after work'),
    )
    state = models.CharField(max_length=1, choices=STATE_CHOICES)

    objects = models.Manager()


class Scores(models.Model):
    game_played=player=models.ForeignKey(Game, on_delete=models.CASCADE)
    round=models.IntegerField(default=1)
    is_won=models.BooleanField()
    reaction_time=models.TimeField()
