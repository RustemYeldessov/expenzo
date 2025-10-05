from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category
from .forms import CategoryForm


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'categories/index.html'
    context_object_name = 'categories'

class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CategoryForm
    template_name = 'categories/create.html'
    success_url = reverse_lazy('categories:index')
    success_message = _('Category creates successfully')

class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/update.html'
    success_url = reverse_lazy('categories:index')
    success_message = _('Category updated successfully')

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories/delete.html'
    success_url = reverse_lazy('categories:index')
    success_message = _('Category deleted successfully')

    def post(self, request, *args, **kwargs):
        try:
            response = self.post(request, *args, **kwargs)
            messages.success(self.request, self.success_message)
            return response
        except ProtectedError:
            messages.error(
                self.request,
                _('It is impossible to delete the category \
                  because it is being used')
            )
            return redirect(self.success_url)