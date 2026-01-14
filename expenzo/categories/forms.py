from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Category


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }