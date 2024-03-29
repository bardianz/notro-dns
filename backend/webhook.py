import subprocess
from django.http import HttpResponse, HttpResponseBadRequest
def webhook_handler(request):
    if request.method == 'POST':
        # Pull changes from Git repository
        subprocess.run(['git', 'pull'])
        return HttpResponse('Webhook received and changes pulled successfully.')
    else:
        return HttpResponseBadRequest('Invalid request method.')