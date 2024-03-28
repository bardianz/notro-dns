from django.shortcuts import render
from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ServiceSerializer
from .models import Service
# Create your views here.


def index_page(request):
    try:
        services = Service.objects.all()
    except Service.DoesNotExist:
        raise Http404("Service not exist")

    return render(request, "api/index.html", {"services": services})






@api_view(['GET'])
def all_services(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)