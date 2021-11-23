from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
    path("", views.IndexPage.as_view(), name="index"),
    path("weather_bot/", include("weather_bot.urls"), name="weather_bot"),
    path("pc_info/", include("pc_info.urls"), name="pc_info"),
    path("towns/", include("towns.urls"), name="towns"),
    path("gold_rates/", include("gold_rates.urls"), name="gold_rates"),
    path("github/", views.GitPage.as_view(), name="git"),
    path('admin/', admin.site.urls, name="admin"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
