"""reactiontime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from game import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("homepage/", views.homepage, name="homepage"),
    path('admin/', admin.site.urls),
    path("register/", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("startgame", views.start_game, name="startgame"),
    path("history", views.history, name="history"),
    path("result", views.result, name="result"),
    path("download_csv", views.download_csv, name="download_csv"),
    path("test", views.test, name="test")] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
