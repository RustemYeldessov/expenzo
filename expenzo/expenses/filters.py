import django_filters
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import Expense
from expenzo.categories.models import Category
from ..sections.models import Section

User = get_user_model()


class ExpenseFilter(django_filters.FilterSet):
    section = django_filters.ModelChoiceFilter(
        queryset=Section.objects.all(),
        label=_("Section")
    )
    date = django_filters.DateFromToRangeFilter(
        field_name="date",
        label=_("Date")
    )

    author = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label=_("Author")
    )

    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label=_("Category")
    )

    class Meta:
        model = Expense
        fields = ["section", "date", "author", "category"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['author'].field.label_from_instance = (
            lambda u: f"{u.first_name} {u.last_name}".strip() or u.username
        )