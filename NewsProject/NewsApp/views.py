from django.shortcuts import render, get_object_or_404
from NewsApp.models import News,Query_data1,Resume
from NewsApp.forms import GetQueryForm,ResumeForm
from django.http import HttpResponse
from django.core.mail import send_mail
from NewsProject import settings
import datetime
# Create your views here.
def home_page_view(request):
    return render(request,'NewsApp/home.html')

def all_news(request):
    news = News.objects.all()
    dict = {'news':news}
    return render(request,'NewsApp/all.html',dict)

def career(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid()==False:
            newdoc = Resume(request.FILES['file'])
            newdoc.save()
            instance = form.save(commit=False)
            instance.name = form.cleaned_data.get('name')
            instance.email = form.cleaned_data.get('email')
            instance.save()
            return render(request,'NewsApp/thankyou.html')
    else:
        form = ResumeForm()
        dict = {'form':form}
        return render(request,'NewsApp/career.html',dict)

def contact(request):
    if request.method == 'POST':
        form = GetQueryForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = form.cleaned_data.get('name')
            instance.email = form.cleaned_data.get('email')
            instance.query = form.cleaned_data.get('query')
            send_mail(
                        'Message from '+instance.name,
                        'Thank you for your query!! We will get back to you!!',
                        settings.EMAIL_HOST_USER,
                        [instance.email],
                        fail_silently=False,
                    )
            instance.save()
        return render(request,'NewsApp/thankyou.html')
    else:
        form = GetQueryForm()
        dict = {'form':form}
        return render(request,'NewsApp/contact.html',dict)

def politics_view(request):
    news = News.objects.filter(id__in=[4,5,6,7,8])
    dict = {'news':news}
    return render(request,'NewsApp/politics.html',dict)

def bollywood_view(request):
    news = News.objects.filter(id__in=[9,10,11,12,13])
    dict = {'news':news}
    return render(request,'NewsApp/bollywood.html',dict)

def sports_view(request):
    news = News.objects.filter(id__in=[14,15,16,17,18])
    dict = {'news':news}
    return render(request,'NewsApp/sports.html',dict)
