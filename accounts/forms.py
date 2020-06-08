from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from blog.models import Category

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')
        def get_context_data(self, **kwargs):
            context = super(UserCreationForm, self).get_context_data(**kwargs)
            context['user_list']= CustomUser.objects.all()
            context['category_list']=Category.objects.all()
            return context
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        def get_context_data(self, **kwargs):
            context = super(CustomUserChangeForm, self).get_context_data(**kwargs)
            context['user_list']= CustomUser.objects.all()
            context['category_list']=Category.objects.all()
            return context