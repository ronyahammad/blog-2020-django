from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

class ProfileCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('username', 'email',)

