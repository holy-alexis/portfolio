from django.urls.conf import path
from . import views

urlpatterns = [
    path("", views.IndexPage.as_view()),
    path("dates/", views.DatesPage.as_view()),
    path("date/<str:date>", views.RatePage.as_view(), name="date")
]
