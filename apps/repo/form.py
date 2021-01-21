from django import forms
from .models import FileRepository


class MakeDirectoryForm(forms.ModelForm):
    class Meta:
        model = FileRepository
        fields = ['name']


class UploadFileForm(forms.Form):
    pass
