from django.contrib import admin
from NewsApp.models import News,Query_data1,Resume
# Register your models here.
class ShowField(admin.ModelAdmin):
    list_display = ['id','news']

class ShowField1(admin.ModelAdmin):
    list_display = ['id','name','email','query']

class ShowField2(admin.ModelAdmin):
    list_display = ['id','name','email','file']

admin.site.register(News,ShowField)
admin.site.register(Query_data1,ShowField1)
admin.site.register(Resume,ShowField2)
