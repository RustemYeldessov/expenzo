from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Expense
from expenzo.categories.models import Category
from expenzo.sections.models import Section


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['section', 'date', 'category', 'description', 'amount']

        widgets = {
            'section': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'id_section'

                }),
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control'

                }),
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'id_category'

                }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': _('Enter description of the expense')

                }),
            'amount': forms.NumberInput(
                attrs={
                    'class': 'form-control'

                }),
        }