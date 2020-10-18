from django import forms
from NA.models import Resume

class ResumeDownloader(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('file',)
