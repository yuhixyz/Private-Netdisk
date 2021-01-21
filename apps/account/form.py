from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='账号', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
