from django.urls import path
from .views import webhook_git_pull,webhook_reloader

urlpatterns= [
    path("pull/",webhook_git_pull),
    path("reload/",webhook_reloader),
]