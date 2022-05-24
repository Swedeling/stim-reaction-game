from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(101)]
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
    avg_speed = models.DecimalField(max_digits=9, decimal_places=3)
    result = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, validators=PERCENTAGE_VALIDATOR)
    objects = models.Manager()


class Score(models.Model):
    game_played=models.ForeignKey(Game, on_delete=models.CASCADE)
    round=models.IntegerField(default=1)
    is_won=models.BooleanField()
    reaction_time=models.TimeField()
