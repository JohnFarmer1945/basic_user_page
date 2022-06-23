from django.urls import path
from . import views


urlpatterns =  [
path("", views.briefing_page, name="briefing_page"),
]