from django.shortcuts import render
from django.http import HttpResponse
import datetime

def matrimonial(request):
    dt=datetime.datetime.now()
    my_dict={'date':dt}
    return render(request,'Matrimonial/home.html',my_dict)

def greetings(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    if h<12:
        return render(request,'Matrimonial/morning.html')
    elif h<16:
        return render(request,'Matrimonial/afternoon.html')
    elif h<21:
        return render(request,'Matrimonial/evening.html')
    else:
        return render(request,'Matrimonial/night.html')

def home(request):
    return render(request,'Matrimonial/home.html')

def morning(request):
    return render(request,'Matrimonial/morning.html')
def afternoon(request):
    return render(request,'Matrimonial/afternoon.html')
