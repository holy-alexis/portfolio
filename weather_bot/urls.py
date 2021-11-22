from django.urls.conf import path
from . import views

urlpatterns = [
    path("", views.IndexPage.as_view()),
]
