from django.contrib import admin
from NA.models import Customer,Resume
# Register your models here.
class Navo(admin.ModelAdmin):
    list_display = ['id','no','name']

class Navo1(admin.ModelAdmin):
    list_display = ['id','file']

admin.site.register(Customer,Navo)
admin.site.register(Resume,Navo1)
