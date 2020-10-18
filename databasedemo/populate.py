import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','databasedemo.settings')
django.setup()
from databaseapp.models import *
from faker import Faker
from random import *
fk = Faker()
def populate(n):
    for i in range(0,n):
        no=randint(100001,9999999)
        nm=fk.name()
        sl=randint(12000,90000)
        add=fk.city()
        emp_record = Employee.objects.get_or_create(emp_no=no,emp_name=nm,emp_sal=sl,emp_add=add)

populate(10)
