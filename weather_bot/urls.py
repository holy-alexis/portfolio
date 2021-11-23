from django.urls.conf import path
from . import views

app_name = "weather_bot"

urlpatterns = [
    path("", views.IndexPage.as_view(), name="index"),
]