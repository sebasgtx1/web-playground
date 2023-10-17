from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. 254 characters maximum and must be valid')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('There is already an account associated with this email')
        return email
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'bio', 'link')
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio' : forms.Textarea(attrs={'class': 'form-control mt-3', 'rows' : 3, 'placeholder': 'Biography'}),
            'link' : forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Link'}),
        }