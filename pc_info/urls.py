from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('receive/', views.Receive.as_view(), name='receive'),
]
