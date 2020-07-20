from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader #html 불러오려면 import
from datetime import datetime

# Create your views here.
# page하나에 method 하나

def index(request):
    template = loader.get_template('index.html')
    now = datetime.now()
    context = {
        'current_date': now
    }
    return HttpResponse(template.render(context, request))

def select(request, year):
    message = 'Select deeplearning model.'
    return HttpResponse(message)

def result(request):
    message = 'result of deeplearning'
    return HttpResponse(message)
