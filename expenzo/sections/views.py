from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Section
from .forms import SectionForm


class SectionListView(LoginRequiredMixin, ListView):
    model = Section
    template_name = 'sections/index.html'
    context_object_name = 'sections'

class SectionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = SectionForm
    template_name = 'sections/create.html'
    success_url = reverse_lazy('sections_index')
    success_message = _('Section creates successfully')

class SectionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Section
    form_class = SectionForm
    template_name = 'sections/update.html'
    success_url = reverse_lazy('sections_index')
    success_message = _('Section updated successfully')

class SectionDeleteView(LoginRequiredMixin, DeleteView):
    model = Section
    template_name = 'sections/delete.html'
    success_url = reverse_lazy('sections_index')
    success_message = _('Section deleted successfully')

    def post(self, request, *args, **kwargs):
        try:
            response = self.post(request, *args, **kwargs)
            messages.success(self.request, self.success_message)
            return response
        except ProtectedError:
            messages.error(
                self.request,
                _('It is impossible to delete the section \
                  because it is being used')
            )
            return redirect(self.success_url)