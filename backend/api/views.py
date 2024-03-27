from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ServiceSerializer
from .models import Service
# Create your views here.


@api_view(['GET'])
def all_services(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services,many=True)
        return Response(serializer,status=status.HTTP_200_OK)