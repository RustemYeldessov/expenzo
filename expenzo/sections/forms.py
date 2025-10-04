from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Section


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name']
        labels = {
            'name': _('Name'),
        }