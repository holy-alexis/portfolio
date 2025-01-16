from django.urls.conf import path
from . import views

app_name = 'upscaler'

urlpatterns = [
    path("", views.UpscalerIndexPage.as_view(), name="index"),
]
