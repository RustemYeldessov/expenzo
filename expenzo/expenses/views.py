from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (CreateView, UpdateView,
                                  DetailView, DeleteView, ListView)

from .filters import ExpenseFilter
from .forms import ExpenseForm
from .models import Expense


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expenses/index.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        queryset = Expense.objects.all()
        self.filterset = ExpenseFilter(self.request.GET, queryset=queryset)

        queryset = self.filterset.qs

        if self.request.GET.get("self_expenses"):
            queryset = queryset.filter(author=self.request.user)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filterset
        return context

class ExpenseDetailView(LoginRequiredMixin, DetailView):
    model = Expense
    template_name = 'expenses/show.html'
    context_object_name = 'expense'

class ExpenseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/create.html'
    success_url = 'expenses_index'
    success_message = _('Expense created successfully')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ExpenseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expanses/update.html'
    success_url = 'expenses_index'
    success_message = _('Expense updated successfully')

class ExpenseDeleteView(LoginRequiredMixin, SuccessMessageMixin,
                        UserPassesTestMixin, DeleteView):
    model = Expense
    template_name = 'expenses/delete.html'
    success_url = 'expenses_index'
    success_message = _('Expense deleted successfully')

    def test_func(self):
        expense = self.get_object()
        return expense.author == self.request.user

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        messages.error(self.request, _("Only the author can delete an issue."))
        return redirect(self.success_url)