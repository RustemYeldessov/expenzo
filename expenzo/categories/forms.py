from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Categories


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }