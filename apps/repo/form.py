from django import forms
from .models import FileRepository


class DirectoryForm(forms.ModelForm):
    class Meta:
        model = FileRepository
        fields = ['name']
