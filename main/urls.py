from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.IndexPage.as_view(), name="index"),
    path("weather_bot/", include("weather_bot.urls")),
    path("pc_info/", include("pc_info.urls")),
    path("towns/", include("towns.urls")),
    path("gold_rates/", include("gold_rates.urls")),
    path("github/", views.GitPage.as_view()),
    path('admin/', admin.site.urls),
]
