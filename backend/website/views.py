from django.shortcuts import render
from django.http import Http404
from api.models import Server
from website.models import HelpPage

def index_page(request):
    try:
        services = Server.objects.all()
    except Server.DoesNotExist:
        raise Http404("Service not exist")

    return render(request, "website/index.html", {"services": services})

def help_page(request):
    try:
        help = HelpPage.objects.last()
        context = {"help_content": help}
    except HelpPage.DoesNotExist:
        raise Http404("Page not exist")
    if help == None:
        context = {"help_content": "No Content!"}

    return render(request, "website/help.html", context)

