from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

import subprocess
from django.http import HttpResponse, HttpResponseBadRequest
# def webhook_handler(request):
#     if request.method == 'POST':
#         # Pull changes from Git repository
#         subprocess.run(['git', 'pull'])
#         return HttpResponse('Webhook received and changes pulled successfully.')
#     else:
#         return HttpResponseBadRequest('Invalid request method.')

@api_view(['POST'])
def webhook_handler(request):
    if request.method == 'POST':
        subprocess.run(['git', 'pull'])
        return Response(None,status=status.HTTP_200_OK)
    else:
        return Response(None,status=status.HTTP_400_BAD_REQUEST)
