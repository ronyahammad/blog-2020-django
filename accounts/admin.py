from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
#from blog.views import CustomContentMixin

class CustomUserAdmin(UserAdmin):
    model=CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'username','name','age']
    
admin.site.register(CustomUser,CustomUserAdmin)