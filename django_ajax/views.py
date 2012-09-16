
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('index.html')

def gettime(request):
    if request.is_ajax():
        return HttpResponse(str(datetime.now()))
    
    # Graceful degradation
    return render_to_response('index.html', {'time': str(datetime.now()) })