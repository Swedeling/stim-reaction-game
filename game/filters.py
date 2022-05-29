import django_filters
from .models import Game
from crispy_forms.helper import FormHelper
from django import forms


class GameFilter(django_filters.FilterSet):


    class Meta:
        model = Game
        fields = ['player', 'good_answers', 'bad_answers', 'state','result']

    def __init__(self, *args, **kwargs):
        super(GameFilter, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.layout = Layout(
        #     Fieldset(
        #         'Player',
        #         'Good answers',
        #         'Bad answers',
        #         'State',
        #         'Result', wrapper_class="extra-class"
        #     ))

