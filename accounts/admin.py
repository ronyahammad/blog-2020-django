from django.contrib import admin
from .models import Profile
#from django.contrib.auth.admin import UserAdmin
#from .forms import ProfileCreationForm,ProfileEditForm

#class ProfileUserAdmin(UserAdmin):
    #add_form=ProfileCreationForm
    #form=ProfileEditForm
    #model=Profile
    #List_display=['email', 'username', 'birthdate', 'is_staff',]
admin.site.register(Profile)
