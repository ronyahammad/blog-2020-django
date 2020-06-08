from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField 
from django.utils.timezone import now,datetime
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from .validators import validate_file_size

class Category(models.Model):
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title
class Post(models.Model):
    title = models.CharField(max_length=255)
    body=RichTextField(blank=True,null=True)
    image=models.FileField(upload_to="mediaphoto",validators=[validate_file_size])
    topImage=ImageSpecField(source='image',processors=[ResizeToFill(750,300)],format='PNG',options={'quality':60})  
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
        
class Comment(models.Model):
    post=models.ForeignKey(to=Post,on_delete=models.CASCADE,related_name='comments',null=True)
    comment=models.TextField(max_length=5000)
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)
    reply=models.ForeignKey('Comment',null=True,on_delete=models.CASCADE,related_name='replies')
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('post_detail')