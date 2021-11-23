from django.urls.conf import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "gold"

urlpatterns = [
    path("", views.IndexPage.as_view(), name="index"),
    path("dates/", views.DatesPage.as_view(), name="dates"),
    path("date/<str:date>/", views.RatePage.as_view(), name="date")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
