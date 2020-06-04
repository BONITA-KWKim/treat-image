from django import forms

class UploadImageForm(forms.Form):
    raw_image = forms.ImageField()
