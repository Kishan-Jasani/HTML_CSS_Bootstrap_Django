from django.contrib import admin
from databaseapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','emp_no','emp_name','emp_sal','emp_add']

admin.site.register(Employee,EmployeeAdmin)
