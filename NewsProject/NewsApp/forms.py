from django import forms
from NewsApp.models import Query_data1,Resume
class GetQueryForm(forms.ModelForm):
    class Meta:
        model = Query_data1
        fields = ('name','email','query')

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name','email','file')
