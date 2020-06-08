from .views import (
    BlogappListView,
    BlogappUpdateView,
    BlogappDetailView,
    BlogappDeleteView,
    BlogappCreateView,
    CategoryListView,
    SearchView,
    
    )
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from . import views
urlpatterns = [
    
    path('home/',BlogappListView.as_view(),name='home'),
    path('<int:pk>/edit/',BlogappUpdateView.as_view(),name='post_edit'),
    path('<int:pk>/',BlogappDetailView.as_view(),name='post_detail'),
    path('<int:pk>/delete',BlogappDeleteView.as_view(),name='post_delete'),
    path('new/',BlogappCreateView.as_view(),name='post_new'),
    path('search/',SearchView.as_view(),name='search'),
    path('category/<int:pk>/',CategoryListView.as_view(),name='category_list'),
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
