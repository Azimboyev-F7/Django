from django import forms
from django.core.exceptions import ValidationError
from .models import New

class NewForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'content', 'image']
        model = New

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

    def clean_title(self):
        if self.cleaned_data['title'].replace(" ", "").isalnum():
            return self.cleaned_data['title']
        raise ValidationError("Title must be alphanumeric")
