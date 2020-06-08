from django.views.generic import CreateView
from .models import CustomUser
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from blog.models import Category
from blog.views import CustomContentMixin

class SignUpView(CreateView,CustomContentMixin):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
