from crispy_forms.helper import FormHelper
from django.forms.widgets import RadioSelect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Game


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class GameForm(forms.ModelForm):
    #typ_nadwozia = forms.ChoiceField(choices = CAR_CHOICES, label="", initial='', widget=forms.Select(), required=True)

    state=forms.ChoiceField(choices=Game.STATE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))


    class Meta:
        model = Game
        fields = ("state",)

    def __init__(self, *args, **kwargs):
        super(GameForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_show_labels = True
        for field in GameForm.Meta.fields:
            self.fields[field].label = False

