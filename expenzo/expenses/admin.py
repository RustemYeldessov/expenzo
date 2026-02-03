from django.contrib import admin
from expenzo.expenses.models import Expense
from expenzo.categories.models import Category
from expenzo.sections.models import Section
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'amount', 'category', 'user')
    list_filter = ('date', 'category', 'section')
    search_fields = ('description',)

admin.site.register(Category)
admin.site.register(Section)