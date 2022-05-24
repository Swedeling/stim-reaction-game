import django_filters
from .models import Game

class GameFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = ['player', 'good_answers', 'bad_answers', 'state','result']