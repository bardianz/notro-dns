from django.urls import path
from .views import all_services

urlpatterns= [
    path("",all_services)
]