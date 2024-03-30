from django.urls import path
from .views import all_services_api_view

urlpatterns= [
    path("",all_services_api_view, name="api_page")
]