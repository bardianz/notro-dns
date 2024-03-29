import subprocess
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['POST'])
def webhook_git_pull(request):
    if request.method == 'POST':
        subprocess.run(['cd', 'dnschanger/dns-changer'])
        subprocess.run(['git', 'pull'])
        return Response(None,status=status.HTTP_200_OK)
    else:
        return Response(None,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def webhook_reloader(request):
    if request.method == 'POST':
        subprocess.run(['touch', '/var/www/dnschanger_pythonanywhere_com_wsgi.py'])
        return Response(None,status=status.HTTP_200_OK)
    else:
        return Response(None,status=status.HTTP_400_BAD_REQUEST)
