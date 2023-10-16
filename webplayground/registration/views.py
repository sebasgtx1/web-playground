from django.contrib.auth.forms import UserCreationForm
from django.forms.models import BaseModelForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login') + '?register'
    
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        #Real time modification
        form.fields['username'].widget = forms.TimeInput(attrs={'class':'form-control mb-2', 'placeholder': 'Username'})
        form.fields['password1'].widget = forms.TimeInput(attrs={'class':'form-control mb-2', 'placeholder': 'Password'})
        form.fields['password2'].widget = forms.TimeInput(attrs={'class':'form-control mb-2', 'placeholder': 'Repeat Password'})
        return form
