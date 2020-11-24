from django.urls import path
from .views import SignUpView, ProfileDetailView, ProfileEditView, ActivateAccount

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
   	path('activate/<uidb64>/<token>/',
   	     ActivateAccount.as_view(), name='activate'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/edit', ProfileEditView.as_view(), name='profile_edit'),
    ]
