from django.urls import path
from . import views

app_name = "towns"

urlpatterns = [
    path("", views.IndexPage.as_view(), name="index"),
    path("search/", views.SearchPage.as_view(), name="search"),
    path('search/towns/', views.TownsList.as_view(), name="towns_list"),
    path('search/town/<str:str_to_search>/', views.SearchByTown.as_view(), name='search_by_town'),
    path('search/people/<str:str_to_search>/', views.SearchByPeople.as_view(), name='search_by_people'),
    path('search/id/<int:pk>/', views.PersonView.as_view(), name="id")
]
