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
    #persona = forms.ModelChoiceField(queryset=Person.objects.all())
    #typ_nadwozia = forms.ChoiceField(choices = CAR_CHOICES, label="", initial='', widget=forms.Select(), required=True)

    class Meta:
        model = Game
        fields = ("state",)
