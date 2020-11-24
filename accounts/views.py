from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView,CreateView,View
from django.views.generic.edit import UpdateView, FormMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import ProfileCreationForm
#from django.contrib.auth.models import User
from .models import Profile
from blog.models import Post
from blog.views import CustomContentMixin

from django.shortcuts import get_object_or_404, render, redirect
from django import forms
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import TokenGenerator
from django.contrib.auth import login
from django.http import request


class SignUpView(View, CustomContentMixin):
    form_class = ProfileCreationForm
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account till it is confirmed
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': TokenGenerator.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(
                request, ('Please Confirm your email to complete registration.'))

            return redirect('login')

        return render(request, self.template_name, {'form': form})

class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = Profile.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, Profile.DoesNotExist):
            user = None
        if user is not None and TokenGenerator.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('home')


class ProfileDetailView(CustomContentMixin,DetailView):
    template_name='profile.html'
    model=Profile
    def get_user_profile(self,pk):
        return get_object_or_404(Profile,pk=pk)
    

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, CustomContentMixin,UpdateView):
    model=Profile
    template_name='profile_edit.html'
    fields=['name','bio','birthdate','location','gender',]
    login_url='login'
    success_url = reverse_lazy('home')
    def get_user_profile_edit(self,pk):
        return get_object_or_404(Profile,pk=pk)

    def test_func(self):
        return self.get_object() == self.request.user
