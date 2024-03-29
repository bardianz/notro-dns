import subprocess
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['POST'])
def webhook_handler(request):
    if request.method == 'POST':
        print("before cd --------------------------------------")
        subprocess.run(['cd', '/home/dnschanger/dns-changer/backend'])
        print("after cd --------------------------------------")
        subprocess.run(['git', 'pull'])
        subprocess.run(['cd', '/home/dnschanger/dns-changer/backend'])
        print("before reload --------------------------------------")

        subprocess.run(['touch', '/var/www/your_domain_wsgi.py'])
        print("after reload --------------------------------------")

        return Response(None,status=status.HTTP_200_OK)
    else:
        return Response(None,status=status.HTTP_400_BAD_REQUEST)
