from typing import Any
from django import http
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

class StaffRequiredMixin(object):
    """
    Implies that the user is part of the staf
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        """ if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login')) """
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
# Create your views here.
class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    def get_success_url(self):
        return reverse_lazy('pages:pages')
    
@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

