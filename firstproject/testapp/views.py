from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello_world_view(request):
    return HttpResponse("<h1>This is response from Django Application</h1>")

def date_time_view(request):
    date=datetime.datetime.now()
    s="The current date and time at the server is: "+str(date)
    return HttpResponse(s)

def params(params):
    return HttpResponse("<h1>Hello "+params+" !!!</h1>")
