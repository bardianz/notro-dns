from django.urls import path
from .views import index_page,help_page

urlpatterns= [
    path('', index_page,name="home_page"),
    path('help/', help_page,name="help_page"),
]