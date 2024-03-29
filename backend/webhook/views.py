import subprocess
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['POST'])
def webhook_git_pull(request):
    if request.method == 'POST':
        # subprocess.run(['cd', 'dnschanger/dns-changer'])


        

        directory = 'dns-changer'
        try:
            # اجرای دستور cd در یک فرآیند فرعی
            subprocess.run(["cd", directory], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error {e}")
            return Response({"error": e},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        try:
            result = subprocess.run(["pwd"], shell=True, check=True, stdout=subprocess.PIPE, text=True)
            pwd_output = result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return Response({"error": e , "pwd" : pwd_output}, status=status.HTTP_406_NOT_ACCEPTABLE)


        subprocess.run(['git', 'pull'])
        return Response({"pwd" : pwd_output},status=status.HTTP_200_OK)
    else:
        return Response(None,status=status.HTTP_400_BAD_REQUEST,)
    

@api_view(['POST'])
def webhook_reloader(request):
    if request.method == 'POST':
        subprocess.run(['touch', '/var/www/dnschanger_pythonanywhere_com_wsgi.py'])
        return Response(None,status=status.HTTP_200_OK)
    else:
        return Response(None,status=status.HTTP_400_BAD_REQUEST)
