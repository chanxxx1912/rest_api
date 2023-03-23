from django import forms
from .models import ConvertedFile

class ConvertedFileForm(forms.ModelForm):
    class Meta:
        model = ConvertedFile
        fields = ('file',)
