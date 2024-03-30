from django.shortcuts import render
from django.http import Http404
from api.models import Service


def index_page(request):
    try:
        services = Service.objects.all()
    except Service.DoesNotExist:
        raise Http404("Service not exist")

    return render(request, "website/index.html", {"services": services})

