from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': _('Name'),
        }