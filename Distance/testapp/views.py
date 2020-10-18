from django.shortcuts import render, get_list_or_404, get_object_or_404
from testapp.models import Measurement
from testapp.forms import MeasurementModelForm
# Create your views here.
def calculate_distance_view(request):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.destination = form.cleaned_data.get('destination')
        instance.location = 'Surat'
        instance.distace = 450
        instance.save()

    dict = {'distance':obj,'form':form}
    return render(request, 'distance/main.html',dict)
