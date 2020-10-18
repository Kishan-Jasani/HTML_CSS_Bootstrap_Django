from django.shortcuts import render
from django.http import HttpResponse
from NP.forms import ResumeDownloader
from NA.functions import Handle_upload_file
# Create your views here.
def view1(request):
    return HttpResponse("<h1>View1</h1>")

def view2(request):
    if request.method == 'POST':
        form = ResumeDownloader(request.FILES, request.POST)
        if form.is_valid():
            Handle_upload_file(request.FILES['file'])
            instance = form.save(commit=False)
            instance.save()
        return HttpResponse('File Uploaded Successfully')
    else:
        form= ResumeDownloader()
        dict = {'form':form}
        return render(request,'new/home.html',dict)
