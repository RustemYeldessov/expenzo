from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.utils.translation import gettext_lazy as _
from django_filters.views import FilterView

from expenzo.core.mixins import SafeDeleteMixin
from .forms import ExpenseForm
from .models import Expense
from .filters import ExpenseFilter

User = get_user_model()


class ExpenseListView(LoginRequiredMixin, FilterView):
    model = Expense
    template_name = "expenses/index.html"
    context_object_name = "expenses"
    filterset_class = ExpenseFilter

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class ExpenseDetailView(LoginRequiredMixin, DetailView):
    model = Expense
    template_name = "expenses/show.html"
    context_object_name = "expense"

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class ExpenseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Expense
    template_name = "expenses/create.html"
    form_class = ExpenseForm
    success_url = reverse_lazy("expenses:index")
    success_message = _("Expense created successfully")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # Этот метод позволяет узнать о текущем пользователе,
    # чтобы отфильтровать список категорий
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ExpenseUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    UpdateView
):
    model = Expense
    template_name = "expenses/update.html"
    form_class = ExpenseForm
    success_url = reverse_lazy("expenses:index")
    success_message = _("Expense updated successfully")

    def test_func(self):
        expense = self.get_object()
        return self.request.user == expense.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def handle_no_permission(self):
        messages.error(
            self.request,
            _("Yot have no permission to perform this action")
        )
        return redirect("expenses:index")

class ExpenseDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    SafeDeleteMixin,
    DeleteView
):
    model = Expense
    template_name = "expenses/delete.html"
    success_url = reverse_lazy("expenses:index")
    success_message = _("Expense deleted successfully")

    def test_func(self):
        expense = self.get_object()
        return self.request.user == expense.user

    def handle_no_permission(self):
        messages.error(
            self.request,
            _("Yot have no permission to perform this action")
        )
        return redirect("expenses:index")