
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('index.html')

def gettime(request):
    if request.is_ajax():
        return HttpResponse('<div>' + str(datetime.now()) +'</div>')
    
    # Graceful degradation
    return render_to_response('gettime.html', {'time': str(datetime.now()) })