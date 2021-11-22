from django.urls import path
from . import views

app_name = "towns"

urlpatterns = [
    path("", views.IndexPage.as_view()),
    path("search/", views.SearchPage.as_view()),
    path('search/towns', views.TownsList.as_view()),
    path('search/town/<str:str_to_search>', views.SearchByTown.as_view(), name='search_town'),
    path('search/people/<str:str_to_search>', views.SearchByPeople.as_view(), name='search'),
    path('search/id/<int:pk>', views.PersonView.as_view(), name="id")
]
