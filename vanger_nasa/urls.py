from django.urls import path

from vanger_nasa.apps import VangerNasaConfig
from vanger_nasa.views import HomePageView

app_name = VangerNasaConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]