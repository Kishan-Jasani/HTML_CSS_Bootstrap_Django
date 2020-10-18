from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def home(request):
    dt = datetime.datetime.now()
    dic = {"date":dt}
    return render(request,'newproject/home.html',dic)
