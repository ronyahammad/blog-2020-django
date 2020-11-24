from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post,Category,Comment
from accounts.models import Profile
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404,reverse
from django.contrib import messages
from .forms import CommentForm
from django.views.generic.edit import FormMixin

class CustomContentMixin:
    def get_context_data(self, **kwargs):
        context = super(CustomContentMixin, self).get_context_data(**kwargs)
        context['user_list']= Profile.objects.all()
        context['category_list']=Category.objects.all()
        return context


class BlogappListView(CustomContentMixin,ListView):
    model = Category,Profile
    template_name = 'home.html'
    context_object_name='post_list'
    queryset=Post.objects.all()
    paginate_by=7
    
   
class BlogappUpdateView(LoginRequiredMixin, UserPassesTestMixin, CustomContentMixin,UpdateView ):
    model=Post
    template_name='post_edit.html'
    fields=('title','body','image','category')
    login_url='login'   
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user
    
class BlogappDetailView(FormMixin,CustomContentMixin,DetailView):
    model=Post
    template_name='post_detail.html'
    #login_url='login'
    form_class=CommentForm
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    def get_context_data(self, **kwargs):
        context = super(BlogappDetailView, self).get_context_data(**kwargs)
        context['comments']=Comment.objects.filter(post=self.object)
        context['comment_form']=CommentForm()
        context['user_list']= Profile.objects.all()
        context['category_list']=Category.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = self.get_form()
        if comment_form.is_valid():
            return self.form_valid(comment_form)
        else:
            return self.form_invalid(comment_form)

    def form_valid(self, comment_form):
        comment_form.instance.post = self.object
        comment_form.instance.author=self.request.user
        comment_form.save()
        return super().form_valid(comment_form)
       

class BlogappDeleteView(LoginRequiredMixin, UserPassesTestMixin, CustomContentMixin, DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')
    login_url='login'
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user
    

class BlogappCreateView(LoginRequiredMixin, CustomContentMixin, CreateView):
    model=Post
    template_name='post_new.html'
    login_url='login'
    fields=('title','body','image','category')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
#https://learndjango.com/tutorials/django-search-tutorial
#https://stackoverflow.com/questions/52688084/how-do-i-add-a-searchbar-through-class-based-view

class SearchView(CustomContentMixin,ListView):
    model=Post
    template_name='search.html'
    paginate_by=7
    def get_queryset(self):
        query=self.request.GET['query']
        post_listTitle=Post.objects.filter(title__icontains=query)
        post_listContent=Post.objects.filter(body__icontains=query)
        post_list=post_listTitle.union(post_listContent)
        return post_list
    
class CategoryListView(CustomContentMixin,ListView):
    model=Post
    template_name='post_category.html'
    paginate_by=7
    def get_queryset(self):
        self.category=get_object_or_404(Category,pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category)
    
