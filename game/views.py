from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Game
from .models import Score
import datetime
from .forms import GameForm

from decimal import Decimal

from .filters import GameFilter
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseNotFound


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="game/register.html", context={"register_form":form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="game/login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("homepage")


def homepage(request):
    return render(request=request, template_name="game/homepage.html")


def history(request):
    myFilter = GameFilter(request.GET, queryset=Game.objects.all())
    objects = myFilter.qs
    return render(request=request, template_name="game/history.html", context={'objects': objects, 'scores': Score.objects.all(), 'myFilter': myFilter})


def start_game(request):
    if request.method == "POST":
        game_form = GameForm(request.POST)
        form = request.POST
        form_state = game_form.data.get('state')

        Game.objects.create(
            player=request.user,
            state=form_state,
            good_answers=int(form.get('good_answers', '0')),
            bad_answers=int(form.get('bad_answers', '0')),
            avg_speed=Decimal(form.get('avg_speed', '0')),
            result=int(form.get('good_answers', '0'))*5
        )
        now = datetime.datetime.now().strftime("%H:%M")

        if Game.objects.filter(player=request.user.id).exists():
            messages.info(request, "Game is added to database!")
        else:
            messages.info(request, "We couldn't add your game to database")

    game_form = GameForm()

    return render(request=request,template_name="game/startgame.html", context={'game_form': game_form})


def test(request):
    return render(request=request,template_name="game/test.html")