from django import forms

from .models import User


class SignIn(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password')


class UploadForm(forms.Form):
    name = forms.CharField(max_length=255)
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
