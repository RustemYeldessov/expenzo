import django_filters
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import Expense
from expenzo.categories.models import Category
from expenzo.sections.models import Section

User = get_user_model()


class ExpenseFilter(django_filters.FilterSet):
    section = django_filters.ModelChoiceFilter(
        queryset=Section.objects.none(),
        label=_("Section")
    )
    date = django_filters.DateFromToRangeFilter(
        field_name="date",
        label=_("Date")
    )

    # user = django_filters.ModelChoiceFilter(
    #     queryset=User.objects.all(),
    #     label=_("Author")
    # )

    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.none(),
        label=_("Category")
    )

    class Meta:
        model = Expense
        fields = ["section", "date", "category"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = getattr(self.request, 'user', None)

        if user:
            self.filters['section'].queryset = Section.objects.filter(user=user)
            self.filters['category'].queryset = Category.objects.filter(user=user)
