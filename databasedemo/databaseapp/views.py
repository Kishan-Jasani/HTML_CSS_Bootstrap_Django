from django.shortcuts import render
from databaseapp.models import Employee
# Create your views here.
def employee_table_data(request):
    employees = Employee.objects.all()
    dict = {'emp':employees}
    return render(request,'db/new.html',dict)
